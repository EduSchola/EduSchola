const Hero = () => {
    return ( 
        <div className="hero w-full bg-[#C0D8FC] relative xl:mt-[2%] px-8 py-4">
            <div className="hero__texts xl:flex-col xl:flex gap-y-12 ">
                <h1 className="hero__title font-bold text-2xl xl:w-[40%]">Transform Your Institution With Our Comprehesive Management System</h1>

                <h1 className="hero__subtitle font-medium text-lg xl:w-[40%]">
                    Our comprehensive schoool management system software is designed to help schools and educational institutions manage all aspects of their operations. Whether you're an administrator, teacher or parent. Our platform provides the tools you need to streamline your work and enhance your students' learning experience.
                </h1>

                <button className="hero__button bg-blue-700 text-white w-fit px-4 py-2 rounded-md">
                    Get Started
                </button>
            </div>
        </div>
     );
}
 
export default Hero;