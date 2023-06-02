import { RiHeadphoneFill } from 'react-icons/ri';
const CompanyOverview = () => {
    return ( 
        <div className=" px-4 py-10 2xl:py-12 company-overview">
            <div className="company-overview__texts text-center flex flex-col gap-y-6 xl:gap-y-6 2xl:gap-y-8 md:gap-y-8 lg:gap-y-8 ">
                <h1 className="company-overview__title text-2xl xl:text-2xl 2xl:text-3xl md:text-2xl lg:text-2xl font-semibold">The Ultimative Intuitive And User-Friendly Education Management Solution</h1>

                <h1 className="company-overview__subtitle xl:w-[65%] 2xl:w-[55%] lg:w-[70%] md:w-[70%] mx-auto">
                    Eduschola provides a comprehensive and user-friendly solution for managing all aspects of your educational platform. From admissions and student records to academic planning and financial management, our platform streamlinnes your daily operations and frees up your time to focus what really matters: providing quality education to your students
                </h1>
            </div>

            <div className="key-points mt-20 xl:mt-28 2xl:mt-28 lg:mt-20 md:mt-24 2xl:ml-[20%] gap-y-32 2xl:gap-x-64 2xl:gap-y-40 2xl:w-[60%] w-full flex flex-col 2xl:flex-row 2xl:flex-wrap justify-center items-center">
                <div className="key-point border-blue-600 w-96 h-fit border-2 px-4 py-4 flex flex-col items-center justify-center gap-y-5 2xl:gap-y-3 ">
                    <h1 className='text-2xl font-bold text-center'>Customer Support</h1>
                    <RiHeadphoneFill className="text-5xl text-blue-500 mx-auto" />
                    <div className="key-point__description xl:w-[70%] 2xl:w-[90%] mx-auto ">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas, eligendi! Culpa iste harum provident nobis modi, porro enim sunt incidunt quos maxime
                    </div>
                </div>

                <div className="key-point border-blue-600 w-96 h-fit border-2 px-4 py-4 flex flex-col items-center justify-center gap-y-5 2xl:gap-y-3 ">
                    <h1 className='text-2xl font-bold text-center'>Customer Support</h1>
                    <RiHeadphoneFill className="text-5xl text-blue-500 mx-auto" />
                    <div className="key-point__description xl:w-[70%] 2xl:w-[90%] mx-auto ">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas, eligendi! Culpa iste harum provident nobis modi, porro enim sunt incidunt quos maxime
                    </div>
                </div>

                <div className="key-point border-blue-600 w-96 h-fit border-2 px-4 py-4 flex flex-col items-center justify-center gap-y-5 2xl:gap-y-3  ">
                    <h1 className='text-2xl font-bold text-center'>Customer Support</h1>
                    <RiHeadphoneFill className="text-5xl text-blue-500 mx-auto" />
                    <div className="key-point__description xl:w-[70%] 2xl:w-[90%] mx-auto ">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas, eligendi! Culpa iste harum provident nobis modi, porro enim sunt incidunt quos maxime
                    </div>
                </div>
            </div>

        </div>
     );
}
 
export default CompanyOverview;