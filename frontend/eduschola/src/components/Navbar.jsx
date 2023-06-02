"use client"
import Link from "next/link";
import { GiHamburgerMenu } from 'react-icons/gi';
import { AiOutlineClose } from 'react-icons/ai';
import { useState } from "react";

const Navbar = () => {

    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const handleLinkClick = () => {
        setIsMenuOpen(false);
      };
    return ( 
        <header className=" w-full">
            <nav className="navbar w-full flex px-5 pt-5 items-center justify-between">
                <div className="logo w-12 h-12 2xl:w-14 2xl:h-14 rounded-full bg-orange-500 "></div>

                <div className="navbar__links xl:flex 2xl:flex lg:flex xl:gap-x-20 2xl:gap-x-20 lg:gap-x-14 md:gap-x-14 text-lg font-medium hidden ">
                    <Link href="/" className="navbar__links text-blue-500  underline">Home</Link>
                    <Link href="/" className="navbar__link">Features</Link>
                    <Link href="/" className="navbar__link">Pricing</Link>
                    <Link href="/" className="navbar__link">Contact Us</Link>
                    
                </div>

                <div className="xl:flex 2xl:flex lg:flex hidden gap-x-8 ">
                    <button className="navbar__btn">
                        Sign In
                    </button>

                    <button className="navbar__btn border border-blue-500 text-blue-500 rounded-md xl:px-3 xl:py-1 2xl:px-3 2xl:py-1 lg:px-3 lg:py-1">
                        Get Started
                    </button>
                </div>

                <div className="hamburger-menu xl:hidden 2xl:hidden lg:hidden">
                    { !isMenuOpen && <button onClick={() => setIsMenuOpen(prev => !prev)} className="text-3xl" >
                        <GiHamburgerMenu />
                    </button>}

                    { isMenuOpen && <button onClick={() => setIsMenuOpen(prev => !prev)} className="text-3xl" >
                        <AiOutlineClose />
                    </button>}
                        

                    <ul className={`subNavbar flex  flex-col fixed z-10 left-0 gap-14 h-[100vh] justify-center items-center w-[100vw] bg-white mt-2 text-2xl transition-all duration-500    
                    ${isMenuOpen ? 'translate-x-0':' translate-x-full'}`}>

                        <Link href="/" className="navbar__links text-blue-500  underline" onClick={() => handleLinkClick()} >Home</Link>
                        <Link href="/" className="navbar__link" onClick={() => handleLinkClick()} >Features</Link>
                        <Link href="/" className="navbar__link" onClick={() => handleLinkClick()} >Pricing</Link>
                        <Link href="/" className="navbar__link" onClick={() => handleLinkClick()} >Contact Us</Link>

                        <button className="navbar__btn">
                            Sign In
                        </button>

                        <button className="navbar__btn ">
                            Get Started
                        </button>

                    </ul>
                    
                </div>
            </nav>
        </header>
     );
}
 
export default Navbar;