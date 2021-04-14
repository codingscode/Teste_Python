# usar colab
import pandas as pd


conjunto_dados = {
    'produtos': ['playstation', 'kit parafusos', 'impressora', 'pendrive', 'caderno'],
    'preco': [1200, 37.50, 722.35, 24.5, 20]
}

mostrar1 = pd.DataFrame(conjunto_dados)
mostrar1  # imprimir

print('----------------------')
dir(pd)  # imprimir

""" 
 ['BooleanDtype', 'Categorical', 'CategoricalDtype', 'CategoricalIndex', 'DataFrame', 'DateOffset',
 'DatetimeIndex', 'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 'Float64Index', 'Grouper', 'HDFStore',
 'Index', 'IndexSlice', 'Int16Dtype', 'Int32Dtype', 'Int64Dtype', 'Int64Index', 'Int8Dtype', 'Interval', 
'IntervalDtype', 'IntervalIndex', 'MultiIndex', 'NA', 'NaT', 'NamedAgg', 'Period', 'PeriodDtype', 'PeriodIndex',
 'RangeIndex', 'Series', 'SparseDtype', 'StringDtype', 'Timedelta', 'TimedeltaIndex', 'Timestamp', 'UInt16Dtype',
 'UInt32Dtype', 'UInt64Dtype', 'UInt64Index', 'UInt8Dtype', '__builtins__', '__cached__', '__doc__', 
'__docformat__', '__file__', '__getattr__', '__git_version__', '__loader__', '__name__', '__package__', 
'__path__', '__spec__', '__version__', '_config', '_hashtable', '_is_numpy_dev', '_lib', '_libs', 
'_np_version_under1p16', '_np_version_under1p17', '_np_version_under1p18', '_testing', '_tslib', '_typing', 
'_version', 'api', 'array', 'arrays', 'bdate_range', 'compat', 'concat', 'core', 'crosstab', 'cut', 
'date_range', 'describe_option', 'errors', 'eval', 'factorize', 'get_dummies', 'get_option', 'infer_freq', 
'interval_range', 'io', 'isna', 'isnull', 'json_normalize', 'lreshape', 'melt', 'merge', 'merge_asof', 
'merge_ordered', 'notna', 'notnull', 'offsets', 'option_context', 'options', 'pandas', 'period_range', 
'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard', 'read_csv', 'read_excel', 'read_feather', 
'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_orc', 'read_parquet', 'read_pickle', 
'read_sas', 'read_spss', 'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata', 'read_table', 
'reset_option', 'set_eng_float_format', 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 
'to_datetime', 'to_numeric', 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts', 
'wide_to_long']

 """
pd.__version__  # imprimir

print('----------------------')

a = [1, 7, 2]

mostrar2 = pd.Series(a)

mostrar2  # imprimir
mostrar2[0]  # imprimir

print('----------------------')
mostrar3 = pd.Series(a, index = ['x', 'y', 'z'])
mostrar3  # imprimir
mostrar3['y']  # imprimir

print('----------------------')

calorias = {'dia1': 420, 'dia2': 380, 'dia3': 390}
mostrar4 = pd.Series(calorias)

mostrar4  # imprimir

print('----------------------')
mostrar5 = pd.Series(calorias, index = ['dia1', 'dia2'])
mostrar5  # imprimir

print('----------------------')
