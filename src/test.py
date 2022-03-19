import os
import sys
import glob
import datetime
import json
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import traceback
from logging import getLogger, StreamHandler, FileHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.setLevel(DEBUG)
logger.propagate = False

def get_timestamp() -> str:
    '''!
    @brief タイムスタンプ取得メソッド
    @return タイムスタンプ(str)
    '''
    timestamp = datetime.datetime.strftime(
        datetime.datetime.now(), "%Y/%m/%d %H:%M:%S")
    return f"[{timestamp}] {os.path.basename(__file__)}"

def read_config(
    filepath: str
) -> dict:
    '''!
    @brief コンフィグ読込メソッド
    @param filepath コンフィグファイル名.json
    '''
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    except:
        logger.warning(traceback.format_exc())
        return None


if __name__=="__main__":

    # Logger
    file_handler = FileHandler("./log/log.txt")
    file_handler.setLevel(DEBUG)
    logger.addHandler(file_handler)
    logger.debug(get_timestamp())

    #
    filepath = "D:/nakashimn/Docker_environments/py36_pytorch/data/input/csv/input.csv"
    df_data = pd.read_csv(filepath)

    for idx, df_datum in df_data.iloc[:100].iterrows():
        # logger.debug(f"features : {df_datum[:-1]}")
        # logger.debug(f"label : {df_datum[-1]}")
        ans = 1*df_datum[0]+4*df_datum[1]-1*df_datum[2]
        error = ans - df_datum[-1]
        logger.debug(f"error : {error}")

    pca = PCA()
    pca.fit(df_data)
    feature = pca.transform(df_data)
    ev_ratio = pca.explained_variance_ratio_
    ev_ratio.cumsum()
