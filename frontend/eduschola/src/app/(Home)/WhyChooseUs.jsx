"use client"
import Slider from "react-slick";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";

const WhyChooseUs = () => { //this is a functional slider component
    const settings = {
        dots: true,
        infinite: false,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        swipeToSlide: true,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 4000,
    };
    return ( 
        <div className="why-choose-us relative w-full px-4 mt-16 ">

            <div className="main-text mb-10 xl:mb-0 text-center ">
                    <h1 className="font-bold text-2xl ">Why Choose Us?</h1>
                    <p className="font-medium text-lg ">Don't just take our word for it. See what our satisfied customers have to say.</p>
            </div>   
            <Slider {...settings} className="reviews">
                    
                    <div className="review flex flex-col  ">
                        <div className="mb-5">
                            <div className="pic rounded-full w-32 h-32 bg-orange-500 mx-auto" />
                            <h1 className="author font-semibold text-xl text-center">Dave Gray</h1>
                        </div>
                        <p className="font-medium w-full lg:w-[70%] md:w-[70%] xl:w-[40%] 2xl:w-[40%] mx-auto">Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam a commodi vitae atque doloremque rerum maiores totam dolorum esse nemo distinctio, soluta ipsam saepe, praesentium similique animi ab facere voluptatum!</p>
                    </div>

                    <div className="review flex flex-col   ">
                        <div className="mb-5">
                            <div className="pic rounded-full w-32 h-32 bg-orange-500 mx-auto" />
                            <h1 className="author font-semibold text-xl text-center">Dave Gray</h1>
                        </div>
                        <p className="font-medium w-full lg:w-[70%] xl:w-[40%] md:w-[70%] 2xl:w-[40%] mx-auto">Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam a commodi vitae atque doloremque rerum maiores totam dolorum esse nemo distinctio, soluta ipsam saepe, praesentium similique animi ab facere voluptatum!</p>
                    </div>
            </Slider>
        </div>
     );
}
 
export default WhyChooseUs;
