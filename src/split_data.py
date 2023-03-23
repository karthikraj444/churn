import os
import yaml
import pandas as pd
import argparse
from pkgutil import get_data
from get_data import get_data,read_params
from sklearn.model_selection import train_test_split
# from sklearn import train_test_split

def split_and_save(config_path):
    config=read_params(config_path)
    test_data_path=config["split_data"]["test_path"]
    train_data_path=config["split_data"]["train_path"]
    raw_data_path =config["load_data"]["raw_dataset_csv"]
    split_ratio=config["split_data"]["test_size"]
    random_state=config["base"]["random_state"]
    df =pd.read_csv(raw_data_path,sep=",",encoding="utf-8")
    # print(df.head())
    train,test= train_test_split(df,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_data_path,sep=",",index=False,encoding="utf-8")
    test.to_csv(test_data_path,sep=",",index=False,encoding="utf-8")

    return split_and_save
