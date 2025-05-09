#Zip File Search
from Sample1 import get_zip_files, search_in_zip
import os
import zipfile

# Search String
search_string = 'TXHD'
# Data Write to File
file = open("C://Users/18478/Desktop/CorrFile.txt", "w") 

directory_path = "C://Users/18478/Desktop/zipfiles" 
os.chdir(directory_path)
zip_files_list = get_zip_files(directory_path)

if zip_files_list:
  print("Zip files found:")
  for zip_file in zip_files_list:
    print(zip_file)
    zip_file_path = 'C://Users/18478/Desktop/zipfiles/'+zip_file
    results = search_in_zip(zip_file_path, search_string)
    if results:
        for filename, line_number, line in results:
            print(f"Found '{search_string}' in {filename}, line {line_number}: {line}")
            split_string_custom_delimiter = line.split("|")
            second_element_custom_delimiter = split_string_custom_delimiter[1]
            print(second_element_custom_delimiter)
            file.write(second_element_custom_delimiter) 
            file.write("\n") 
    else:
        print(f"'{search_string}' not found in {zip_file_path}")
else:
  print("No zip files found in the directory.")


"""
Close Open File
"""
file.close()