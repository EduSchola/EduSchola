import Image from 'next/image'
import Hero from './Hero'
import CompanyOverview from './CompanyOverview'
export default function Home() {
  return (
    <div>
      <Hero />
      <CompanyOverview />
    </div>
  )
}
