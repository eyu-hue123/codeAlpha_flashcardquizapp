document.getElementById("bookingForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    name: document.getElementById("name").value,
    origin: document.getElementById("origin").value,
    destination: document.getElementById("destination").value,
    travel_date: document.getElementById("travel_date").value,
    payment_method: document.getElementById("payment").value,
  };

  const res = await fetch("http://localhost:5000/book", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await res.json();
  document.getElementById("response").innerText = result.message || result.error;
});
