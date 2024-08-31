######## Import the required pacakges ############
import streamlit as st
import google.generativeai as genai
from PIL import Image

####### Provide your api key ###################
api_key="AIzaSyCqjRhE8u9tgGCKBLxrGsWW7eJgUqRj5q0"
genai.configure(api_key=api_key)

######## Choose the heading ###############
st.header("Recycle  Image analytics")

########## Upload a file ##################
uploaded_file=st.file_uploader("Upload an image",type=["png","jpg","jpeg"])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))

############ What you want ask ####################
##prompt=st.text_input("Enter the text")
prompt="We are a Materials Recovery Facility that works towards recycling items to better the environment. Only certain materials can be recycled to produce high quality recycled materials. Therefore, I need your help to understand if an item can or can’t be recycled depending on the item’s materials. If recyclable, I need to know how the item can be recycled. Additionally, use the location to determine if local recycling facilities accept those materials. Can I recycle the inputted image?"
############ Prompt Template ####################

#"You are a waste management expert and you should know what to recycle or not based on the user provided object"

######### Use genai skill ##########################

if st.button("GET RESPONSE"):
    img=Image.open(uploaded_file)
    model=genai.GenerativeModel("gemini-1.5-flash-latest")
    response=model.generate_content([prompt,img])
    st.markdown(response.parts)


# capture user input and display bot response
user_input = st.text_input("Enter the item")

if st.button("RECYCLE"):
    #img=Image.open(uploaded_file)
   ## recycle_prompt="Is the entered text recyclable or not?"
    recycle_prompt = f"We are a Materials Recovery Facility that works towards recycling items to better the environment. Only certain materials can be recycled to produce high quality recycled materials. Therefore, I need your help to understand if an item can or can’t be recycled depending on the item’s materials. If recyclable, I need to know how the item can be recycled. Additionally, use the location to determine if local recycling facilities accept those materials. Can I recycle the {user_input}?"

    model=genai.GenerativeModel("gemini-1.5-flash-latest")
   ##response=model.generate_content([recycle_prompt,user_input])
    response=model.generate_content(recycle_prompt)

    st.markdown(response.parts)