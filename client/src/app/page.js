'use client';
import { useEffect, useState } from 'react';
import { fetchMultipleStocks, fetchMultipleCryptos,  } from '@/utils/api';
import { fetchLatestNews } from '@/utils/api';

export default function Home() {
  const [stocks, setStocks] = useState([]);
  const [cryptos, setCryptos] = useState([]);
  const [news, setNews] = useState([]);

  useEffect(() => {
    const stockSymbols = ["AAPL", "GOOGL", "MSFT", "NVDA", "AMZN", "TSLA", "META", "GC=F", "^GSPC", "^NDX"];
    const cryptoSymbols = ["BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD"];
    fetchMultipleStocks(stockSymbols).then(setStocks);
    fetchMultipleCryptos(cryptoSymbols).then(setCryptos);
    const allSymbols = [...stockSymbols, ...cryptoSymbols].join(',');
    fetchLatestNews(allSymbols).then(setNews);
  }, []);

  if (!stocks.length && !cryptos.length && !news.length) return <p>Loading...</p>;

  return (
    <main>
      <h1>Live Market Dashboard</h1>

      <section>
        <h2>Stocks</h2>
        {stocks.map((s) => (
          <div key={s.symbol}>
            <h3>{s.symbol} - {s.name}</h3>
            <p>Price: ${s.price?.toFixed(2)}</p>
            <p>Change: {s.change}%</p>
            <p>Volume: {s.volume?.toLocaleString()}</p>
          </div>
        ))}
      </section>

      <section>
        <h2>Cryptocurrencies</h2>
        {cryptos.map((c) => (
          <div key={c.symbol}>
            <h3>{c.symbol} - {c.name}</h3>
            <p>Price: ${c.price?.toFixed(2)}</p>
            <p>Change: {c.change}%</p>
            <p>Volume: {c.volume?.toLocaleString()}</p>
          </div>
        ))}
      </section>

      <section>
        <h2>Latest News</h2>
        {news.map((article, index) => (
          <div key={index}>
            <h3>{article.title}</h3>
            <p>{article.description}</p>
            <a href={article.url} target="_blank" rel="noopener noreferrer">Read more</a>
          </div>
        ))}
      </section>
    </main>
  );
}