import './globals.css'
import { Inter, Poppins } from 'next/font/google'
import Navbar from '@/components/Navbar'

const inter = Inter({ subsets: ['latin']})
const poppins = Poppins({ subsets: ['latin'], weight : '400'  })

export const metadata = {
  title: 'Eduschola',
  description: 'Eduschola is a comprehensive and user-friendly Learning Management System designed to revolutionize the way educational institutions manage and deliver online learning. It provides a centralized platform that seamlessly integrates various learning tools, resources, and administrative functionalities to enhance the overall learning experience.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      {/* suppressHydrationWarning prevents browser extensions from causing a server/client mismatch */}
      <body className={poppins.className}  suppressHydrationWarning={true}> 
        <Navbar />
        {children}</body>
    </html>
  )
}
