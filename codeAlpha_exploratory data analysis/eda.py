import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset.csv")

# Display basic info
print("Dataset Info:")
print(df.info())

# Summary statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check for null values
print("\nMissing Values:")
print(df.isnull().sum())

# Distribution of Ratings
plt.figure(figsize=(6,4))
sns.histplot(df["Rating"], kde=True, bins=5)
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("plots/rating_distribution.png")
plt.show()

# Top 5 books with highest reviews
top_reviews = df.sort_values("Reviews", ascending=False).head(5)
print("\nTop 5 Most Reviewed Books:")
print(top_reviews[["Title", "Author", "Reviews"]])

# Boxplot of Price by Genre
plt.figure(figsize=(8,4))
sns.boxplot(x="Genre", y="Price", data=df)
plt.xticks(rotation=45)
plt.title("Price Distribution by Genre")
plt.savefig("plots/price_by_genre.png")
plt.show()