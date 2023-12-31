import pandas as pd


def gender_letter(df):
    print("Processing gender_letter.py...")

    # Map the values in the "Gender" column to 'M' and 'F'
    gender_mapping = {1: "M", 0: "F"}
    df["Gender"] = df["Gender"].map(gender_mapping)

    print("gender_letter.py processing complete.")
    return df
