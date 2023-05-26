import { RiHeadphoneFill } from 'react-icons/ri';
const CompanyOverview = () => {
    return ( 
        <div className="xl:mt-[2%] px-4 py-2 company-overview">
            <div className="company-overview__texts text-center flex flex-col xl:gap-y-6">
                <h1 className="company-overview__title xl:text-2xl font-semibold">The Ultimative Intuitive And User-Friendly Education Management Solution</h1>

                <h1 className="company-overview__subtitle xl:w-[95%]">
                    Eduschola provides a comprehensive and user-friendly solution for managing all aspects of your educational platform. From admissions and student records to academic planning and financial management, our platform streamlinnes your daily operations and frees up your time to focus what really matters: providingquality education to your students
                </h1>
            </div>

            <div className="company-overview__key-points xl:mt-[10%] ">
                <div className="key-point border-blue-600 border-2 px-4 py-2 flex-col items-center justify-center gap-y-5  ">
                    <h1 className='text-2xl font-bold text-center'>Customer Support</h1>
                    <RiHeadphoneFill className="text-5xl text-blue-500 mx-auto" />
                    <div className="key-point__description xl:w-[60%] mx-auto ">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas, eligendi! Culpa iste harum provident nobis modi, porro enim sunt incidunt quos maxime
                    </div>
                </div>
            </div>
        </div>
     );
}
 
export default CompanyOverview;