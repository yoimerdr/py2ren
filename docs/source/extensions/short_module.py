import argparse
import re

cfg = argparse.Namespace(modules=None)


def _checks_modules_signatures(source, docs=False):
    if not cfg.modules or not source:
        return source

    pattern = r"({}).([\w.]+)".format("|".join(map(re.escape, cfg.modules)))
    return re.sub(pattern, r"~\1.\2", source)


def _process_docstrings(app, what, name, obj, options, lines):
    result = _checks_modules_signatures("\n".join(lines), True)

    del lines[0:]
    lines.extend(result.splitlines())


def _process_signatures(app, what, name, obj, options, signature, return_annotation):
    if what in ('apiproperty', 'apidata', 'apiattribute'):
        obj.annotation = _checks_modules_signatures(obj.annotation)
    return _checks_modules_signatures(signature), _checks_modules_signatures(return_annotation)




def _init(app):
    source = app.config.shortmd_modules
    cfg.modules = tuple(source) if source else ()


def setup(app):
    app.add_config_value("shortmd_modules", None, "env")

    _init(app)

    app.connect("autodoc-process-docstring", _process_docstrings)
    app.connect("autodoc-process-signature", _process_signatures)
