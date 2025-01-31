import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (assuming it's unzipped and named 'Netflix_shows_movies.csv')
df = pd.read_csv("netflix_data.csv")

# Display basic info and check for missing values
print(df.info())
print(df.isnull().sum())

# Fill missing values (e.g., replacing NaN in 'cast' and 'director' with 'Unknown')
df.fillna({"director": "Unknown", "cast": "Unknown"}, inplace=True)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# Exploratory Data Analysis (EDA)
print("\nSummary Statistics:\n", df.describe(include='all'))

# Visualizing the most common genres
plt.figure(figsize=(10, 6))
sns.countplot(y=df['listed_in'].value_counts().index[:10], 
              data=df, order=df['listed_in'].value_counts().index[:10], 
              palette='coolwarm')
plt.title("Top 10 Most Common Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

# Distribution of ratings
plt.figure(figsize=(8, 5))
sns.countplot(x=df['rating'], data=df, order=df['rating'].value_counts().index, palette='viridis')
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Export one visualization for R
plt.figure(figsize=(8, 5))
sns.histplot(df['release_year'], bins=20, kde=True, color='blue')
plt.title("Distribution of Movies and Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.savefig("release_year_distribution.png")  # Save as image for R
plt.show()