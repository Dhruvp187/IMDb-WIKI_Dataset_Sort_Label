import pandas as pd


def txt_to_csv(input_file_path):
    print("Processing txt_to_csv.py...")
    # Read the CSV file
    df = pd.read_csv(input_file_path)

    # Extract relevant columns for each person
    name_columns = [f"Name_{i}" for i in range(1, 460723)]
    gender_columns = [f"Gender_{i}" for i in range(1, 460723)]
    age_columns = [f"Age_{i}" for i in range(1, 460723)]
    photo_taken_columns = [f"Photo_taken_{i}" for i in range(1, 460723)]
    full_path_columns = [f"Full_Path_{i}" for i in range(1, 460723)]

    # Create a new DataFrame with rearranged columns
    new_df = pd.DataFrame(
        {
            "Name": df[name_columns].values.flatten(),
            "Gender": df[gender_columns].values.flatten(),
            "Age": df[age_columns].values.flatten(),
            "Year_of_Photo": df[photo_taken_columns].values.flatten(),
            "Full_File_Path": df[full_path_columns].values.flatten(),
        }
    )

    print("txt_to_csv.py processing complete.")
    return new_df
