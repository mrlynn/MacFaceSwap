import './globals.css'

export const metadata = {
  title: 'MacFaceSwap',
  description: 'Real-time face swapping for macOS',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body suppressHydrationWarning={true}>
        {children}
      </body>
    </html>
  )
}