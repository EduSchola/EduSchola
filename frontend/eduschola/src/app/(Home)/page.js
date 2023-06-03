import Hero from './Hero'
import CompanyOverview from './CompanyOverview'
import ContactUs from './ContactUs'
import WhyChooseUs from './WhyChooseUs'
import Footer from '@/components/Footer'
export default function Home() {

  return (
    <div>
      <Hero />
      <CompanyOverview />
      <ContactUs />
      <WhyChooseUs />
      <Footer />
    </div>
  )
}
