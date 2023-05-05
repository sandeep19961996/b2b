
    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
           
            
        } else {
          $('#mobile-serch').removeClass('sticky-top shadow-sm')
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });



//    Use for js Serach
$(".anyname").chosen();

//    Use for js Text animation
        // var type=new Typed(".auto-type",{
        //   strings:["MARKET PLACE"],
        //   typeSpeed:150,
        //   backSpeed:150,
        //   loop:true
        // })
   


     

jQuery(document).ready(function(){
    jQuery(window).scroll(function(){
        if (jQuery(this).scrollTop() > 100) {
            jQuery('.back-to-top').fadeIn();
        } else {
            jQuery('.back-to-top').fadeOut(); 
    }
    });
    // scroll-to-top animate
    jQuery('.back-to-top').click(function(){
    jQuery("html, body").animate({ scrollTop: 0 }, 1500);
        return false;
    });
    });


        
        //  Sticky Navbar
  //   $(window).scroll(function () {
  //     if ($(this).scrollTop() > 45) {
  //         $('.scroll_btn').addClass('sticky-top shadow-sm');
  //     } else {
  //         $('.scroll_btn ').removeClass('sticky-top shadow-sm');
  //     }
  // });
    //=========COUNTER JS=========
    // $('.counter').countUp();
   
    //=======SELECT2======
    $(document).ready(function() {
        $('.select_2').select2();
    });


    // ===VENO BOX JS===
    // $('.venobox').venobox();


    //*==========ISOTOPE==============
    // var $grid = $('.grid').isotope({});


    //active class
    $('.wsus__location_filter button').on("click", function(event) {

        $(this).siblings('.active').removeClass('active');
        $(this).addClass('active');
        event.preventDefault();

    });


    //=========LISTING SLIDER=========
    // $('.listing_slider').slick({
    //     slidesToShow: 4,
    //     slidesToScroll: 1,
    //     autoplay: false,
    //     autoplaySpeed: 2000,
    //     dots: true,
    //     arrows: false,

    //     responsive: [{
    //             breakpoint: 1400,
    //             settings: {
    //                 slidesToShow: 4,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 1200,
    //             settings: {
    //                 slidesToShow: 3,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 992,
    //             settings: {
    //                 slidesToShow: 2,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 768,
    //             settings: {
    //                 slidesToShow: 2,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 576,
    //             settings: {
    //                 slidesToShow: 1,
    //                 slidesToScroll: 1,
    //             }
    //         }
    //     ]
    // });



    //*=====TESTIMONIAL SLIDER=====
    // $('.testi_slider').slick({
    //     slidesToShow: 2,
    //     slidesToScroll: 1,
    //     autoplay: true,
    //     autoplaySpeed: 2000,
    //     dots: true,
    //     arrows: false,

    //     responsive: [{
    //             breakpoint: 1200,
    //             settings: {
    //                 slidesToShow: 2,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 992,
    //             settings: {
    //                 slidesToShow: 1,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 768,
    //             settings: {
    //                 slidesToShow: 1,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 576,
    //             settings: {
    //                 slidesToShow: 1,
    //                 slidesToScroll: 1,
    //             }
    //         }
    //     ]
    // });


  
    // $(window).on('scroll', function() {
    //     var scrolling = $(this).scrollTop();

    //     if (scrolling > 300) {
    //         $('.scroll_btn').fadeIn();
    //     } else {
    //         $('.scroll_btn').fadeOut();
    //     }
    // });


    //=========ABOUT PAGE SLIDER=========
    // $('.about_page_slider').slick({
    //     slidesToShow: 6,
    //     slidesToScroll: 1,
    //     autoplay: true,
    //     autoplaySpeed: 2000,
    //     dots: false,
    //     arrows: false,


    //     responsive: [{
    //             breakpoint: 1200,
    //             settings: {
    //                 slidesToShow: 4,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 992,
    //             settings: {
    //                 slidesToShow: 3,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 768,
    //             settings: {
    //                 slidesToShow: 3,
    //                 slidesToScroll: 1,
    //             }
    //         },
    //         {
    //             breakpoint: 576,
    //             settings: {
    //                 slidesToShow: 2,
    //                 slidesToScroll: 1,
    //             }
    //         }
    //     ]
    // });


    // ==========SUMMER NOTE JS==========
    // $(document).ready(function() {
    //     $('.summer_note').summernote();
    // });


  
 
$('.autoplay2').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
        {
          breakpoint: 768,
          settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '40px',
            slidesToShow: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '40px',
            slidesToShow: 1
          }
        },
       
      ]
  });     

  $('.autoplay3').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
        {
          breakpoint: 768,
          settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '0px',
            slidesToShow: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '0px',
            slidesToShow: 1
          }
        },
       
      ]
  });  

  // block mouse right click 
//   document.addEventListener("contextmenu", (event) => {
//     event.preventDefault();
//  });


// var prevScrollpos = window.pageYOffset;
// window.onscroll = function() {
// var currentScrollPos = window.pageYOffset;
//   if (prevScrollpos > currentScrollPos) {
//     document.getElementById("mobile-serch").style.top = "90px";
//   } else {
//     document.getElementById("mobile-serch").style.top = "-100px";
//   }
//   prevScrollpos = currentScrollPos;
// }

window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.documentElement.scrollTop > 50) {
    document.getElementById("mobile-serch").style.top = "-100px";
  } else {
    document.getElementById("mobile-serch").style.top = "90px";
  }
}

$(document).ready(function(){
  $(".menuIcon").on("click", function(){
    $(this).toggleClass("active");
    $(".sideMenu").toggleClass("active");
  });
});