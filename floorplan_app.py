##################################################################
# Brian Lesko 
# 9/26/2023
# Drawing Study: displaying the floorplan of the house using streamlit
##################################################################

import streamlit as st
from PIL import Image
import os

# Path to the images directory
IMAGE_DIR = "png"

##################################################################
# Title
##################################################################

st.title("Floorplan App WIP")
st.write('By Brian Lesko, 9/28/2023')

'---'
placeholder = st.empty()
'---'

##################################################################
# Image Selection
##################################################################

# List all files in the images directory
image_files = [f for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]
image_files = [img for img in image_files if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

selected_image = None

# Check if image_files is not empty
if image_files:
    # Create columns for image previews
    image_cols = st.columns(len(image_files))
    button_cols = st.columns(len(image_files))

    for idx, image_file in enumerate(image_files):
        image_path = os.path.join(IMAGE_DIR, image_file)
        thumbnail = Image.open(image_path)
        # Resize the image to create a thumbnail
        thumbnail.thumbnail((100, 100))

        # Display the thumbnail in its column
        image_cols[idx].image(thumbnail, caption=image_file)

        # Display the select button in its column
        if button_cols[idx].button(f"Select {image_file}"):
            selected_image = image_path

    ##################################################################
    # Image Display
    ##################################################################

    if selected_image:
        # Display the selected image in a larger size
        image = Image.open(selected_image)
        with placeholder:
            st.image(image, caption=os.path.basename(selected_image), use_column_width=True)
        '---'
else:
    st.write("No images found in the 'images' directory.")
    '---'
