from pandas import DataFrame as DataFrame

def pivot_table(data, values=..., index=..., columns=..., aggfunc=..., fill_value=..., margins=..., dropna=..., margins_name=..., observed=...) -> DataFrame: ...
def pivot(data: DataFrame, index=..., columns=..., values=...) -> DataFrame: ...
def crosstab(index, columns, values=..., rownames=..., colnames=..., aggfunc=..., margins=..., margins_name: str=..., dropna: bool=..., normalize=...) -> DataFrame: ...
