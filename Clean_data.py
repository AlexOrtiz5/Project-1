import pandas as pd

# Function to change the names of the columns
def clean_columns_name(data):
    # Cleans the name of the columns
    data.columns = data.columns.str.lower().str.replace(' ','_')
    return data

# Function to clean the data on the first csv
def clean_lego_data(data):
    # Drop duplicates, if any
    data.drop_duplicates(inplace=True)

    # Convert 'year' column to datetime if it's in string format
    if isinstance(Lego_df['year'][0], str):
        Lego_df['year'] = pd.to_datetime(Lego_df['year'], errors='coerce').dt.year

    # Fill missing values in 'Star rating' and 'Number of reviews' with 0
    Lego_df['star_rating'].fillna(0, inplace=True)
    Lego_df['number_of_reviews'].fillna(0, inplace=True)

    # Remove commas and convert columns to numeric types
    Lego_df['Set Price'] = Lego_df['set_price'].round(2)
    #Lego_df['number_of_reviews'] = pd.to_numeric(Lego_df['number_of_reviews'], errors='coerce')
    #Lego_df['star_rating'] = Lego_df['star_rating'].str.replace(',', '.', regex=True).astype(float)

    # Fill missing values in 'Star rating' and 'Number of reviews' with 0
    data['star_rating'].fillna(0, inplace=True)
    data['number_of_reviews'].fillna(0, inplace=True)

    # Remove commas and convert columns to numeric types
    data['set_price'] = data['set_price'].round(2)

    # Drop rows with missing 'Set Price' values
    data.dropna(subset=['set_price'], inplace=True)

    return data

# Function to clean the data on the second csv
def clean_lego_set(data):
    data.drop_duplicates(inplace=True)
    data.dropna(inplace=True)
    return data

# Function to check for symbols in theme_name
def check_collaboration(theme):
    if isinstance(theme, str) and ('™' in theme or '®' in theme):
        return 'Collaboration'
    else:
        return 'Regular Theme'
