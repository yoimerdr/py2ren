# py2ren
A tool to automate the transformation of native python module to ren'py store module.

## Requirements

Before you start, you need to download a py2ren [release](https://www.github.com/yoimerdr/py2ren/releases),
and have a python version 2.7 or later installed on your computer. Then unzip.

## Usage
### CLI usage
Located in the py2ren's parent folder, you can now use the command.

```shell
    python -m py2ren path [options]
```


Positional argument:

  - **path**: target transformation path.


Options:

  - **-o, --out**:                     the output folder for the transformation result.
  - **-n, --name**:                    the base module name, must not contain spaces.
  - **-il, --init-level**:             the init level for the init expression.
  - **-c, --config**:                  path to the configuration file.
  - **-nks, --no-keep-structure**:     flag to disable keeping the module structure.
  - **-fc, --force-config**:           flag to force the creation of the configuration file.
  - **-h, --help**:                    show the help message and exit



For example, if you have the following file:

```python
def say_hello(name: str):
    return "Hello, " + name + "."
```

And run the command

```shell
    python -m py2ren sample.py -n sample_module
```

After the conversion, you will get:

````python
init -1 python in sample_module:
    def say_hello(name: str):
        return "Hello, " + name + "."
````

> - py2ren does not remove type annotations, so if you want better compatibility with renpy projects, you should remove them.
> - if the  **out** parameter is specified, by default the parent path of the file, or the folder path itself, will be used.


### Module usage


You can also use py2ren as a python module; and continuing with the previous example, you can obtain the same result by doing the following.


````python
# this script is located in py2ren's parent folder
import py2ren

py2ren.convert("filename.py", ".", "sample_module")
````

    



