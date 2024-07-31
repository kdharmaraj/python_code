import os
def search_text_in_specific_files(drive_path, file_name, search_text):
    search_text_lower = search_text.lower()

    try:
        # Iterate over all directories in the specified drive
        for root, dirs, files in os.walk(drive_path):
            if file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        # Read file line by line
                        for line_number, line in enumerate(file, start=1):
                            if search_text_lower in line.lower():
                                print(f"{search_text} found in {file_path} on line {line_number}: {line.strip()}")
                except FileNotFoundError:
                    print(f"The file {file_path} does not exist.")
                except Exception as e:
                    print(f"An error occurred while reading {file_path}: {e}")
    except Exception as e:
        print(f"An error occurred while accessing the drive {drive_path}: {e}")


# Usage
drive_path = 'E:\\cts_work\\search_text'  # e.g., 'C:\\' for Windows or '/' for Unix-based systems
file_name = 'sample.txt'
search_text = 'error'
search_text_in_specific_files(drive_path, file_name, search_text)
