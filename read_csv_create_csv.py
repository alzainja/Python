# This python program can be used to read a utf-8 csv file and take user input
# to create a new csv file with specific columns taken from the original file

# Author: Jaffar Alzain <alzainja>

import pandas as pd
import os

def file_exists(file_name):
    return os.path.isfile(file_name)

def get_available_columns(dataframe):
    return list(dataframe.columns)

def main():
    file_name = input('Enter a csv file name(e.g. Example.csv): ')

    if not file_exists(file_name):
        print('File cannot be found:', file_name,
              '\nPython program and csv file must be in the same folder')
        exit()

    csv_data = pd.read_csv(file_name, skip_blank_lines=True)
    available_columns = get_available_columns(csv_data)
    print('Here is a list of available columns:', available_columns)

    columns = input('Enter comma separated column names (case sensitive): ')

    column_list = [col.strip() for col in columns.split(',')]

    if not all(col in available_columns for col in column_list):
        print('Some of the entered columns are not in the available columns list\n'
              'or you did not enter comma separated column names (case sensitive)')
        exit()

    output = pd.DataFrame(csv_data, columns=column_list)
    new_file_name = os.path.join('new_' + file_name)
    output.to_csv(new_file_name, index=False)
    print('New file titled', new_file_name, 'has been created')

    input('Press Enter to exit')

if __name__ == "__main__":
    main()
