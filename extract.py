import os
import shutil

# Define the main folder path
main_folder = r"D:\Coding\Facial Recognition\Oulu CASIA NIR"

# Iterate over each person folder (P001 to P080)
for person_folder in os.listdir(main_folder):
    person_folder_path = os.path.join(main_folder, person_folder)
    
    # Iterate over each emotion folder inside the person folder
    for emotion_folder in os.listdir(person_folder_path):
        emotion_folder_path = os.path.join(person_folder_path, emotion_folder)
        
        # Iterate over each image file in the emotion folder
        for filename in os.listdir(emotion_folder_path):
            # Construct the new filename with emotion label
            new_filename = f"{emotion_folder}_{filename}"
            
            # Construct the paths for old and new files
            old_file_path = os.path.join(emotion_folder_path, filename)
            new_file_path = os.path.join(person_folder_path, new_filename)
            
            # Move the file and rename it
            shutil.move(old_file_path, new_file_path)
    
    # Remove the emotion folders
    shutil.rmtree(emotion_folder_path)
