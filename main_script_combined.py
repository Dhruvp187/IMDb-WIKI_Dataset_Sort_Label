from txt_to_csv import txt_to_csv
from gender_letter import gender_letter
from rename_images import rename_images
from sort_images_by_name import sort_images_by_name


def main_data_processing():
    # Process the first code
    first_code_input = r"D:/Github/DatasetLabeling/imdb.txt"
    first_df = txt_to_csv(first_code_input)

    # Process the second code using the output of the first code as input
    updated_df = gender_letter(first_df)

    # Save the updated DataFrame to a new CSV file
    second_code_output = r"D:/Github/DatasetLabeling/CSV_File.csv"
    updated_df.to_csv(second_code_output, index=False)
    print(f"Updated DataFrame saved to: {second_code_output}")

    # Rename images in the dataset folder
    dataset_folder = (
        r"D:/Github/DatasetLabeling/imdb_crop"  # Replace with the actual path
    )
    rename_images(dataset_folder, updated_df)

    # Save the final DataFrame to a new CSV file with updated file paths
    final_output_file = r"D:/Github/DatasetLabeling/Final_CSV_File.csv"
    updated_df[["Name", "Gender", "Age", "New_File_Path"]].to_csv(
        final_output_file, index=False
    )
    print(f"Final DataFrame with updated file paths saved to: {final_output_file}")


def main_image_processing():
    # Replace 'input_folder' with the path to your folder containing images
    input_folder = r"D:/Github/DatasetLabeling/imdb_crop"
    sort_images_by_name(input_folder)


if __name__ == "__main__":
    print("Processing main_script_combined.py...")

    # Run data processing
    main_data_processing()

    # Run image processing
    main_image_processing()

    print("main_script_combined.py processing complete.")
