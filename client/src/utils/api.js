export const fetchBackendMessage = async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/');
    const data = await res.json();
    return data.message;
  } catch (error) {
    console.error("Failed to fetch backend:", error);
    return "Error connecting to backend.";
  }
};

export const fetchMultipleStocks = async (symbols = ["AAPL","GOOGL","MSFT"]) => {
  const query = symbols.join(",");
  const res = await fetch(`http://127.0.0.1:8000/api/stocks/?symbols=${query}`);
  return res.json();
};

export const fetchMultipleCryptos = async (symbols = ["BTC","ETH","LTC"]) => {
  const query = symbols.join(",");
  const res = await fetch(`http://127.0.0.1:8000/api/crypto/?symbols=${query}`);
  return res.json();
};

export const fetchLatestNews = async (category = "stocks") => {
  const res = await fetch(`http://127.0.0.1:8000/api/news?query=${category}`);
  return res.json();
};