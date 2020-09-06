# This python program can be used to read a utf-8 csv file and take user input
# to create a new csv file with specific columns taken from the original file

# Author: Jaffar Alzain <alzainja>

import pandas

fname = input('Enter a csv file name(e.g. Example.csv):')

try:
    open(fname)
except Exception:
    print('File cannot be found:', fname,
          '\nPython program and csv file must be in the same folder')
    exit()

csv_data = pandas.read_csv(fname, skip_blank_lines=True)
available_columns = list(csv_data.columns)
print('Here is a list of available columns:', available_columns)

columns = input('Enter comma seperated column names(case sensitive):')

try:
    column_list = columns.split(',')
    column_list = [x.strip(' ') for x in column_list]
    csv_data[column_list].isin(available_columns)
    new_list = []
    for n in column_list:
        new_list.append(n)
except Exception:
    print('Some of the entered columns are not in the available columns list\n'
          'or you did not enter comma seperated column names(case sensitive)')
    exit()

output = pandas.DataFrame(csv_data, columns=new_list)
output.to_csv('new_'+fname, index=False)
print('New file titled new_'+fname, 'has been created')

input('Press Enter to exit')
