import pandas as pd

# Set some pandas options
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)


class Dataset:
    def __init__(self):
        cols=["age","job","marital","education","default","balance","housing","loan","contact","day","month",
            "duration","campaign","pdays","previous","poutcome","y"]
        # Load from CSV
        self.data = pd.DataFrame(pd.read_csv('data/bank-full.csv', skip_blank_lines=True,
                                    usecols=cols, sep=';'))

    def get_data(self, data_slice):
        return self.data if data_slice[0]=='all' else self.data[data_slice]    

    