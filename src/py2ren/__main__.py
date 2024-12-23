from __future__ import absolute_import

import os
import sys

if sys.path[0] in ('', os.getcwd()):
    sys.path.pop(0)

if __package__ == '':
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

if __name__ == "__main__":
    from .cli import main

    main()
