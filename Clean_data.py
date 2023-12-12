import pandas as pd

def clean_lego_data(data):
    # Drop duplicates, if any
    data.drop_duplicates(inplace=True)
    
    # Drop rows with missing values
    for col in categorical_columns:
        data[col].dropna(inplace=True)
    
    # Convert 'year' column to datetime if it's in string format
    if isinstance(data['year'][0], str):
        data['year'] = pd.to_datetime(data['year'], errors='coerce').dt.year
    
    # Fill missing values in numerical columns with their respective means
    numerical_columns = ['Part category', 'Part name', 'Part material', 'Part URL', 'Set Price', 'Number of reviews', 'Star rating']
    for col in numerical_columns:
        data[col].fillna(data[col].mean(), inplace=True)

    
    # Fill missing values in categorical columns with a placeholder ('Unknown' or 'Missing')
    categorical_columns = ['Part color', 'RGB', 'Is Transparent?']
    for col in categorical_columns:
        data[col].fillna('Unknown', inplace=True)
    
    return data
