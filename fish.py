import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('Fish.csv')
avg_height_by_species = df.groupby('Species')['Height'].mean().reset_index() 
#result is stored in a new DataFrame called 'avg_height_by_species
#reset_index() is used to reset the index of the DataFrame so that 'Species' becomes a regular column
plt.bar(avg_height_by_species['Species'], avg_height_by_species['Height'])
plt.title('Species by their Average Height')
plt.xlabel('Species')
plt.ylabel('Avg Height')
st.pyplot(plt)