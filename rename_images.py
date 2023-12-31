import os


def rename_images(dataset_folder, df):
    print("Processing rename_images.py...")

    # Dictionary to store the running number for each name
    name_counter = {}

    # Iterate over rows in the DataFrame and rename images
    for index, row in df.iterrows():
        name = row["Name"]
        gender = row["Gender"]
        age = str(int(row["Age"]))  # Assuming age is a whole number

        # Get the file extension (assumed to be '.jpg')
        file_extension = os.path.splitext(row["Full_File_Path"])[1]

        # Increment the running number for the current name
        name_counter[name] = name_counter.get(name, 0) + 1
        running_number = str(name_counter[name]).zfill(2)

        # Create the new file name
        new_name = f"{name}_{running_number}_{gender}_{age}{file_extension}"

        # Construct the old path by appending "dataset folder name" to "Full_File_Path"
        old_path = os.path.join(dataset_folder, row["Full_File_Path"])

        # Create the new file path
        new_path = os.path.join(dataset_folder, new_name)

        # Rename the image file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

        # Update the DataFrame with the new file path
        df.at[index, "New_File_Path"] = new_path

    print("rename_images.py processing complete.")
