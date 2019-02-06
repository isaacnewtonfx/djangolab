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
        var photoiconURL = base_url + "static/app_users/img/usericon.svg?timestamp=" + new Date().getTime();
        $("#userPhoto,#userPhoto2").attr('src',photoiconURL)
                        .width(50)
                        .height(50);
    
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
    
    
    
    });