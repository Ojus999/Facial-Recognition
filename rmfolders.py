import os
import shutil

# Define the main folder path
main_folder = r"D:\Coding\Facial Recognition\Oulu CASIA NIR"

for person_folder in os.listdir(main_folder):
    person_folder_path = os.path.join(main_folder, person_folder)
    for emo in os.listdir(person_folder_path):
        emotion_folder_path = os.path.join(person_folder_path,emo)
        if os.path.isdir(emotion_folder_path):
            shutil.rmtree(emotion_folder_path)
        elif emotion_folder_path[-2:] == 'db':
            os.remove(emotion_folder_path)