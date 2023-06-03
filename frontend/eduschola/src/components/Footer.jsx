import Link from 'next/link'
const Footer = () => {
    return ( 
        <footer className=" 2xl:mt-12 footer relative w-full px-4 py-2 bg-slate-800 flex flex-col xl:flex-row 2xl:flex-row lg:flex-row justify-center gap-x-36 gap-y-12 flex-wrap">
            <div className="company flex flex-col text-white gap-y-3 text-center">
                <h1 className="font-bold text-lg">Company</h1>
                <Link href="/" className="font-medium">About Us</Link>
                <a href="#contact-us font-medium">Contact Us</a>
            </div>

            <div className="company flex flex-col text-white gap-y-3 text-center">
                <h1 className="font-bold text-lg">Features</h1>
                <Link href="/" className="font-medium">Schedule Management</Link>
                <Link href="/" className="font-medium">Parent Portal</Link>
                <Link href="/" className="font-medium">Student Information</Link> 
            </div>

            <div className="company flex flex-col text-white gap-y-3 text-center">
                <h1 className="font-bold text-lg">Resources</h1>
                <Link href="/" className="font-medium">Contact Us</Link>
                <Link href="/" className="font-medium">Help</Link>
                <Link href="/" className="font-medium">Sitemap</Link> 
            </div>
        </footer>
     );
}
 
export default Footer;