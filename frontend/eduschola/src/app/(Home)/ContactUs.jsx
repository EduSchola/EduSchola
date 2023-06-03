import { MdLocationOn } from 'react-icons/md';
import { BsTelephoneFill } from 'react-icons/bs';
import { AiFillMail } from 'react-icons/ai';
const ContactUs = () => {
    return ( 
        <div className="relative w-full px-4">
            <h1 className="text-center text-2xl font-bold mb-4">Contact Us</h1>

            <div className='lg:flex-row xl:flex-row 2xl:flex-row gap-x-32 flex flex-col gap-y-20'>
                <div className="contact-details flex flex-col 2xl:ml-80  gap-y-12 gap-x-32 md:mx-auto ">

                    <div className="flex gap-x-6">
                        <MdLocationOn className="text-blue-500 text-3xl" />
                        <h1>Plot 54, Saint Anthony Layout, High Fashion Industrial Estate</h1>
                    </div>

                    <div className="flex gap-x-6">
                        <BsTelephoneFill className="text-blue-500 text-2xl" />
                        <h1>+12345678901</h1>
                    </div>

                    <div className="flex gap-x-6">
                        <AiFillMail className="text-blue-500 text-2xl" />
                        <h1>eduschola@gmail.com</h1>
                    </div>
                </div>

                <form className="text-center flex flex-col gap-y-8 md:mx-auto">
                    <h1 className='text-lg font-semibold'>Get In Touch And Leave A Message For Us</h1>
                    <input type="email" name="email" id="email" className=' h-10 w-96 border-2 border-gray-600 rounded-md px-4 py-2' placeholder='Email'  />
                    <input type="email" name="email" id="email" className=' h-10 w-96 border-2 border-gray-600 rounded-md px-4 py-2' placeholder='Email'  />
                    <button type="submit" className='w-96 h-10 text-white bg-blue-700 rounded-md px-4 py-2 font-medium '>Send Message</button>
                </form>
            </div>
        </div>
     );
}
 
export default ContactUs;