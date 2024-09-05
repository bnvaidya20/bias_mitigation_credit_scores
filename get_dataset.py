
import os
import urllib.request

from config import *


# Create the directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"Created directory: {data_dir}")

# Download the files if they don't exist
for file_name, url in data_files.items():
    file_path = os.path.join(data_dir, file_name)
    if not os.path.exists(file_path):
        print(f"Downloading {file_name} from {url}")
        urllib.request.urlretrieve(url, file_path)
        print(f"Saved {file_name} to {file_path}")
    else:
        print(f"{file_name} already exists at {file_path}")

print("All required files are in place.")