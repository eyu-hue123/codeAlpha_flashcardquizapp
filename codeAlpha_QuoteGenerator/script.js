const quotes = [
  { text: "The best way to get started is to quit talking and begin doing.", author: "Walt Disney" },
  { text: "Don't let yesterday take up too much of today.", author: "Will Rogers" },
  { text: "It's not whether you get knocked down, it's whether you get up.", author: "Vince Lombardi" },
  { text: "Success is not final, failure is not fatal: It is the courage to continue that counts.", author: "Winston Churchill" },
  { text: "Act as if what you do makes a difference. It does.", author: "William James" },
  { text: "Believe you can and you're halfway there.", author: "Theodore Roosevelt" }
];

const quoteText = document.getElementById("quote");
const quoteAuthor = document.getElementById("author");
const newQuoteBtn = document.getElementById("newQuote");

function showRandomQuote() {
  const random = Math.floor(Math.random() * quotes.length);
  quoteText.textContent = quotes[random].text;
  quoteAuthor.textContent = - ${quotes[random].author};
}

newQuoteBtn.addEventListener("click", showRandomQuote);

// Show one at start
showRandomQuote();