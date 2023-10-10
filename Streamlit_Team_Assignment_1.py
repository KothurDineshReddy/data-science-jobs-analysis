#This is a team work
#Team members:
#Nikitha Goturi (017424550)
#Harshitha Reddy Lingala (017406545)
#Dinesh Reddy Kothur (017475367)
#Ganaprathyusha puluputhurimuni(016800602)
#Nimmagadda karthik(016996148)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Loading the Titanic dataset through pandas
file_path = "TitanicSurvival.csv"
df = pd.read_csv(file_path)

# Cleaning the data (fill missing 'age' values with median)
median_age = df['age'].median()
df['age'].fillna(median_age, inplace=True)

# visualizations
def survival_rate_by_gender():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='sex', hue='survived', data=df)
    plt.title("Survival Rate by Gender")
    return plt

def age_distribution():
    plt.figure(figsize=(8, 6))
    plt.hist(df['age'])
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    return plt

def age_heatmap():
    plt.figure(figsize=(10, 8))
    heatmap_data = df.pivot_table(index='passengerClass', columns='sex', values='age', aggfunc='mean')
    sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', cbar=True)
    plt.title("Age Heatmap by Passenger Class and Sex")
    plt.xlabel("Sex")
    plt.ylabel("Passenger Class")
    return plt

def age_vs_passenger_class():
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='passengerClass', y='age', data=df)
    plt.title("Age vs. Passenger Class")
    return plt

# Define the double donut chart function
def double_donut_chart():
    labels = ['Not Survived', 'Survived']
    values = df['survived'].value_counts().values

    fig = go.Figure()

    # Outer donut
    fig.add_trace(go.Pie(
        labels=labels,
        values=values,
        hole=0.6,
        name='Total',
        textinfo='label+percent',
        domain=dict(x=[0, 0.48]),
    ))

    fig.update_layout(title="Double Donut Chart - Survival Distribution")

    return fig

# Adding the  interactive element i.e (dropdown menu)
visualization_option = st.selectbox("Select Visualization", ["Survival Rate by Gender", "Age Distribution",
                                                             "Age Heatmap",
                                                            "Age vs. Passenger Class", "Double Donut Chart"])

#To display the selected graphs 
if visualization_option == "Survival Rate by Gender":
    st.pyplot(survival_rate_by_gender())
    st.write("Analysis: survival rate of female is higher than male ")
    
elif visualization_option == "Age Distribution":
    st.pyplot(age_distribution())
    st.write("Analysis: 20 to 40 age group contribute 70% of the popuplation on the ship ")

elif visualization_option == "Age Heatmap":
    st.pyplot(age_heatmap())
    st.write(" The heatmap visualizes the average ages of passengers based on their class and gender")
    
elif visualization_option == "Age vs. Passenger Class":
    st.pyplot(age_vs_passenger_class())
    st.write(" Analysis: Box plot shows that average age of 1st class passengers is around 36,2nd is around 29,3rd is 25" )
   
elif visualization_option == "Double Donut Chart":
    st.plotly_chart(double_donut_chart())
    st.write(" Analysis:38.2% of the passengers on the Titanic survived the disaster, while the 61.8% did not.")
    
