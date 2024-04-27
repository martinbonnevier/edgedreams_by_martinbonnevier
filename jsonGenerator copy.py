import os
import json

# The directory containing your images
image_directory = './images/random'

# The name of the JSON file you want to generate
json_filename = 'images.json'

# Generate a list of image file paths
image_files = [
    os.path.join('https://www.martinbonnevier.de/images/random/', filename)
    # os.path.join('./images/random/', filename)
    for filename in os.listdir(image_directory)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
]

# Create a dictionary to hold your image data
image_data = {'images': image_files}
print(image_data)
# Write the image data to a JSON file
with open(json_filename, 'w') as json_file:
    json.dump(image_data, json_file, indent=4)
