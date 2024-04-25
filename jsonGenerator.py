import os
import json

# The folder containing your images
image_folder = './images'

# The JSON file you want to create
json_file = 'gallery.json'

# List of image formats you want to include
image_formats = {'.jpg', '.jpeg', '.png', '.gif'}

# Generate the JSON data structure
gallery_data = []
for filename in os.listdir(image_folder):
    if os.path.splitext(filename)[1].lower() in image_formats:
        # Remove the file extension and split the filename
        title, description, tag = os.path.splitext(filename)[0].split('_')

        # Replace underscores in the title, description, and tag with spaces
        title = title.replace("THIS IS THE TITLE", " ").strip()
        description = description.replace("this is the description", " ").strip()
        tag = tag.replace("this is the tag", " ").strip()

        gallery_data.append({
            "src": f"images/{filename}",
            "title": title,
            "description": description,
            "format": filename.split('.')[-1].upper(),
            "tag": tag
        })

# Write the JSON structure to a file
with open(json_file, 'w') as outfile:
    json.dump(gallery_data, outfile, indent=4)
