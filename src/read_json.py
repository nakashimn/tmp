from abc import abstractmethod
import os
import sys
import argparse
import glob
import datetime
import json
from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import traceback
from logging import getLogger, NullHandler, StreamHandler, FileHandler, DEBUG
logger = getLogger(__name__)
handler = NullHandler()
logger.addHandler(handler)
logger.propagate = False

class JsonReader:
    '''!
    @brief 複数のjsonファイルを読み込んでデータフレームに変換するクラス
    '''
    def __init__(
        self,
        filepaths,
        cls_logger=None
    ):
        '''!
        @brief コンストラクタ
        @param filepaths jsonファイルパスのリスト
        @param cls_logger ロガー(=None)
        '''
        self.logger = cls_logger or logger
        self.filepaths = filepaths
        self.data = self._convert_json_to_dataframe()

    def _convert_json_to_dataframe(self):
        '''!
        @brief 複数のjsonファイルを一つのデータフレームに変換する
        '''
        list_df_data = []
        for filepath in self.filepaths:
            df_data_part = self._tabularize_json(filepath)
            list_df_data.append(df_data_part)
        df_data = pd.concat(list_df_data).reset_index(drop=True)
        return df_data

    def _tabularize_json(
        self,
        filepath : str
    ):
        '''!
        @brief jsonファイルのデータをテーブル化する
        @param filepath jsonファイルのパス
        '''
        data = self._read_json(filepath)
        list_dict_data = self._unfold_data(data, filepath)
        df_data_part = pd.DataFrame(list_dict_data)
        return df_data_part

    def _read_json(
        self,
        filepath : str
    ):
        '''!
        @brief jsonファイルを読み込む
        @param filepath jsonファイルのパス
        '''
        with open(filepath, "r") as f:
            data = json.load(f)
        return data

    def _unfold_data(
        self,
        data : dict,
        filepath : str
    ):
        '''!
        @brief dataの選定とネスト解消を行う
        @param data 読み込んだjsonデータ
        @param filepath jsonファイルのパス
        '''
        list_dict_data = []
        dict_data = {"filepath": filepath}
        list_dict_data.append(dict_data)
        return list_dict_data
