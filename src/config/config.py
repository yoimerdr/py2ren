import json
import os.path

from .exceptions import NonLoadableSourceConfigurationPath, NonLoadableConfigurationPath
from ..converter.bases import KNOWN_BASES
from ..utils.filepath import listfiles, filename


class Init(object):
    __slots__ = ('_name', '_level', '_class_bases')

    def __init__(self, name=None, level=0, class_bases=None):
        name = name.strip() if name is not None else None
        self._name = name if name else None
        self._level = level
        self._class_bases = class_bases if isinstance(class_bases, dict) else None

    @classmethod
    def _get_params(cls, dct):
        return {
            "name": dct.get('name', None),
            "level": dct.get('initLevel', None),
            "class_bases": dct.get('classBases', None),
        }

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def class_bases(self):
        return self._class_bases or {}

    @classmethod
    def from_dict(cls, dct):
        return dct if isinstance(dct, cls) else cls(**cls._get_params(dct))

    def to_dict(self):
        source = {}
        if self.name:
            source['name'] = self.name
        if self.level is not None:
            source['initLevel'] = self.level

        if self.class_bases:
            source['classBases'] = self.class_bases
        return source


class FileModule(Init):
    __slots__ = ('_ignore',)

    def __init__(self, name=None, level=0, class_bases=None, ignore=False):
        super(FileModule, self).__init__(name, level, class_bases)
        self._ignore = bool(ignore)

    @property
    def ignore(self):
        return self._ignore

    @classmethod
    def _get_params(cls, dct):
        params = super(FileModule, cls)._get_params(dct)
        params['ignore'] = dct.get('ignore', False)
        return params

    def to_dict(self):
        source = super(FileModule, self).to_dict()
        if self.ignore:
            source['ignore'] = self.ignore

        return source


class Module(FileModule):
    __slots__ = ('_modules',)

    def __init__(self, name=None, modules=None, level=0, class_bases=None, ignore=False):
        super(Module, self).__init__(name, level, class_bases, ignore)
        self._modules = modules if isinstance(modules, dict) else None

    @property
    def modules(self):
        return self._modules

    @staticmethod
    def map_modules(modules):
        if not isinstance(modules, dict):
            return None
        for key in modules:
            from_dict = FileModule.from_dict
            if "modules" in modules[key] and modules[key]['modules']:
                from_dict = Module.from_dict
            modules[key] = from_dict(modules[key])
        return modules

    @classmethod
    def _get_params(cls, dct):
        params = super(Module, cls)._get_params(dct)
        params["modules"] = Module.map_modules(dct.get('modules', None))
        return params

    def to_dict(self):
        source = super(Module, self).to_dict()
        source['modules'] = {k: self.modules[k].to_dict() for k in self.modules}
        return source


class FileConfig(Init):
    __slots__ = ('_stored_modules',)

    def __init__(self, name=None, stored_modules=None, level=0, class_bases=None):
        super(FileConfig, self).__init__(name, level, class_bases)
        self._stored_modules = tuple(stored_modules) if isinstance(stored_modules, (list, tuple)) else None

    @property
    def stored_modules(self):
        return self._stored_modules or ()

    @classmethod
    def _get_params(cls, dct):
        params = super(FileConfig, cls)._get_params(dct)
        params["stored_modules"] = dct.get('storedModules', None)
        return params

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            return cls.from_dict(json.load(f))

    def to_dict(self):
        source = super(FileConfig, self).to_dict()
        source['storedModules'] = self.stored_modules
        return source


class ModuleConfig(FileConfig):
    __slots__ = ('_modules',)

    def __init__(self, name=None, stored_modules=None, modules=None, level=0, class_bases=None):
        super(ModuleConfig, self).__init__(name, stored_modules, level, class_bases)
        self._modules = modules if isinstance(modules, dict) else None

    @property
    def modules(self):
        return self._modules

    @classmethod
    def _get_params(cls, dct):
        params = super(ModuleConfig, cls)._get_params(dct)
        params["modules"] = Module.map_modules(dct.get('modules', None))
        return params

    def to_dict(self):
        source = super(ModuleConfig, self).to_dict()
        source['modules'] = {k: self.modules[k].to_dict() for k in self.modules}
        return source


def load_dict(source):
    from_dict = FileConfig.from_dict
    if "modules" in source and source['modules']:
        from_dict = ModuleConfig.from_dict

    return from_dict(source)


def load_file(path):
    if not os.path.isfile(path):
        raise NonLoadableConfigurationPath(path)

    with open(path) as f:
        source = json.load(f)

    return load_dict(source)


def load(path, creates=True):
    if os.path.isdir(path):
        filepath = os.path.join(path, "py2ren.config.json")
    elif os.path.isfile(path):
        filepath = os.path.join(os.path.dirname(path), "py2ren.config.json")
    else:
        raise NonLoadableSourceConfigurationPath(path)
    if creates and not os.path.isfile(filepath):
        return dump(path)
    return load_file(filepath)


def create(path, name=None, store_modules=None, init_level=0, class_bases=None):
    path = os.path.normpath(path)

    cfg_name = os.path.basename(path) if name is None else None

    if os.path.isdir(path):
        modules = {}
        for filepath in listfiles(path, ('.py',)):
            parts = filepath.split(os.path.sep)
            current = modules
            level = None
            for level, part in enumerate(parts[:-1], start=1):
                if part not in current:
                    current[part] = {"modules": {}, "initLevel": init_level - level - 1}
                current = current[part]["modules"]
            source = {}
            if level is None:
                if parts[-1] != "__init__.py":
                    source["initLevel"] = init_level - 1
            elif parts[-1] == "__init__.py":
                source["initLevel"] = init_level - level
            current[parts[-1]] = source
        return ModuleConfig(name, store_modules, Module.map_modules(modules), init_level, class_bases or KNOWN_BASES)

    elif os.path.isfile(path):
        if cfg_name is not None:
            name = filename(cfg_name)
        return FileConfig(name, store_modules, init_level, class_bases or KNOWN_BASES)
    raise NonLoadableSourceConfigurationPath(path)


def dump_config(folder, config):
    path = os.path.join(folder, "py2ren.config.json")
    with open(path, 'w') as f:
        json.dump(config.to_dict(), f, indent=2, ensure_ascii=False)


def dump(path, name=None, store_modules=None, init_level=0, class_bases=None):
    config = create(path, name, store_modules, init_level, class_bases)
    path = path if isinstance(config, ModuleConfig) else os.path.dirname(path)
    dump_config(path, config)
    return config
