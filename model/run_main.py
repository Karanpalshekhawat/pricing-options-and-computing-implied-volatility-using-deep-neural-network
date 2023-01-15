"""
This module is the main file which call all
other modules to import data, run neural
network model and generate parameters and then
create output file
"""
import pandas as pd

from model import *


def pre_processing(nmb):
    """
    This method creates the dataset that we will
    use for training and testing the NN model

    Args:
        nmb (int) : number of dataset to generate

    Returns:
        pd.DataFrame
    """
    df = read_input_variables_file()
    ticker = df['ticker'].iloc[0]
    st_current_price = get_current_price(ticker)
    range_of_inputs = create_set_of_input_parameters(nmb)
    option_df = create_dataset(df, st_current_price, range_of_inputs)

    return option_df


if __name__ == "__main__":
    num_dt_hyper = 100000
    dt_set_hyper = pre_processing(num_dt_hyper)  # small dataset for hyperparameter tuning
    running_hyperparameter_tuning = False
    if running_hyperparameter_tuning:
        hyperparameter_tuning(dt_set_hyper)
    file_name = r"./model/output/" + "best_hyper_parameter.pkl"
    df_hyper = pd.read_pickle(file_name)
