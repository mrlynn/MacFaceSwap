import './globals.css'

export const metadata = {
  title: 'FaceSwap',
  description: 'Real-time face swapping application for macOS',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
