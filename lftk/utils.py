from typing import Union, List

import ndjson
import pandas as pd

def get_feature_map(path):
    feature_df = convert_ndjson_to_pd(path).set_index('key')
    feature_map = feature_df.to_dict('index')
    return feature_map

def convert_ndjson_to_pd(path: str):
    with open(path, encoding='utf-8') as f:	
        data = ndjson.load(f)
        data = pd.DataFrame(data)
    return data

def get_pandas_row(
    dataframe: pd.core.frame.DataFrame, 
    column: str, 
    to_search: str,
    return_pandas: bool = False
    ) -> Union[List[dict], pd.core.frame.DataFrame]:
    mask = dataframe[column] == to_search
    if return_pandas == False:
        rows = dataframe[mask].to_dict('records')
    else:
        rows = dataframe[mask]
    return rows

def safe_division(n, d):
    return n / d if d else 0