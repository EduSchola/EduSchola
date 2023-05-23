import Link from "next/link";
const Navbar = () => {
    return ( 
        <header className="navbar w-full flex xl:pt-5 xl:px-5 items-center">
            <div className="navbar-logo font-bold text-xl xl:mr-16">LOGO</div>
            <nav className="navbar__nav-items nav-items flex ">
                <div className="nav-items hidden xl:flex xl:gap-x-20 mr-64 mt-2">
                    <Link href="/" className="nav-items__link">Home</Link>
                    <Link href="/" className="nav-items__link">Features</Link>
                    <Link href="/" className="nav-items__link">Pricing</Link>
                    <Link href="/" className="nav-items__link">Contact Us</Link>
                </div>

                <div className="nav-btns hidden xl:flex gap-x-10 mt-2 ">
                    <button className="btn">Sign In</button>
                    <button className="btn border-2 px-3 py-1 border-blue-600 rounded-lg text-blue-600 ">Get Started</button>
                </div>
                
            </nav>
        </header>
     );
}
 
export default Navbar;