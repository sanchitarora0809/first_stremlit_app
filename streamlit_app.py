
import streamlit ;
import pandas ;
streamlit.title('My Parents New Healthier Diner')

streamlit.header('Breakfast')
streamlit.text(' 🥣 Omega 3 & blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


streamlit.dataframe(my_fruit_list)
