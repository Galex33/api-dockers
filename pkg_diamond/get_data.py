import pandas as pd 

def read_data(reader, name_data, index=None, columns=None):
    name_data = reader(name_data)
    df = pd.DataFrame(name_data, index, columns)
    df = df[~df.duplicated()]
    return df

