from typing import Iterable, Type

from . import filepath, iter
from typing import TypeVar, Iterable, Callable, Generator

_T = TypeVar("_T")
_R = TypeVar("_R")


def rowchars(text: str, char: str, start: int = 0) -> int: pass


def strip_indexes(source: Iterable, indexes: Iterable[int]): pass


def trymap(func: Callable[[_T], _R], value: _T, default: _R = None, allow: Iterable[Type[Exception]] = None): pass
