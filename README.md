# Eurostat Data Downloader
This script allows you to download data from Eurostat and save it to a CSV file. Below is a brief description of each part of the code:<br>
Description:<br>
download_and_save_data is a function that fetches data from Eurostat based on the dataset code (dataset_code) and saves it to a CSV file.<br>
eurostat.get_data_df(dataset_code) retrieves data from Eurostat in the form of a DataFrame.<br>
The CSV file name is generated based on the csv_filename parameter provided when the function is called.<br>
The data is saved to a CSV file, and the user receives a confirmation message<br>
