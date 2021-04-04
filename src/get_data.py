#read parameter
#read data file from source and return

import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    #read yaml file
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):

    #get data source path
    config = read_params(config_path)
    data_path = config["data_source"]["source"]
    
    #read data
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    return df
