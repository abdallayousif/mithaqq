$(function (){
    'use strict';
    // adjecst slider  window height
    var winH   = $(window).height(),
        
        navbarH = $('.navbar').innerHeight(),

        haderH = $('.metheqq_nile').innerHeight();
        
    $('.silder, .carousel-inner, .imge').height( winH - (navbarH));
    $('.vidslid, .navgeted').height( winH - (haderH));

    $("#shhid").click(function(){
     $('#no').toggle();
      });

    $('.contanser').slick({
        autoplay: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll:1,
        autoplaySpeed:310
   });

 // Product Slider 4 Column
 $('.product-slider-4').slick({
    autoplay: true,
    infinite: true,
    dots: false,
    slidesToShow: 4,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 4,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 3,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 2,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
            }
        },
    ]
});


// Product Slider 3 Column
$('.product-slider-3').slick({
    autoplay: true,
    infinite: true,
    dots: false,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 3,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 2,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
            }
        },
    ]
});


// Product Detail Slider
$('.product-slider-single').slick({
    infinite: true,
    autoplay: true,
    dots: false,
    fade: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    asNavFor: '.product-slider-single-nav'
});
$('.product-slider-single-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    dots: false,
    centerMode: true,
    focusOnSelect: true,
    asNavFor: '.product-slider-single'
});


// Brand Slider
$('.brand-slider').slick({
    speed: 5000,
    autoplay: true,
    autoplaySpeed: 0,
    cssEase: 'linear',
    slidesToShow: 5,
    slidesToScroll: 1,
    infinite: true,
    swipeToSlide: true,
    centerMode: true,
    focusOnSelect: false,
    arrows: false,
    dots: false,
    responsive: [
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 4,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 3,
            }
        },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 2,
            }
        },
        {
            breakpoint: 300,
            settings: {
                slidesToShow: 1,
            }
        }
    ]
});


// Review slider
$('.review-slider').slick({
    autoplay: true,
    dots: false,
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
            }
        }
    ]
});


// Widget slider
$('.sidebar-slider').slick({
    autoplay: true,
    dots: false,
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1
});


// Quantity
$('.qty button').on('click', function () {
    var $button = $(this);
    var oldValue = $button.parent().find('input').val();
    if ($button.hasClass('btn-plus')) {
        var newVal = parseFloat(oldValue) + 1;
    } else {
        if (oldValue > 0) {
            var newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 0;
        }
    }
    $button.parent().find('input').val(newVal);
});


// Shipping address show hide
$('.checkout #shipto').change(function () {
    if($(this).is(':checked')) {
        $('.checkout .shipping-address').slideDown();
    } else {
        $('.checkout .shipping-address').slideUp();
    }
});


// Payment methods show hide
$('.checkout .payment-method .custom-control-input').change(function () {
    if ($(this).prop('checked')) {
        var checkbox_id = $(this).attr('id');
        $('.checkout .payment-method .payment-content').slideUp();
        $('#' + checkbox_id + '-show').slideDown();
    }
});

// session data send to basket



  
let hex = [1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"],
    color = [];


for(let i=0; i<6; i++){
    color.push(hex[Math.floor(Math.random() * hex.length)]);
}

let finel = '#' + color.join("");

console.log(finel);

document.getElementById("call-to").style.backgroundColor = finel;





});
// java script all




