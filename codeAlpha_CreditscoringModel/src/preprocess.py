import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.fillna(df.median(), inplace=True)
    X = df.drop("SeriousDlqin2yrs", axis=1)
    y = df["SeriousDlqin2yrs"]
    return X, y

def scale_features(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)

def prepare_data(path):
    X, y = load_and_clean_data(path)
    X_scaled = scale_features(X)
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)
