// Initialize and add the map
function initMap() {
    // The location of Uluru
    const uluru = { lat: 15.621339, lng: 32.533831 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: uluru,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: uluru,
      map: map,
    });
  }



  $(window).scroll(function() {

    if (visible($('.count-digit'))) {
        if ($('.count-digit').hasClass('counter-loaded')) return;
        $('.count-digit').addClass('counter-loaded');

        $('.count-digit').each(function() {
            var $this = $(this);
            jQuery({
                Counter: 0
            }).animate({
                Counter: $this.text()
            }, {
                duration: 3000,
                easing: 'swing',
                step: function() {
                    $this.text(Math.ceil(this.Counter));
                }
            });
        });
    }
});


var form = document.getElementById('comment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    
        var custName = document.getElementById("inputFirstName").value;
        var custAdd = document.getElementById("inputLastName").value;
        var custAdd2 = document.getElementById("inputEmail").value;
        var postCode = document.getElementById("message").value;


        
      $.ajax({
        type: "POST",
        url: 'https://mithaqq.herokuapp.com//metheqq_root/send/',
        dataType: 'json',
        data: {
          fristname: custName,
          lastname: custAdd,
          email: custAdd2,
          message: postCode,
          csrfmiddlewaretoken: CSRF_TOKEN,
          action: "post",
        },

        success: function (json) {
            console.log(message)
        },
    });
});