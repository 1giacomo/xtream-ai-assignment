import pandas as pd

def clean_data(df):
    cleaned_df = df[
        (df['price'] > 0) &
        (df['x'] > 0) &
        (df['y'] > 0) &
        (df['z'] > 0) &
        (df['carat'] < 2.5)
    ]
    return cleaned_df

def linear_encoding(df):
    cut_mapping_dict = {
        "Ideal": 4,
        "Premium": 3,
        "Very Good": 2,
        "Good": 1,
        "Fair": 0,
    }

    clarity_mapping_dict = {
        "IF": 7,
        "VVS1": 6,
        "VVS2": 5,
        "VS1": 4,
        "VS2": 3,
        "SI1": 2,
        "SI2": 1,
        "I1": 0
    }

    df['cut'] = df['cut'].replace(cut_mapping_dict)
    df['color'] = df['color'].apply(lambda x: ord('Z') - ord(x))
    df['clarity'] = df['clarity'].replace(clarity_mapping_dict)

    return df

def drop_columns(df):
    return df.drop(['x', 'y', 'z', 'depth', 'table'], axis=1)

def hot_key_encoding(df):
    return pd.get_dummies(df, columns=['cut', 'color', 'clarity'])