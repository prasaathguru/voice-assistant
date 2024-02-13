import streamlit as st
from streamlit_chat import message
from annotated_text import annotated_text, annotation

st.set_page_config( layout="wide",page_title="User Manual",page_icon='🎙️')



def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

st.title("User Manual")
st.header("Features Available")

#st.info('You can greet the assistant by using hello, hey, hi', icon="ℹ️")

#1 greetings
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**1. Greetings**")
        annotated_text(('You can greet the g-ai by using the words like : '),('**Hi**, '),('**Hello**'),(',**Hey**') )
        st.write("Example : Hi , What's up")
    with col2:
        message("Hi , What's up",is_user=True)
        message("Hey, what's up?, I'm very well, thanks for asking")    

st.markdown("""---""")


#2 set user/assistant name        
# with st.container():
#     col1,col2 = st.columns(2,gap="large")
#     with col1:
st.markdown("**2. Set User/Assistant Name for the conversation**")
annotated_text(('You can set the g-ai name using the command : '),('your name should be **[Your name]**'),("  "),('[ insert assistant name ]',"keyword" ) )
annotated_text(('You can set the user name using the command : '),('my name is [**Name**]'),('[ insert user name ]',"keyword" ) )
    # with col2:
    #     message("Hello my name is Anna, your name should be Cortana",is_user=True)
    #     message("Okay, i will remember that Anna, okay, i will remember that my name is Cortana")

st.markdown("""---""")

#3 tell the time
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col2:
        st.markdown("**3. Tell the time**")
        annotated_text(('You can Ask the time '),('what\'s the time ',"command"),("  "),('tell me the time ',"command") ,("  "),('what time is it ',"command"),("  "),('what is the time ',"command"))

    with col1:
        message(" whats the time",is_user=True)
    #     message("what time is it",is_user=True)
        message("The time is  10:30 ")

st.markdown("""---""")

#4 search on google 
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**4. Search on Google**")
        # st.markdown("The chatbot is designed to search for key terms and sentences on google such as gold prices, stock status")
        annotated_text(('Search for keywords/sentences on google  e.g. '),('search for ',"command"),("  "),)

    with col2:
        message("Search for Artificial Intelligence",is_user=True)
        message("Here is what I found for AI on google ")

st.markdown("""---""")


#5 search on youtube 
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**5. Search on Youtube**")
        annotated_text(('Search for keywords/sentences on youtube  e.g. '),('search for ',"command"),("  "),)

    with col2:
        message("Search for g-ai on youtube",is_user=True)
        message("Here is what I found for G_AI on youtube ")

st.markdown("""---""")

#6 forecast the weather 
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**6. Get the weather forcast for the day**")
        annotated_text(('What is the weather today e.g. '),('tell me about / what is ',"sentence"),("  "),('weather ',"keyword"))

    with col2:
        message("What is the weather forcast in salem",is_user=True)
        message("Here is what I found for on google")

st.markdown("""---""")

#7 location
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**7. Find location**")
        annotated_text(('Sentence ...',"sentence"),("  "),('what is my exact location ',"keyword"))

    with col2:
        message("what is my exact location ",is_user=True)
        message("You must be somewhere near here, as per Google maps")

st.markdown("""---""")

#7 Exit conversation
with st.container():
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.markdown("**8. Exit the conversation**")
        annotated_text(('Using the following terms indicate the end of the conversation with the bot'),
                       (" "),('bye ',"keyword"),("  "),('quit ',"keyword"),("  "),('done ',"keyword"),("  "),('exit ',"keyword"))

    with col2:
        message("Thank you g-ai, bye ",is_user=True)
        message("Bye")