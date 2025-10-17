'use client';
import { useEffect, useState } from 'react';
import { fetchMultipleStocks } from '@/utils/api';

export default function Home() {
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    fetchMultipleStocks(["AAPL", "GOOGL", "MSFT", "TSLA"]).then(setStocks);
  }, []);

  if (!stocks.length) return <p>Loading...</p>;

  return (
    <main>
      <h1>Live Stock Dashboard</h1>

      <div>
        {stocks.map((s) => (
          <div key={s.symbol}>
            <h2>{s.symbol}</h2>
            <h3>{s.name}</h3>
            <p>Sector: {s.sector}</p>
            <p>Price: ${s.price?.toFixed(2)}</p>
            <p>
              Change: {s.change}
            </p>
            <p>Volume: {s.volume?.toLocaleString()}</p>
          </div>
        ))}
      </div>
    </main>
  );
}