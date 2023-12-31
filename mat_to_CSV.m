% Prompt user for input and output file paths
inputFilePath = input('Enter the path to the input .mat file: ', 's');
outputFilePath = input('Enter the path to save the output CSV file: ', 's');

% Load the .mat file
try
    load(inputFilePath); % Load IMDb data from the specified .mat file
catch
    error('Error loading the input file. Please check the file path and format.');
end

% Calculate age for all entries
[age, ~] = datevec(datenum(imdb.photo_taken, 7, 1) - imdb.dob);

% Create a table for all entries
dataTable = table(imdb.name, imdb.gender, ...
    age, imdb.full_path, imdb.photo_taken, 'VariableNames', {'Name', 'Gender', 'Age', 'Full_Path', 'Photo_taken'});

% Write the table to a CSV file
try
    writetable(dataTable, outputFilePath, 'Delimiter', ',', 'WriteVariableNames', true);
    disp(['CSV file saved successfully at ' outputFilePath]);
catch
    error('Error writing CSV file. Please check the output file path.');
end
