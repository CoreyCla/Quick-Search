import csv
import pandas as pd


class Csvi:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file

    def get_header(self):
        with open(self.csv_file, 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            return reader.fieldnames

    # Returns data from .csv file formatted with the first column values as the keys, and the rest of the row divided up
    # into another dictionary where the keys are the column names and the values are the corresponding row values.
    def get_rows_dict(self):
        reader = csv.DictReader(open(self.csv_file))
        result = {}

        for row in reader:
            key = row.pop(self.get_header()[0])
            result[key] = row
        return result

    # Returns data from .csv file formatted with the first column values as the key, and the rest of the row divided up
    # into list values.
    def get_rows_list(self):
        reader = csv.reader(open(self.csv_file))
        inner_dict = {}

        for row in reader:
            key = row[0]
            inner_dict[key] = row[1:]

        return inner_dict

    # Returns data from .csv file formatted with the header values as the keys, and a list of the respective column
    # data as the values.
    def get_cols(self):
        reader = csv.DictReader(open(self.csv_file))
        inner_dict = {}

        for row in reader:
            for column, value in row.items():
                inner_dict.setdefault(column, []).append(value)

        return inner_dict

    # Returns data from .csv file as a dictionary formatted with the header values (only the ones in the col_values
    # list) as the keys, and a list of the respective column data as the values. Needs refactoring to remove the mess
    # of a nested for-loop.
    def get_cols_by_name(self, col_names: list):
        reader = csv.DictReader(open(self.csv_file))

        inner_dict = {}
        for row in reader:
            for column, value in row.items():
                if column in col_names:
                    inner_dict.setdefault(column, []).append(value)

        return inner_dict

    # Returns an empty panda data frame with the same headers as the current .csv file
    def get_empty_df(self):
        new_df = pd.DataFrame(columns=self.get_header())
        return new_df

    ########## TO-DO ##########
    # - Add write capabilities so that the object can be given a dictionary that gets exported to .csv
    # - Skip csv's integrated write method because it takes forever. Instead put all new lines in one
    #   single string and write to file.
    # - Error/exception handling
    # - Pygtrie module from google (benchmark against it)


