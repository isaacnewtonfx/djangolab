//Tips
//Get full url
var base_url = window.location.protocol + "//" + window.location.host + "/openshiftapp/";
//var base_url = window.location.protocol + "//" + window.location.host + "/";
//alert(fullURL);

$(document).ready(function(){

    //function to load user photo on the fly
    $(document).on('change','#id_photo',null,function(){
        
        if (this.files && this.files[0])
        {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#userPhoto,#userPhoto2')
                    .attr('src', e.target.result)
                    .width(200)
                    .height(200);
            };
            reader.readAsDataURL(this.files[0]);
        }
    });


    //code to clear user photo
    $(".clrPhoto").click(function(){
        var photoiconURL = base_url + "assets/images/usericon.svg?timestamp=" + new Date().getTime();
        $("#userPhoto,#userPhoto2").attr('src',photoiconURL)
                        .width(50)
                        .height(50);

    });


    $('.js-captcha-refresh').click(function(){

        var $form = $(this).parents('form');
        var url = location.protocol + "//" + window.location.hostname + ":"
                  + location.port + "/captcha/refresh/";

                  console.log(url);

        // Make the AJAX-call
        $.getJSON(url, {}, function(json) {
            $form.find('input[name="captcha_0"]').val(json.key);
            $form.find('img.captcha').attr('src', json.image_url);
        });

        return false;


    });




    //ajax to refresh captcha img
    // $('#refreshCaptcha').click(function(){

    //     //tell user to please wait
    //     $('#refreshMsg').text("Please Wait...");

    //     //remove previous image tag from the dom
    //     $("#CaptchaImg").remove();
    //     var CaptchaImgTagURL = base_url + "general_auth/ajax_captcha";

    //     //replace with new image tag from ajax request
    //     $.get(CaptchaImgTagURL,function(img_tag){
    //         //insert new captcha image tag into the dom

    //         $("#captchaContainer").html(img_tag);
    //         $('#refreshMsg').text("Refresh Captcha");
    //     });
    // });



    $('[data-toggle=popover]').popover({
        content: $('#AccountPopoverContent').html(),
        html: true,
        placement:'bottom'

    }).click(function() {
        $(this).popover('show');
    });

    // Setup dataTable
    $("#myTable").dataTable({"aoColumns":[null,null,null,null,null,null,null,null,null]});


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



});//end of file