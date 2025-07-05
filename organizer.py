import os
import shutil

folder_path = "C:/Users/YourName/Downloads"  # Change to your actual folder path

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        ext = file.split('.')[-1].upper()
        new_folder = os.path.join(folder_path, ext)

        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        shutil.move(file_path, os.path.join(new_folder, file))

print("✅ Files organized successfully!")
