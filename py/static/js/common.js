

chagePic = function(){
    //alert("def");
    if( index < pics.length ){
        $("#pic_1").attr("src", pics[index]);
        index = index + 1;
    }
    else{
        //clearInterval( fun_name );
        index = 0;
    }
}



