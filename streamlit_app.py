import streamlit
import pandas

streamlit.title("My Helathy Diner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣🥑🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗ale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pcik Some Fruits:",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
