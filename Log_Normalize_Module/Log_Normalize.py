from cmapPy.pandasGEXpress.parse_gct import parse
from cmapPy.pandasGEXpress.write_gct import write
import pandas as pd
import numpy as np
import argparse

def read_GCT(file):
    gct = parse(file)
    df = gct.data_df
    return df

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename",
                    type=str,
                    help="Name of the file to be read")
args = parser.parse_args()
data = read_GCT(args.filename)

data[data <= 0] = 0
log_data = np.log(data)
log_data_swapped = log_data.transpose()
log_data_swapped.to_csv("output.gct")
