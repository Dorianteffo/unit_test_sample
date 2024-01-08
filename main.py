import pandas as pd 

# Function to load the CSV
def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

# Function to clean the data
def clean_data(data):
    data['SUPPLIER'] = data['SUPPLIER'].fillna("NO SUPPLIER")
    data['ITEM TYPE'] = data['ITEM TYPE'].fillna("NO ITEM TYPE")
    data['RETAIL SALES'] = data['RETAIL SALES'].fillna(-1)
    return data


if __name__ == '__main__' : 
    df = load_data('dataset/Warehouse_and_Retail_Sales.csv')
    clean_df = clean_data(df)

