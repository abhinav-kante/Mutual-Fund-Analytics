import pandas as pd
import os

folder = "data/raw/nav_data"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\n" + "=" * 50)
        print(file)
        print("=" * 50)

        print("Shape:", df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicates:")
        print(df.duplicated().sum())

        print("\nFirst 5 Rows:")
        print(df.head())