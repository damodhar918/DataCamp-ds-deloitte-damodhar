import pandas as pd

import xml.etree.ElementTree as ET

import os
# set the main directory path
# http://vision.stanford.edu/aditya86/ImageNetDogs/
main_dir = "./Annotation"

# set the output file path
output_file_path = "./"

# initialize empty list and dictionary variables
data_list = []

# loop through each subdirectory in the main directory
for subdir in os.listdir(main_dir):
    subdir_path = os.path.join(main_dir, subdir)
    # skip any non-directory files
    if not os.path.isdir(subdir_path):
        continue
    # loop through each file in the subdirectory
    for file in os.listdir(subdir_path):
        file_path = os.path.join(subdir_path, file)
        # load file contents as a string
        with open(file_path, 'r') as f:
            data_list.append(f.read())



# create pandas DataFrame from the data_list and dog_list variables
df = pd.DataFrame({'folder': [], 'filename': [], 'width': [], 'height': [], 'dog_list': []})
for data in data_list:
    # parse the annotation file
    root = ET.fromstring(data)
    # extract the relevant information
    folder = root.find('folder').text
    filename = root.find('filename').text
    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)
    # extract information about all dogs in the image
    dog_list = []
    for obj in root.findall('object'):
        name = obj.find('name').text
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        dog = [name, xmin, ymin, xmax, ymax]
        dog_list.append(dog)
    # append the row to the DataFrame
    dog_list = [item for sublist in dog_list for item in sublist]
    df.loc[len(df)] = pd.Series({'folder': folder, 'filename': filename, 'width': width, 'height': height, 'dog_list': dog_list})



# write the DataFrame to a csv file
df.to_csv(output_file_path + 'dog_list.csv', index=False)
df.head()