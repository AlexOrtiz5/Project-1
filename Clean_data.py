import pandas as pd

def clean_columns_name(data):
    # Cleans the name of the columns
    data.columns = data.columns.str.lower().str.replace(' ','_')
    return data

def clean_lego_data(data):
    # Drop duplicates, if any
    data.drop_duplicates(inplace=True)
    
    # Convert 'year' column to datetime if it's in string format
    if isinstance(data['year'][0], str):
        data['year'] = pd.to_datetime(data['year'], errors='coerce').dt.year
    
    # Fill missing values in 'Star rating' and 'Number of reviews' with 0
    data['star_rating'].fillna(0, inplace=True)
    data['number_of_reviews'].fillna(0, inplace=True)
    
    # Remove commas and convert columns to numeric types
    data['set_price'] = data['set_price'].round(2)
    
    # Drop rows with missing 'Set Price' values
    data.dropna(subset=['set_price'], inplace=True)
    
    return data

# Function to check for symbols in theme_name
def check_collaboration(theme):
    if isinstance(theme, str) and ('™' in theme or '®' in theme):
        return 'Collaboration'
    else:
        return 'Regular Theme'