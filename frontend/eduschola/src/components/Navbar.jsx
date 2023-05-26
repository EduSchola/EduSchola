import Link from "next/link";
const Navbar = () => {
    return ( 
        <header className=" w-full ">
            <nav className="navbar w-full flex xl:pt-5 xl:px-5 items-center">
                <div className="logo xl:w-12 xl:h-12 rounded-full bg-orange-500 xl:mr-[10%]"></div>

                <div className="navbar__links flex gap-x-20 text-lg font-medium xl:mr-[15%]">
                    <Link href="/" className="navbar__links text-blue-500 underline">Home</Link>
                    <Link href="/" className="navbar__link">Features</Link>
                    <Link href="/" className="navbar__link">Pricing</Link>
                    <Link href="/" className="navbar__link">Contact Us</Link>
                </div>

                <div className="flex gap-x-8">
                    <button className="navbar__btn">
                        Sign In
                    </button>

                    <button className="navbar__btn border border-blue-500 text-blue-500 rounded-md xl:px-3 xl:py-1">
                        Get Started
                    </button>
                </div>
            </nav>
        </header>
     );
}
 
export default Navbar;