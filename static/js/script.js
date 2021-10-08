(function () {
'use strict';
  $(document).ready(function() {    
    $('.main_menu').meanmenu({
      meanMenuContainer: '.heading_thum',
      meanScreenWidth: '767',
      meanRevealPosition: 'right'
    });
    $('select').niceSelect();

    $('#step-2 .step_form_select_item_cart_inner').on('click', function(){
      $('.three-column').removeClass('d-none').addClass('acitve');
    })

    $('#step-1 #next').on('click', function(e){
      e.preventDefault();
      $('#step-1').addClass('d-none')
      $('#step-2').removeClass('d-none')
    })
    $('#step-2 #next').on('click', function(e){
      e.preventDefault();
      $('#step-2').addClass('d-none')
      $('#step-3').removeClass('d-none')
    })
    $('#step-3 #next').on('click', function(e){
      e.preventDefault();
      $('#step-3').addClass('d-none')
      $('#step-4').removeClass('d-none')
    })
    $('#step-4 #next').on('click', function(e){
      e.preventDefault();
      $('#step-4').addClass('d-none')
      $('#step-5').removeClass('d-none')
    })
    
    $('#step-2 #back').on('click', function(e){
      e.preventDefault();
      $('#step-2').addClass('d-none')
      $('#step-1').removeClass('d-none')
    })
    $('#step-3 #back').on('click', function(e){
      e.preventDefault();
      $('#step-3').addClass('d-none')
      $('#step-2').removeClass('d-none')
    })
    $('#step-4 #back').on('click', function(e){
      e.preventDefault();
      $('#step-4').addClass('d-none')
      $('#step-3').removeClass('d-none')
    })
    $('#step-5 #back').on('click', function(e){
      e.preventDefault();
      $('#step-5').addClass('d-none')
      $('#step-4').removeClass('d-none')
    })



    var slider = document.getElementById("myRange");
    var output = document.getElementById("outPut");
    output.value = slider.value; // Display the default slider value
    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
      output.value = this.value;
    }


  });
})();

