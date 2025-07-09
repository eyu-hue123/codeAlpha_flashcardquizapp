import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
df = pd.read_csv("dataset.csv")

# Create folder for charts
os.makedirs("charts", exist_ok=True)

# 1. Bar Chart: Top 5 Most Reviewed Books
top_reviews = df.sort_values("Reviews", ascending=False).head(5)
plt.figure(figsize=(8,4))
sns.barplot(x="Title", y="Reviews", data=top_reviews)
plt.xticks(rotation=45)
plt.title("Top 5 Most Reviewed Books")
plt.tight_layout()
plt.savefig("charts/top_reviews.png")
plt.close()

# 2. Boxplot: Price by Genre
plt.figure(figsize=(8,4))
sns.boxplot(x="Genre", y="Price", data=df)
plt.xticks(rotation=45)
plt.title("Book Price Distribution by Genre")
plt.tight_layout()
plt.savefig("charts/price_by_genre.png")
plt.close()

# 3. Scatter Plot: Reviews vs Rating
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="Rating", y="Reviews", hue="Genre")
plt.title("Rating vs Reviews")
plt.tight_layout()
plt.savefig("charts/rating_vs_reviews.png")
plt.close()

print("✅ Charts saved in /charts folder.")