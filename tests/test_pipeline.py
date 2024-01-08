import pytest 
import pandas as pd 
import numpy as np
from main import load_data, clean_data


@pytest.fixture #to set up a temporary CSV file 
def csv_file(tmp_path):
    data = pd.DataFrame({
    'YEAR' : [2022, 2023, 2010], 
    'MONTH' : ["Jan", "Feb", "March"], 
    'SUPPLIER': [np.nan, "Sup1", np.nan], 
    'ITEM CODE': [12, 13, 24],
    'ITEM DESCRIPTION': ["first", "second", "third"],
    'ITEM TYPE': ["Wine", "Liquor", np.nan], 
    'RETAIL SALES': [100, 130, np.nan],
    'RETAIL TRANSFERS': [0, 12, 0],
    'WAREHOUSE SALES': [0, 12, 0]
        }
    )

    file_path = tmp_path / "data.csv"
    data.to_csv(file_path, index=False)
    return file_path


def test_load_data(csv_file):
    data = load_data(csv_file)
    
    assert 'SUPPLIER' in data.columns
    assert 'ITEM CODE' in data.columns
    assert 'RETAIL SALES' in data.columns
    assert len(data) == 3



def test_clean_data(csv_file):
    data = load_data(csv_file)
    data = clean_data(data)
    
    assert data['SUPPLIER'].isna().sum() == 0
    assert data['RETAIL SALES'].isna().sum() == 0
    assert data['ITEM TYPE'].isna().sum() == 0
    assert data.loc[2, 'RETAIL SALES'] == -1
    assert len(data) == 3  