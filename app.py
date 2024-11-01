import streamlit as st



st.set_page_config(page_title="My OWN Webpage",page_icon=":tada:",layout="wide")


with st.container():

    st.write("HI,I AM LALITH :wave: ")
    st.write("A STUDENT LEARNING WEB DEV ")
    st.write("I AM CURIOUS IN LEARNING NEW THINGS ") 


with st.container():
    st.write("-----------")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("WHAT I DO")
        
        st.write("*I AM A STUDENT AS I SAY THAT I AM CURIOUS IN LEARNING THAS WHICH ARE APPART FROM ACADEMICS AS ILOVE THING APPART FROM ACADEMICS SPREAD PEACE THANK YOU!")
                             

with st.container():
    st.write("--------")
    st.header("MY BLOG")
    st.write("##")
    image_column, text_column=st.columns((1,2))

    with text_column:
        st.subheader("THE BLOG IS ABOUT AGRICULTURE IN NORTH INDIA ")
        st.write("FROM READING THAT YOU MAY KNOW ABOUT THE STAGE OF  AGRICULTURE IN NORTH INDIA ")
        st.markdown("[SEE THIS .....](http://lalithkishore194.blogspot.com)")

        contact_form = """
        <form action="https://formsubmit.co/kishorelalith194@gmail.com" method="POST">
           <input type="hidden" name="_captcha" value="false"> 
           <input type="text" name="name"placeholder="Your name" required>
           <input type="email" name="email"placeholder="Your email"required>
           <textarea name="message"placeholder="Your message here "required></textarea>
           <button type="submit">Send</button>
        </form>
        """
        left_column,right_column =st.columns(2)
        with left_column:
            st.markdown(contact_form,unsafe_allow_html=True)
        with right_column:
            st.empty








