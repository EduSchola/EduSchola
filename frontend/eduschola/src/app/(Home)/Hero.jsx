const Hero = () => {
    return ( 
        <div className="hero w-full bg-[#C0D8FC] relative mt-6 md:mt-4 px-4 py-4 lg:px-8  lg:py-4 md:px-8 md:py-4 xl:px-8 xl:py-4 2xl:px-8 2xl:py-4">
            <div className="hero__texts flex-col flex gap-y-7 xl:gap-y-12 2xl:gap-y-16 md:gap-y-14 lg:gap-y-14 ">
                <h1 className="hero__title font-bold text-2xl xl:w-[40%] 2xl:w-[45%] lg:w-[50%] ">Transform Your Institution With Our Comprehesive Management System</h1>


                <h1 className="hero__subtitle font-medium text-lg xl:w-[40%] lg:w-[50%] 2xl:w-[40%]">
                    Our comprehensive school management system software is designed to help schools and educational institutions manage all aspects of their operations. Whether you&apos;re an administrator, teacher, or parent, our platform provides the tools you need to streamline your work and enhance your students&apos; learning experience.
                </h1>

                <button className="hero__cta-button bg-blue-700 text-white w-fit px-4 xl:px-4 2xl:px-6 md:px-4 lg:px-4 py-2 rounded-md">
                    Get Started
                </button>
            </div>
        </div>
     );
}
 
export default Hero;