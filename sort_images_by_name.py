import os
import shutil
from tqdm import tqdm
import time


def sort_images_by_name(input_folder):
    print("Processing sort_images_by_name.py...")
    # Create a dictionary to store lists of image files for each name
    name_dict = {}

    # Count the total number of files for progress bar
    total_files = sum(
        1
        for _ in os.listdir(input_folder)
        if os.path.isfile(os.path.join(input_folder, _))
    )

    # Create a progress bar
    progress_bar = tqdm(
        total=total_files, desc="Sorting Images", unit="file", unit_scale=True
    )

    # Record the start time
    start_time = time.time()

    # Iterate through all files in the folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Check if the item is a file
        if os.path.isfile(file_path):
            # Extract the name from the file
            name = filename.split("_")[0]

            # Add the file to the corresponding name's list
            if name not in name_dict:
                name_dict[name] = []
            name_dict[name].append(file_path)

            # Update the progress bar
            progress_bar.update()

    # Record the end time
    end_time = time.time()

    # Close the progress bar
    progress_bar.close()

    # Calculate and display time elapsed
    time_elapsed = end_time - start_time
    print(f"Time Elapsed: {time_elapsed:.2f} seconds")

    # Create subfolders for each name and move images into respective subfolders
    for name, file_list in name_dict.items():
        subfolder_path = os.path.join(input_folder, name)

        # Create the subfolder if it doesn't exist
        os.makedirs(subfolder_path, exist_ok=True)

        # Move images into the subfolder
        for file_path in file_list:
            new_file_path = os.path.join(subfolder_path, os.path.basename(file_path))
            shutil.move(file_path, new_file_path)

    print("sort_images_by_name.py processing complete.")
