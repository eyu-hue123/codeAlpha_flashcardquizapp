import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv("reviews.csv")

# Function to get sentiment polarity
def get_polarity(text):
    return TextBlob(text).sentiment.polarity

# Apply sentiment analysis
df["Polarity"] = df["Review"].apply(get_polarity)

# Classify sentiment
def classify_sentiment(p):
    if p > 0:
        return "Positive"
    elif p < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Polarity"].apply(classify_sentiment)

# Print summary
print(df[["Review", "Polarity", "Sentiment"]])

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Plot sentiment distribution
sentiment_counts = df["Sentiment"].value_counts()
sentiment_counts.plot(kind="bar", color=["green", "red", "gray"])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/sentiment_distribution.png")
plt.close()

print("✅ Sentiment analysis complete. Chart saved to /charts.")