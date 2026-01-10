import streamlit as st
import base64


# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="<Julio Jesus Ramirez> Portfolio",
    page_icon="📊",
)


def home_page():
    # ----- Left menu -----
    with st.sidebar:
        st.image("eae_img.png", width=200)
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("***Final Project - Dec 2025***")
        st.write("**Author:** <your name> ")
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


    # ----- Top title -----
    st.html("""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Julio Ramirez</h1></div>""")  # TODO: Add your name


    # ----- Profile image file -----
    profile_image_file_path = "juliopp.jpg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

    with open(profile_image_file_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


    # ----- Your Profile Image -----
    st.html(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="Julio Jesus Ramirez" width="300" height="300" style="border-radius: 70%; object-fit: cover; margin-top: 90px; margin-bottom: 40px;">
    </div>
    """)


    # ----- Personal title or short description -----
    current_role = "Student at EAE Business school doing a Master in Bid Data & Analytics"

    st.html(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""")

    st.write("##")    # Adding some space


    # ----- About me section -----
    st.subheader("About Me")

    # TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
    st.write("""
    - 🧑‍💻 I am a entrepenur with most of my experience in hospitality. I do house music events
             and I host guests in our very own Airbnb's in Punta Cana, Dominican Republic. 

    - 🛩️ prev: I did a Associate in Science in Digital Marketing and a BBA in Marketing Analytics. 

    - ❤️ < My passion is hospitality. However, I am very data driven business wise and I love the combination
             of operations and business withtin the data cyle.

    - 🤖 < My personal projects are Cana Corals Solutions which is a data driven company that will focus on 
             creating a SaaS long term for different businesses. Inclouding doctors, hospitality check ins, 
             events and financial. 

    - 🏂 <Your Hobbies are editing my own footage for all the marketing and padel. 
             

    - 📫 How to reach me: Jjesusr@student.eae.es

    - 🏠 I love Barcelona 
    """)

    # Feel free to add other points like your Linkedin, Github, Social Media, etc.

    # This is ensambling the entire app with the different pages and the navigation menu
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("pages/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("pages/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("pages/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])
pg.run()