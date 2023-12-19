#Imports
import pickle
import streamlit as st
import sklearn

# to run in command line use the following command: streamlit run streamlit_app.py



st.title('**Experiencing a Book Hangover?**')
st.markdown("##### _Let's explore the books waiting on your TBR (to-be-read) list..._")
st.text("")
st.text("")
st.text("")

st.markdown("**In the space provided below, input the author and title of your book in the following format:**")
st.markdown("<p style='text-align: center;'>Author : Title</p>", unsafe_allow_html=True)
st.text("")
st.text("")


st.markdown("**Here is an example...**")
st.markdown("<p style='text-align: center;'>Suzanne Collins : The Hunger Games</p>", unsafe_allow_html=True)
st.text("")
st.text("")


#Load pickled pipeline so we can take inouts and make predictions
with open('code/book_pipe.pkl', 'rb') as pickle_in:
    pipe = pickle.load(pickle_in)

# get user input
user_text = st.text_input('Please input the author and title of your book following the format outlined above:')

#now generate predictions
predicted = pipe.predict([user_text])[0]

#display predictions
st.markdown(f'**Your prediction is: {predicted}**')



st.markdown("- A prediction of 1 indicates that this book is worthy of breaking the book hangover. Read it now!")
st.markdown("- A prediction of 0 indicates that a you should still read this book, but it is not going to be the 'next great read' that will pull you out of your book hangover.")
