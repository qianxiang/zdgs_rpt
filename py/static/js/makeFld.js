//


$(document).ready(function(){

    $('#b_2').bind('click', function() {
        document.form_1.action = "skipThisOne";
        document.form_1.submit();
        
    });
});

