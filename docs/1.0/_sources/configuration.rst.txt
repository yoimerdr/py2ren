Configuration
=============

The py2ren tool uses a JSON configuration file named ``py2ren.config.json`` (by default)
to control how Python modules are converted to Ren'Py store modules.
This configuration is generated automatically, but can be modified.

This format is represented by the classes present in :doc:`modules/config`.

File configuration
------------------

The following is the configuration format:

.. code-block:: json

    {
        "name": "module_name",
        "initLevel": 0,
        "classBases": {
            "python_name": "renpy_name"
        },
        "storedModules": ["module", "name"],
    }



For example, if we want to convert the file ``sample.py`` we can use the following configuration:

.. code-block:: json

    {
        "name": "sample_file",
        "initLevel": 0,
        "classBases": {
            "object": "python_object",
            "list": "python_list",
            "tuple": "python_tuple",
            "dict": "python_dict"
        },
        "storedModules": [],
    }


This configuration:

* Names the store module "sample_file"
* Sets default init level to 0.
* Maps Python base classes to Ren'Py equivalents.
* It does not replace any module import with its renpy store representation.


Module configuration
--------------------

The following is the configuration format:

.. code-block:: json

    {
        "name": "module_name",
        "initLevel": 0,
        "classBases": {
            "python_name": "renpy_name"
        },
        "storedModules": ["module", "name"],
        "modules": {
            /*file config*/
            "file.py": {
                "initLevel": 0,
                "ignore": false,
                "name": "submodule_file",
                "classBases": {
                    "python_name": "renpy_name"
                }
            },
            /*module config*/
            "submodule": {
                "initLevel": 0,
                "ignore": false,
                "name": "submodule_folder",
                "classBases": {
                    "python_name": "renpy_name"
                }
            }
        }
    }



For example, if we want to convert the folder (module) ``sample`` we can use the following configuration:


.. code-block:: json

    {
        "name": "sample_folder",
        "initLevel": 0,
        "classBases": {
            "object": "python_object",
            "list": "python_list"
        },
        "storedModules": ["gallerynpy"],
        "modules": {
            "main.py": {},
            "utils": {
                "initLevel": -1,
                "modules": {
                    "__init__.py": {},
                    "helpers.py": {
                        "initLevel": -2
                    }
                }
            },
            "config": {
                "ignore": true
            }
        }
    }

This configuration:

* Names the store module "sample_folder".
* Sets default init level to 0.
* Maps Python base classes to Ren'Py equivalents.
* It replaces the module 'gallerynpy' import with its renpy store representation (i.e. from store import gallerynpy).
* Configures the module structure with:

   - A main.py file using default settings.
   - A utils package initializing at level -1.
   - A helpers.py module initializing at level -2.
   - A config directory that will be ignored.


.. note::

    * The only difference between file and module config is the ``modules`` section.
    * If a file or directory has no configuration, a default configuration will be used.
    * The default configuration will use the defined fields of the nearest parent if they are defined, otherwise the default ones will be used.
    * If a submodule is not present in “modules” it will be ignored.
    * If the configuration type is not compatible with the target file or directory, an exception will be thrown.
