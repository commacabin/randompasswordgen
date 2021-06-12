import streamlit as st
import pandas as pd
import string
import random


Pas_Length=[8,9,10,11,12,13,14,15,16]
st.write("PASSWORD GENERATOR")
st.sidebar.header('Create a Strong Password')

Length = st.sidebar.selectbox('Select the LENGTH of Password',Pas_Length, 1)


s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
def create_Password():
        data1 = "".join(random.sample(s, Length))
        data = {'LENGTH': Length
                , 'PASSWORD': data1}
        features = pd.DataFrame(data, index=[1])
        st.write(features)
        st.write(data1)
st.subheader('User Entered LENGTH OF PASSWORD ')
st.subheader('Your Generated Password is ')
st.sidebar.button('Create Random Password',create_Password() )

