import { RiHeadphoneFill } from 'react-icons/ri';
const CompanyOverview = () => {
    return ( 
        <div className="xl:mt-[2%] 2xl:mt-[2%] px-4 py-2 company-overview">
            <div className="company-overview__texts text-center flex flex-col xl:gap-y-6 2xl:gap-y-8 ">
                <h1 className="company-overview__title xl:text-2xl 2xl:text-3xl font-semibold">The Ultimative Intuitive And User-Friendly Education Management Solution</h1>

                <h1 className="company-overview__subtitle xl:w-[65%] 2xl:w-[55%] mx-auto">
                    Eduschola provides a comprehensive and user-friendly solution for managing all aspects of your educational platform. From admissions and student records to academic planning and financial management, our platform streamlinnes your daily operations and frees up your time to focus what really matters: providingquality education to your students
                </h1>
            </div>

            <div className="key-points xl:mt-[10%] 2xl:mt-[10%] 2xl:ml-[20%] xl:ml-[8%] 2xl:gap-x-64 xl:gap-x-48 xl:gap-y-32 2xl:gap-y-40 2xl:w-[60%] xl:w-[95%] flex flex-wrap">
                <div className="key-point border-blue-600 2xl:w-96 xl:w-96 h-fit border-2 xl:px-4 xl:py-4 2xl:px-4 2xl:py-4 flex flex-col items-center justify-center xl:gap-y-5 2xl:gap-y-3 ">
                    <h1 className='text-2xl font-bold text-center'>Customer Support</h1>
                    <RiHeadphoneFill className="text-5xl text-blue-500 mx-auto" />
                    <div className="key-point__description xl:w-[70%] 2xl:w-[90%] mx-auto ">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas, eligendi! Culpa iste harum provident nobis modi, porro enim sunt incidunt quos maxime
                    </div>
                </div>

                <div className="key-point border-blue-600 2xl:w-96 xl:w-96 h-fit border-2 xl:px-4 xl:py-4 2xl:px-4 2xl:py-4 flex flex-col items-center justify-center xl:gap-y-5 2xl:gap-y-3 ">
                    <h1 className='text-2xl font-bold text-center'>Customer Support</h1>
                    <RiHeadphoneFill className="text-5xl text-blue-500 mx-auto" />
                    <div className="key-point__description xl:w-[70%] 2xl:w-[90%] mx-auto ">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas, eligendi! Culpa iste harum provident nobis modi, porro enim sunt incidunt quos maxime
                    </div>
                </div>

                <div className="key-point border-blue-600 2xl:w-96 xl:w-96 h-fit border-2 xl:px-4 xl:py-4 2xl:px-4 2xl:py-4 flex flex-col items-center justify-center xl:gap-y-5 2xl:gap-y-3 2xl:ml-[30%] xl:ml-[30%] ">
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