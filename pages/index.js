import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import SentimentAnalysis from '../components/SentimentAnalysis';
import SearchComponent from '../components/SearchComponent';

export default function Home() {
  return (
    <div>
      <SentimentAnalysis />
      <SearchComponent/>
    </div>
  );
};


