'use client';
import { useEffect, useState } from 'react';
import { fetchBackendMessage } from '@/utils/api';

export default function Home() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetchBackendMessage().then(setMessage);
  }, []);

  return (
    <main className="flex items-center justify-center h-screen text-2xl">
      <p>{message}</p>
    </main>
  );
}