'''
This program can autonomously generate an overview EDA (Exploratory Data Analysis) report for any dataset.
'''

import os
import pandas as pd
import traceback
from pandas_profiling import ProfileReport

def get_input_file():
    '''
        This fuction will get the file path from user.
    '''
    file_path = ""
    while True:
        file_path = input("Enter the file path to the dataset: ")
        if file_path == "":
            print("This is a required info. Please enter again.")
            continue
        elif os.path.isfile(file_path):
            break
        else:
            print("Wrong file path or file is not exist. Please enter again.")
            continue
    return file_path

def gen_report_eda(path_df, path_output, title):
    '''
        This fuction will read the data and auto general a EDA report about the dataset.
        Parameter:
            path_df: the data source file path.
            path_output: the output path of the report (*html file).
            title: the title of the report.
    '''
    output_path = os.path.join(path_output, "_".join(title.lower().split()))
    df = pd.read_csv(path_df)
    profile = ProfileReport(df, title=title)
    profile.to_file(output_path)
    return output_path

if __name__ == "__main__":
    print("===== Autonomous EDA (Exploratory Data Analysis) Report =====")
    path_df = get_input_file()
    title = input("Enter the title of the report (leave blank for default): ")
    title = title if title != "" else "Autonomous EDA Report"
    path_output = input("Enter the report output path (leave blank for default): ")
    path_output = path_output if path_output != "" else "./"
    try:
        output_path = gen_report_eda(path_df, path_output, title)
        print("All work is done! Check your output at:" + output_path)
        print("===== Finish =====")
    except Exception as e:
        print("Error! Something went wrong! Please check again!")
        print("Error details: " + str(e))
        print("===== Finish =====")