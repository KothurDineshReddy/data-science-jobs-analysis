import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('Fish.csv')
avg_height_by_species = df.groupby('Species')['Height'].mean().reset_index() 
fig, (ax1, ax2) = plt.subplots(2)
ax1.bar(avg_height_by_species['Species'], avg_height_by_species['Height'])
ax1.set_title('Species by their Average Height')
ax1.set_xlabel('Species')
ax1.set_ylabel('Avg Height')
ax2.axis('off')  # Turn off axis for the DataFrame table
ax2.table(cellText=avg_height_by_species.values, colLabels=avg_height_by_species.columns, loc='center')
# Adjust layout to prevent overlap
plt.tight_layout()
# Display the subplots in the Streamlit app
st.pyplot(fig)
