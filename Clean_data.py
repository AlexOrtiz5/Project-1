import pandas as pd
def clean_columns_name(Lego_df):
   
    # Cleans the name of the columns
    Lego_df.columns = Lego_df.columns.str.lower().str.replace(' ','_')
    return Lego_df

def clean_lego_data(Lego_df):
    # Drop duplicates, if any
    Lego_df.drop_duplicates(inplace=True)
   
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
    
   
    # Drop rows with missing 'Set Price' values
    Lego_df.dropna(subset=['set_price'], inplace=True)

    return Lego_df

# Function to check for symbols in theme_name
def check_collaboration(theme):
    if isinstance(theme, str) and ('™' in theme or '®' in theme):
        return 'Collaboration'
    else:
        return 'Regular Theme'
