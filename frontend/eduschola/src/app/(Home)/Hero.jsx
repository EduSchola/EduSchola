const Hero = () => {
    return ( 
        <div className="hero w-full bg-[#C0D8FC] relative xl:mt-[2%] 2xl:mt-[2%] xl:px-8 xl:py-4 2xl:px-8 2xl:py-4">
            <div className="hero__texts flex-col flex xl:gap-y-12 2xl:gap-y-16 ">
                <h1 className="hero__title font-bold text-2xl xl:w-[40%] 2xl:w-[45%]">Transform Your Institution With Our Comprehesive Management System</h1>

                <h1 className="hero__subtitle font-medium text-lg xl:w-[40%] 2xl:w-[40%]">
                    Our comprehensive school management system software is designed to help schools and educational institutions manage all aspects of their operations. Whether you&apos;re an administrator, teacher, or parent, our platform provides the tools you need to streamline your work and enhance your students&apos; learning experience.
                </h1>

                <button className="hero__button bg-blue-700 text-white w-fit xl:px-4 xl:py-2 2xl:px-6 2xl:py-2 rounded-md">
                    Get Started
                </button>
            </div>
        </div>
     );
}
 
export default Hero;