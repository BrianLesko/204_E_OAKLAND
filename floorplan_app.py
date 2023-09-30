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

st.title("204 E OAKLAND DRAWINGS")
st.write('Brian Lesko, 9/28/2023')
'---'

##################################################################
# Image indexing
##################################################################

# List all files in the images directory
image_files = [f for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]
image_files = [img for img in image_files if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
total_images = len(image_files)
image_files.sort()

##################################################################
# Main Selection with Session State
##################################################################

# Use Streamlit's session state to maintain the selected_image_num across reruns
if 'selected_image_num' not in st.session_state:
    st.session_state.selected_image_num = 0

col0, col1, col2, col3 = st.columns([1, 3, 1, 1])

with col2:
    if image_files and st.button("< Prev"):
        st.session_state.selected_image_num = (st.session_state.selected_image_num - 1) % len(image_files)
        
with col3:
    if image_files and st.button("Next >"):
        st.session_state.selected_image_num = (st.session_state.selected_image_num + 1) % len(image_files)

with col1:
    if image_files:
        # display the floor name
        st.subheader(image_files[st.session_state.selected_image_num])
        #new_selection = st.selectbox("Select an image", list(enumerate(image_files)), format_func=lambda o: o[1], index=st.session_state.selected_image_num)
        #st.session_state.selected_image_num = new_selection[0]

##################################################################
# Main Image
##################################################################

'---'
placeholder_image = Image.open('placeholder.png')
placeholder = st.image(placeholder_image, use_column_width=True)
'---'

##################################################################
# Image Gallery
##################################################################

st.header("Image Gallery")

if image_files:
    # Create columns for image previews
    image_cols = st.columns(len(image_files))
    button_cols = st.columns(len(image_files))

    for idx, image_file in enumerate(image_files):
        image_path = os.path.join(IMAGE_DIR, image_file)
        thumbnail = Image.open(image_path)
        # Resize the image to create a thumbnail
        thumbnail.thumbnail((400, 400))

        # Display the thumbnail in its column
        image_cols[idx].image(thumbnail, caption=None)

        # Display the select button in its column
        if button_cols[idx].button(f"Select {image_file}"):
            st.session_state.selected_image_num = idx
            st.session_state.used_selectbox = True


    ##################################################################
    # Image Display
    ##################################################################

    if st.session_state.selected_image_num is not None:
        # Display the selected image in a larger size
        selected_image_path = os.path.join(IMAGE_DIR, image_files[st.session_state.selected_image_num])
        image = Image.open(selected_image_path)
        with placeholder:
            st.image(image, caption=os.path.basename(selected_image_path), use_column_width=True)
        '---'
else:
    st.write("No images found in the 'images' directory.")
    '---'

##################################################################
# About Me
##################################################################

st.write('  ') 
st.write('  ') 

col1, col2, = st.columns([1,5], gap="medium")

with col1:
    st.image('./dp.png')

with col2:
    st.write(""" 
    Hey it's Brian,
            
    Thanks for visting this page, I hope you enjoy it!
            
    Feel free to explore more about my journey and connect with me through Twitter, Github and Linkedin below.

    """)
         
##################################################################
# Brian Lesko
# Social Links
##################################################################


# make 10 columns 
col1, col2, col3, col4, col5, col6 = st.columns(6)


with col2:

    st.write('')
    st.write('')
    st.write('[Twitter](https://twitter.com/BrianJosephLeko)')

with col3:

    st.write('')
    st.write('')
    st.write('[LinkedIn](https://www.linkedin.com/in/brianlesko/)')

with col4:

    st.write('')
    st.write('')
    st.write('[Github](https://github.com/BrianLesko)') 

with col5:

    st.write('')
    st.write('')
    st.write('[Buy me a Coffee](https://www.buymeacoffee.com/brianlesko)')

# write, centered "Brian Lesko 9/19/2023"

"---"

with st.expander("About this page"):
    st.write("""
    ## About this page
    A [Streamlit](https://streamlit.io/) demo written in [Pure Python]() hosted on [Github](https://github.com/BrianLesko) for displaying the floorplan drawings of my rental house - created in AutoCAD. 
             
    Topics used during creation:
             Python | Streamlit | PIL | Github | AutoCAD 
             session states | expander | columns | buttons | images | markdown

    Priject Inspirations: 
             Architecture | Design | Drawing | Floorplan | House | Rental 
             Rental Property | Real Estate | Investment Property | Investment

    Other project topics:
            Robotics Engineer | Mechanica | Mechanical Engineering | Software engineer

    ### Run this demo locally
    ```
    pip install --upgrade streamlit
    streamlit run https://github.com/BrianLesko/Robotics/blob/main/demo-FWRD-DYNM-2R/FWRD-DYNM-2R.py
    ```
             
    """)