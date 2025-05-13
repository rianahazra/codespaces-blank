# import streamlit as st
# st.write("Hello World")
# st.image("https://i.natgeofe.com/n/4cebbf38-5df4-4ed0-864a-4ebeb64d33a4/NationalGeographic_1468962_square.jpg",width=100)

import streamlit as st
st.header('Streamlit is :blue[cool] :cockroach:',divider="rainbow")
tab1,tab2,tab3=st.tabs(["🌟 About Me 🌟","🎨 Hobbies","🏆 Achievements"])
with tab1:
    st.title("🌟 About Me 🌟")
    column1,column2=st.columns([0.7,0.3])
    with column1:
        # Name Section
        st.header("👤 Name")
        st.text("Riana Hazra")
        st.image("https://i.ytimg.com/vi/hw4_JfzEgWc/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBVSQb13rCl_xc-dxiLOzH-oxdHKQ", width=500)
    with column2:
        # About Section
        st.header("Biography :cockroach: ")
        st.text("I like coding in python and hiking in national parks")
    
        #Contact Section
        st.header("Contact Information :sunglasses: :spider:")
        st.text("""Phone Number: 123-456-7890 
                Address: Sesame street
                Email: abc@gmail.com""")
with tab2: 
    # Hobbies Section
    st.header("🎨 Hobbies")
    st.text("- Coding 💻")
    st.text("- Hiking 🚶‍♀️‍➡️")
    st.image("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/cd/70/9b/guano-point.jpg?w=1200&h=-1&s=1", width=400)
    st.text("- Music 🎵")
with tab3:
    # Achievements Section
    st.header("🏆 Achievements")
    st.text("- Won a science competition 🏅")
    st.text("- Valedictorian")
    st.text("- Won a debate competition 💬")
