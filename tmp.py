import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score, f1_score
import traceback
from logging import getLogger, StreamHandler, FileHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
file_handler = FileHandler("./log/log.txt")
file_handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.addHandler(file_handler)
logger.setLevel(DEBUG)
logger.propagate = False


def count_lower_threshold(df_data, threshold):
    """!
    @brief
    @param df_data
    @param threshold
    """ 
    return np.sum(df_data<threshold)


def check_state(count, threshold_low, threshold_high):
    """!
    @brief
    @param
    """
    state = 0           # "Normal"
    if(threshold_high > count >= threshold_low):
        state = 1       # "Caution"
    if(count >= threshold_high):
        state = 2       # "Disturbed"
    return state


if __name__ == "__main__":
    # read_csv
    df_data = pd.read_csv("./data/test.csv")

    df_buffer = pd.DataFrame()
    df_tmp = pd.DataFrame([[1,2,3]], columns=["x", "y", "z"])
    df_buffer = pd.concat([df_buffer, df_tmp], ignore_index=True)

    df_predicted = df_data["predicted"]
    count_predicted = df_predicted.rolling(window=15, min_periods=1).apply(count_lower_threshold, args=[0])
    state_predicted = count_predicted.apply(check_state, args=[7, 12])

    df_label = df_data["label"]
    count_label = df_label.rolling(window=15, min_periods=1).apply(count_lower_threshold, args=[0])
    state_label = count_label.apply(check_state, args=[7, 12])

    recall = recall_score(state_label, state_predicted)
    precision = precision_score(state_label, state_predicted)
    accuracy = accuracy_score(state_label, state_predicted)

    confusion_matrix(state_label, state_predicted)
