import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def clean_logistics_data(df):
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.replace("","_")
    )

"""df = df.drop_duplicates()
#df = df.fillna(0)

#return df """

