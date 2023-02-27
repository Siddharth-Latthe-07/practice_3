import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Resume", page_icon=":tada:", layout="wide")

# loading the animation to the web page using request and streamlit_lottie modules
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
#def local_css(file_name):
 #   with open(file_name) as f:
  #      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")
lottie_code = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")
lottie_c = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_1pxqjqps.json")
lottie_z=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_DMgKk1.json")
img_contact_form = Image.open("venv/images/2023-01-17 (1).png")
img_lottie_animation = Image.open("venv/images/2023-01-17.png")
img_1=Image.open("venv/images/2023-01-19.png")
img_2=Image.open("venv/images\Screenshot 2023-01-19 142107.png")
img_3=Image.open("venv/images\download .png")
img_4=Image.open("venv/images\Screenshot_20230118_185256.jpg")
img_5=Image.open("venv/images\photo_3.png")


# ---- HEADER SECTION ----
with st.container():
    image_column, text_column = st.columns((1, 5))
    left_column, right_column = st.columns(2)


    with image_column:
        st.image(img_4)



    st.subheader("Hi, I am Siddharth :wave:")
    st.title("A Budding Explorer :mag:")
    st.write(
        "A very Passionate, Motivated, Keen Learner, Problem Solver & hard worker who always looks for opportunities to grow and excel"
    )
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education")
        st.write("##")
        st.write(
            """
            :school: 10th- St. Xavier's Hig School Kolhapur, 92.40%
            """
        )
        st.write(
            """
            :school_satchel: 12th- Chh. Shahu Vidyalaya Kolhapur, 82% 
            """
        )
        st.write(
            """
            :mortar_board: 3rd Year (E&TC) at VIIT, Pune (CGPA- 9.61)
            """
        )
        with right_column:
            st_lottie(lottie_z, height=300, key="education")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Meeting the technically ME!!!")
        st.write("##")
        st.write(
            """
            :pushpin: I am a budding ML & DS enthusiast.""")
        st.write(
            """
            :pushpin: Networking Domain & IoT stuffs also fascinates me""")
        st.write(
            """
            :pushpin: Good hands on Python, C/C++, Java""")
        st.write(
            """
            :pushpin: Python Web Development using Streamlit and Open CV always entertains me""")

            


        st.write("[Linkedin>](www.linkedin.com/in/siddharth-latthe-4ab69a213)")
        st.header("Meeting the Non-technical ME!!!")
        st.write("##")
        st.write(
            """
            :pushpin: Good at leadership skills""")
        st.write(
            """
            :pushpin: Descent at communication Skill""")
        st.write(
            """
            :pushpin: At leisure, prefer reading & watching Biopics and wildlife Documentaries
            """
        )
        st.write(
            """
            :pushpin: Sustain to have Multi-Tasking Capability
            """
        )
        st.write(
            """
            :pushpin: Descent percentage of Time Management
            """
        )
        


    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    with right_column:
        st_lottie(lottie_code,height=300,key="data science")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_1)
    with text_column:
        st.subheader("IoT based Home Automation")
        st.write(
            """
            Learnt how to interface various sensors with arduino board using arduino programming.
            
            Built a circuit design which can automate the room right from opening and closing of the door
            to switching on & off the lights and fans.
            
            In this project, I have used various sensors like temperature,PIR,light,servo motor etc
            """
        )
        st.markdown("[Project Link](https://www.tinkercad.com/things/1EuVD3aTIDn-homeautomation2)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.subheader("Movie Recommendation System")
        st.write(
            """
            This project mainly focuses on giving the user a proper and accurate recommendation of the respective search that he/she does.
            In this project, we have taken a dataset from tmdb that contains over 5000 movies with detailed description.
            By applying various data analytics processes and by using python modules of Streamlit,pickle we have made a web interface for the same
            """
        )
        st.markdown("[Project Link](https://github.com/Siddharth-Latthe-07/Movie-Recommended-System)")
with st.container():
    image_column, text_column = st.columns((1, 2))

    with text_column:
        st.subheader("Personal Voice Assistant")
        st.write(
            """
            In this project,I have used python programming to build my own customized voice assistant which can open any application I want. 
            I have used text to speech library, speech recognition library and many other libraries according to the application.
            """
        )
        st.markdown("[Project Link](https://github.com/Siddharth-Latthe-07/Personal-Voice-Assistant)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
        st.image(img_5)

    with text_column:
        st.subheader("Air Canvas using ML & Open Cv")

        st.write(
            """
             In this Project, I have made an Air Canvas that can draw anything as per the movement of my hand. 
             We have used the Mediapipe library for hand detection and landmarks.
             Further, created two windows as output,of which the first window will detect the real time movement through webcam and the second will draw the lines as per movement.
            """
        )


        st.markdown("[Project Link](https://github.com/Siddharth-Latthe-07/Air-Canvas)")
with st.container():
    st.write("---")
    st.header("Internship")
    st.write("##")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_3)

    with text_column:
        st.subheader("IoT & Robotics")
        st.write(
            """
            In this internship, I have made a Home Automation System, wherein the lights,fans and doors are automated
            and can be controlled without human interference
            """
        )


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    st.write(":telephone_receiver: 7977472790")
    st.write(":email: siddharthlatthe@gmail.com")
    st.write(":house: Kolhapur")
    st.write(" :point_right: [Github >](https://github.com/Siddharth-Latthe-07)")


    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
   # contact_form = """
    #<form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
     #   <input type="hidden" name="_captcha" value="false">
      #  <input type="text" name="name" placeholder="Your name" required>
       # <input type="email" name="email" placeholder="Your email" required>
        #<textarea name="message" placeholder="Your message here" required></textarea>
        #<button type="submit">Send</button>
    #</form>
  #  """
   # left_column, right_column = st.columns(2)
    #with left_column:
     #   st.markdown(contact_form, unsafe_allow_html=True)
   # with right_column:
    #    st.empty()
