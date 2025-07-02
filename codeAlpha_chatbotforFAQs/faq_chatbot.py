import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data (only once)
nltk.download('punkt')

# FAQ dataset (you can add more!)
faqs = {
    "What is your return policy?": "You can return any item within 30 days.",
    "How can I contact support?": "You can contact us at support@example.com.",
    "Do you offer international shipping?": "Yes, we ship to over 100 countries.",
    "How do I reset my password?": "Click on 'Forgot password' on the login page.",
    "What payment methods are accepted?": "We accept credit cards, PayPal, and UPI."
}

# Create vectorizer
vectorizer = TfidfVectorizer()

def get_response(user_input):
    questions = list(faqs.keys())
    all_texts = questions + [user_input]  # Add user's input to FAQ list

    tfidf = vectorizer.fit_transform(all_texts)
    similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
    best_match_index = np.argmax(similarity)

    # If similarity is low, say "I don't understand"
    if similarity[0][best_match_index] < 0.3:
        return "Sorry, I don't understand your question."
    return faqs[questions[best_match_index]]

# Chat loop
print("🤖 Welcome to the FAQ Chatbot! (Type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bot: Goodbye! 👋")
        break
    response = get_response(user_input)
    print("Bot:", response)