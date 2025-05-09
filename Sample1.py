import os
import io
import zipfile

def search_in_zip(zip_file_path, search_string):
    """
    Searches for a string within the contents of a zip file.

    Args:
        zip_file_path (str): The path to the zip file.
        search_string (str): The string to search for.
    """
    results = []
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as z:
            for filename in z.namelist():
                try:
                    with z.open(filename) as f:
                        content = f.read().decode('utf-8')
                        lines = content.splitlines()
                        for i, line in enumerate(lines):
                            if search_string in line:
                                results.append((filename, i + 1, line))
                except UnicodeDecodeError:
                    pass  # Ignore files that can't be decoded as UTF-8
    except FileNotFoundError:
        print(f"Error: Zip file not found at {zip_file_path}")
        return None
    return results

def get_zip_files(directory):
  """
  Returns a list of all zip files in the given directory.
  """
  zip_files = []
  for filename in os.listdir(directory):
    if filename.endswith(".zip") and zipfile.is_zipfile(filename):
      zip_files.append(filename)
  return zip_files