import os
import shutil

# Define the source directory where you have subdirectories with PNG files
source_directory = './'

# Define the target directory where you want to copy the PNG files
target_directory = './images/'

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Walk through the source directory and its subdirectories
for root, _, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.png'):
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_directory, file)
            
            # Copy the PNG file to the target directory
            try:
                shutil.copy2(source_path, target_path)
            except:
                print ("An Exception has been thrown, but we do not care too much")
            
            print(f'Copied: {source_path} to {target_path}')

print('Copy process completed.')
