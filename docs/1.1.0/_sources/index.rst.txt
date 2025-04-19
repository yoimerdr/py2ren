Welcome to py2ren's documentation!
==================================

**py2ren** is a tool that will allow you to transform python module into ren'py store module.

This transformation is done by taking the code and copying it
to .rpy files wrapped inside the expressions for a module stored
in ren'py like :renpy:`init python in module_name`

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   quickstart
   configuration

.. toctree::
    :maxdepth: 2
    :caption: Modules

    modules/config
    modules/helpers
    modules/converter/index
    modules/utils/index
    modules/cli

.. toctree::
    :maxdepth: 2
    :caption: Versions

    changelog
    versions-docs