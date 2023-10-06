import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
file_path = "TitanicSurvival.csv"
df = pd.read_csv(file_path)

# Cleaning the data (fill missing 'age' values with median)
median_age = df['age'].median()
df['age'].fillna(median_age, inplace=True)

# Define visualizations
def survival_rate_by_gender():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='sex', hue='survived', data=df)
    plt.title("Survival Rate by Gender")
    return plt

def age_distribution():
    plt.figure(figsize=(8, 6))
    plt.hist(df['age'].dropna(), bins=20)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    return plt

def survival_distribution():
    plt.figure(figsize=(8, 6))
    survival_counts = df['survived'].value_counts()
    plt.pie(survival_counts, labels=['Not Survived', 'Survived'], autopct='%1.1f%%', startangle=140)
    plt.title("Survival Distribution")
    plt.axis('equal')
    return plt

def age_density():
    plt.figure(figsize=(8, 6))
    age_counts = df['age'].value_counts(normalize=True).sort_index()
    plt.fill_between(age_counts.index, 0, age_counts.values, color='blue', alpha=0.3)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Density")
    return plt

def age_vs_passenger_class():
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='passengerClass', y='age', data=df)
    plt.title("Age vs. Passenger Class")
    return plt

# Add interactive element (dropdown menu)
visualization_option = st.selectbox("Select Visualization", ["Survival Rate by Gender", "Age Distribution",
                                                            "Survival Distribution", "Age Density",
                                                            "Age vs. Passenger Class"])

# Display selected visualization
if visualization_option == "Survival Rate by Gender":
    st.pyplot(survival_rate_by_gender())
elif visualization_option == "Age Distribution":
    st.pyplot(age_distribution())
elif visualization_option == "Survival Distribution":
    st.pyplot(survival_distribution())
elif visualization_option == "Age Density":
    st.pyplot(age_density())
elif visualization_option == "Age vs. Passenger Class":
    st.pyplot(age_vs_passenger_class())
