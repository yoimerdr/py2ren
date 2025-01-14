config
------

The config module provides the configuration management functionality:
Classes and functions to create, load and manipulate configuration settings.

.. multi-directive::
    :source: py2ren.config
    :directive: autoapiclass
    :items-options: members=True && show-inheritance=True
    :items: FileConfig, ModuleConfig, FileModule, Module, Init

.. multi-directive::
    :source: py2ren.config
    :directive: autoapifunction
    :items: create, load, dump, load_file, load_dict, dump_config


.. multi-directive::
    :source: py2ren.config
    :directive: autoapiexception
    :items: NonLoadableSourceConfigurationPath, NonLoadableConfigurationPath