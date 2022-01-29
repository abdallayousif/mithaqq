var stripe = Stripe('pk_test_51JmCOqDLOcBRlRS7HK7pVTDrHXxtAOgXZof7eNeIUOkE9rRRAVa1MoYuW6XfdkYz6yr7gzdkauTKhvnclJpDjdTi00MZBLwF6a');

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
base: {
  color: "#000",
  lineHeight: '2.4',
  fontSize: '16px'
}
};





var form = document.getElementById('payment-form');


form.addEventListener('submit', function(ev) {
ev.preventDefault();



    var active2 = document.getElementById("payment_code").value;
    var active = document.getElementById("show");

  console.log(active.value);


     alert(active2);
     $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/orders/add2/',
        data: {
          config: active2,
          order_key: clientsecret,
          csrfmiddlewaretoken: CSRF_TOKEN,
          action: "main",
        },
        success: function (data) {
          console.log(data);
          if(data.is_taken){
            window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
          };
          if(data.is_nottaken){
            alert('كود الشراء خطا');
          }
        },
      });
    });
 