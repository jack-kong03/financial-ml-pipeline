'use client';
import { useEffect, useState } from 'react';
import { fetchStockData } from '@/utils/api';

export default function Home() {
  const [stock, setStock] = useState(null);

  useEffect(() => {
    fetchStockData().then(setStock);
  }, []);

  if (!stock) return <p>Loading...</p>;

  return (
    <main className="flex flex-col items-center justify-center h-screen text-xl">
      <h1 className="text-3xl font-bold mb-4">Stock Data</h1>
      <p>Symbol: {stock.symbol}</p>
      <p>Price: ${stock.price}</p>
      <p>Change: {stock.change}</p>
      <p>Volume: {stock.volume.toLocaleString()}</p>
    </main>
  );
}