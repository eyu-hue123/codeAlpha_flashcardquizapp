# 💬 Sentiment Analysis Project

## 📁 Dataset
Contains 10 sample product reviews in a CSV file:
- Review

## 🛠️ Tools Used
- Python
- TextBlob (for sentiment analysis)
- matplotlib (for visualization)

## 🔍 What It Does
- Analyzes each review's sentiment using TextBlob
- Calculates polarity (from -1 to 1)
- Classifies as Positive, Negative, or Neutral
- Creates a bar chart showing sentiment distribution

## ▶️ How to Run
1. Make sure reviews.csv is in the same folder.
2. Install required libraries:
   ```bash
   pip install pandas textblob matplotlib
   python -m textblob.download_corpora