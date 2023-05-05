
    $('.autoplay').slick({
        cssEase: 'linear',
         slidesToShow: 6,
         slidesToScroll: 1,
        autoplay: true,
        arrows:true,
        autoplaySpeed: 1000,
        responsive: [
          {
            breakpoint: 1200,
            settings: {
              arrows: true,
              centerMode: true,
              centerPadding: '0px',
              slidesToShow: 4
            }
            
          },
        
          {
            breakpoint: 768,
            settings: {
              arrows: true,
              centerMode: true,
              centerPadding: '0px',
              slidesToShow: 2
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

              

    $('.autoplay4').slick({
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
  
  $(document).ready(function(){
    $("#myInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myTab ").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });