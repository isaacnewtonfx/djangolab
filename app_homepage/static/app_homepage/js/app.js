$(document).ready(function(){


    // Set up anything Slider
    $(function(){
        $('#slider').anythingSlider({
            theme           : 'metallic',
            easing          : 'easeInOutBack',
            expand          : true,
            autoPlay      : true,
            delay:7000,
            navigationFormatter : function(index, panel){
                return ['Slab', 'Parking Lot', 'Drive', 'Glorius Dawn', 'Bjork?', 'Traffic Circle'][index - 1];
            }
        });
    });

    // Set up textillate
    $(".mytextillate").textillate({ initialDelay: 500,in: { delay: 3, shuffle: true}, loop:true});

    // Set up cycle image slideshow
    $("#slideshow").cycle({
        fx:'fade',
        pause:1,
        speed:3000,
        prev:'#prev',
        next:'#next'
    });




})