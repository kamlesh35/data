import streamlit as st 
st.title("Kamlesh Kumar")
st.title("Welcome to the site")
st.header("Python Package")
st.subheader("This is package of python")
st.markdown("My name is kamlesh kumar Now i am learning a new library of python")
st.code('''for i in range(1,100,1):
          print(i)
        
        ''')


# Set a dataset(Excel sheet or database)
# import pandas as pd
# data = pd.read_csv("employees.csv")
# st.dataframe(data)


#Create a form with the help of streamlit
st.subheader("Please Leave Your Details here..")

name = st.text_input("Enter your name :")
fname = st.text_input("Enter your father name :")
adr = st.text_area("Enter your text")

classdata = st.selectbox("Enter your class :",(1,2,3,4,5,6))


# get the data of table ..
button = st.button("Submit")

if button :
    st.markdown(f"""
       Name : {name} \n
       Father name : {fname} \n
       Address : {adr} \n
       class : {classdata}

""")