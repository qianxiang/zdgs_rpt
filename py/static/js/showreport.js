//

nextOne = function(){ 
    //alert('');
    $('#nextOne').get(0).click();
}

$(document).ready(function(){
    flag = $('input[name="automode"]').get(0).value;
    if(flag=='y'){
        setTimeout('nextOne()', 5000);
    }
});

