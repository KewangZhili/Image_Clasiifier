import os
import shutil

source_folder = r"/Users/koushikmukka/Documents/real_and_ai_images/ai-generated-images"
destination_folder = r"/Users/koushikmukka/Downloads/archive/train/FAKE"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder +"/"+ file_name
    destination = destination_folder +"/"+ file_name
    # move only files
    shutil.move(source, destination)
    print('Moved:', file_name)

source_folder = r"/Users/koushikmukka/Documents/real_and_ai_images/real-images"
destination_folder = r"/Users/koushikmukka/Downloads/archive/train/REAL"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder +"/" +file_name
    destination = destination_folder +"/" +file_name
    # move only files
    shutil.move(source, destination)
    print('Moved:', file_na
