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

    If you'd like to read more about the project, keep scrolling down.
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

st.markdown('## My Crazy Rental Property as a College Student')
col1, col2 = st.columns([1,12])
with col2:
    st.markdown("""

                
    Since you're checking out my AutoCAD model of 204 E Oakland, I want you to read some notes on what I learned while making it.

    But first, I'm going to tell you how I got to making a floorplan for a house that has been around since the early 1900's .. making this house four times my age! - I'm 23 right now. 

    I began my undergraduate degree in mechanical engineering just over 5 years ago, In 2018. Going into university, I was recovering from the first of many surgeries in my years ahead. This surgery was to remove my Stapes, which left me deaf in one ear. 
    Unable to swim on doctors’ orders I found myself looking for something to fill my summer with. I began reading about financial investments - something I had taken a class on in high school. 

    After trudging through stocks bonds and alternative investments, I found myself interested in real-estate, but had no idea where to start. Left confused about how to enter real-estate investing, I invested into stocks. 

    Fast forward to my junior year at Ohio State. The world changing Covid-19 prevented college students from attending. It just so happened to be the most difficult year of my four-year university track. 

    My grades struggled, but like the summer before college, I found myself with more spare time between zoom lectures, which were notoriously more boring than normal lectures. So, I filled a small piece of each day browsing Zillow. For-sale listings were being posted and with each one I conducted a profitability analysis study.

    After some time, I found a property that was just a tad bit more brilliant than the rest, and so, without having any idea on how I would fund the project, I toured the property and made an offer. 
    It wasn’t easy deciding on how to fund the down payment – which seemed like an impossible task to an already broke college student. It wasn’t easy qualifying for the loan or conducting all the inspections necessary during the purchase process. But because the numbers were solid, I knew it had to be possible. 
                

    ### The challenges of owning a house

    The challenges continued. I had a rough first year and learned the most valuable lessons in real estate. More so than anything I read in a book or saw a guru talk about on Youtube. 
    The risk of owning a house was not often spoken about online. I found myself in a situation where a complete rehab was necessary. My first house, and rental property, slowly was destroyed by the first tenants I had move into the property. The red flags slipping past me, I was distracted by positive background checks, credit reports, and of course the pressure of the mortgage payment.

    There was a major lesson to be learned about what something looks like on paper. The cherry on top was that during this chaos, my surgeon, the same one that removed my stapes 4 years ago, ordered me to stay home for several months following my fifth surgery in January of 2022 – what seemed like the peak of house damages.

    Not only was I missing school my senior year, but I was losing valuable time away from properly managing 204 E Oakland.

    Finally, in the end of summer of 2022 the tenants who wrecked the place were gone. And In my mind, I had the next 6 months to fix the place. The light at the end of the tunnel was visible, but the hardship was not over.  I tried taking shortcuts and worked with people who ended up taking advantage of me. The rehab process took more than 12 months and cost much more than I anticipated.

    It's now August of 2023, I have 204 rented out to good people this year. Now, Id rather leave the place empty than rent it to people I am not confident in. The floorplan is not just part of documenting the current state of the house, but also to provide a better experience for future tenants – allowing them to decide if it’s the right place to tour, serving as a guide for furniture placement, and showcasing a little professionalism where it previously lacked. 
     
                
    ### What I learned when making the floorplans

    Anyways, let’s talk about what I learned when making this AutoCAD plan view of 204. 

    ##### First let’s talk about accuracy.

    The most effective way to model is to assume each room is a rectangle, but each room is imperfect in its age. With this, modeling older builds are trickier because measurements won’t add up on each side of the room. To mitigate the downsides of this, the best way is to group inaccuracies into the least important dimensions on the floor. Mainly, I focused on making the room shapes and dimensions a higher priority than the hallways.

    The second most important aspect in accuracy is wall thickness, I found it most effective to model the house with a constant wall thickness, even though this isn’t exactly true. The homes walls are plaster, which is thicker and thinner in certain areas. This also added error into the model, which again needed to be dispersed across different wall dimensions. 

    ##### Now let’s talk about clarity. 

    After receiving my bachelor’s in engineering, I had an advantage from 3D printing and drawing manufactured parts in the past. However, I had even more help from my best friend, Angela, she’s an architecture major - I can’t thank her enough for her input on this plan project and 204 in general. 

    The methodology behind drawing a floor plan starts off simply. Plan views are made by cutting the building at a certain height, usually 4 ft above the floorboards. Anything cut in the process shows up as a line. Anything below the cut line but being hidden is a dashed, hidden line. These show up in places where a wall is cut and beneath that cut line exists a doorframe or other walls that are important to show. This happens on floor 3 with the staircase and on floor 1 with the side door.

    ### Line thickness rules that I sometimes break
                
    Beyond mastering those basics, line thicknesses is the most important modification for clarity. Line thickness adds a feel of depth and hierarchical importance on a floorplan. It distinguishes exterior from interior more clearly than using a single line stroke thickness and it can even show differing materials such as windows and cabinetry. 

    In this model, I’ve used the following rules:
    1.	Exterior walls do not connect to interior walls and are drawn with 0.6,mm line thickeness, designated as Heavy
    2.	Interior walls are drawn as 0.3 mm designated medium
    3.	Lite line thickness of 0.25 is reserved for interior doors and windows. Windows are drawn not as one line but two. See the model.
    4.	Detailed additions like furniture and cabinetry are added in 0.09 mm line thickness, designated as Fine detail.
    5.	Layer Management. I’ve employed different layers and named them according to MIT's 2022 BIM and CAD drawing standards.

                
    ### Title Blocks
    The last thing Id like to leave in these notes are my thoughts on title blocks.
    I couldn’t find an easy template online that I liked, So I made my own with the important pieces of information: project issue (start) date, Revision number and date, Project Name, Author, and a designation for which direction is north. Ive placed this in the bottom left of of each drawing, which is designated by a double boarder, a standard in engineering drawing.

    Those are all the notes I have time to leave. I hope you’ve found my model and commentary useful in some way. 

    Brian

                
    """)

"---"

with st.expander("Creating this page"):
    st.write("""
    ## About this page
    A [Streamlit](https://streamlit.io/) demo written in [Pure Python]() hosted on [Github](https://github.com/BrianLesko) for displaying the floorplan drawings of my rental house - created in AutoCAD. 
             
    Topics used during creation:
             Python | Streamlit | PIL | Github | AutoCAD 
             session states | expander | columns | buttons | images | markdown

    Project Inspirations: 
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