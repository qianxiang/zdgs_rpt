//

nextOne = function(){ 
    document.form_1.submit();
}

$(document).ready(function(){
    flag = $('input[name="automode"]').get(0).value;
    if(flag=='y'){
        setTimeout('nextOne()', 5000);
    }
});

