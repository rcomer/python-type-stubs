from __future__ import annotations
import numpy as np
from pandas.core.dtypes.generic import ABCIndex as ABCIndex
from typing import Optional, Tuple, Union

def unique(values): ...
unique1d = unique

def isin(comps, values) -> np.ndarray: ...
def factorize(values, sort: bool=..., na_sentinel: int=..., size_hint: Optional[int]=...) -> Tuple[np.ndarray, Union[np.ndarray, ABCIndex]]: ...
def value_counts(values, sort: bool=..., ascending: bool=..., normalize: bool=..., bins=..., dropna: bool=...) -> Series: ...
def duplicated(values, keep=...) -> np.ndarray: ...
def mode(values, dropna: bool=...) -> Series: ...
def rank(values, axis: int=..., method: str=..., na_option: str=..., ascending: bool=..., pct: bool=...) : ...
def checked_add_with_arr(arr, b, arr_mask = ..., b_mask = ...): ...
def quantile(x, q, interpolation_method: str = ...): ...

class SelectN:
    obj = ...
    n = ...
    keep = ...
    def __init__(self, obj, n: int, keep: str) -> None: ...
    def nlargest(self): ...
    def nsmallest(self): ...
    @staticmethod
    def is_valid_dtype_n_method(dtype) -> bool: ...

class SelectNSeries(SelectN):
    def compute(self, method): ...

class SelectNFrame(SelectN):
    columns = ...
    def __init__(self, obj, n: int, keep: str, columns) -> None: ...
    def compute(self, method): ...

def take(arr, indices, axis: int=..., allow_fill: bool=..., fill_value=...) : ...
def take_nd(arr, indexer, axis: int=..., out=..., fill_value=..., allow_fill: bool=...) : ...
take_1d = take_nd

def take_2d_multi(arr, indexer, fill_value = ...): ...
def searchsorted(arr, value, side: str = ..., sorter = ...): ...
def diff(arr, n: int, axis: int=..., stacklevel=...) : ...
def safe_sort(values, codes=..., na_sentinel: int=..., assume_unique: bool=..., verify: bool=...) -> Union[np.ndarray, Tuple[np.ndarray, np.ndarray]]: ...

from pandas import Series as Series
