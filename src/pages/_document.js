// src/pages/_document.js
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  const baseUrl = process.env.NODE_ENV === 'production' 
    ? 'https://macfaceswap.com' 
    : '';

  return (
    <Html>
      <Head>
        <base href={baseUrl + '/'} />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}