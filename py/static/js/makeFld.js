//
// 倒计时 模块   包括两个全局变量，两个函数
var COUNT_DOWN_TIME = 5;
var COUNT_DOWN_ELEMENT = '';
var COUNT_DOWN_TIMER;
function addCountDown( delay, elementId ){
    if( delay < 1 ){
        COUNT_DOWN_TIME = 5;
    }
    else {
        COUNT_DOWN_TIME = delay;
    }
    
    COUNT_DOWN_ELEMENT = document.getElementById( elementId );
    if( COUNT_DOWN_ELEMENT  ){
        showCountDown();
    }
}

function delCountDown(){
    clearTimeout(COUNT_DOWN_TIMER);       
}

// 私有函数，不许直接调用
function showCountDown(){
  if ( COUNT_DOWN_TIME > -1 ){
      COUNT_DOWN_ELEMENT.innerHTML='' + COUNT_DOWN_TIME;
      COUNT_DOWN_TIME--;
      COUNT_DOWN_TIMER = setTimeout('showCountDown()', 1000);
  }
  else{
      document.form_1.submit();
  }
}

// 倒计时 模块 END

checkAutoMode = function( elem ){
    if( elem.checked ){
        $('#countdownText').show();
        addCountDown(5, 'countdown');
    }
    else{
        delCountDown();
        $('#countdownText').hide();
    }
}



$(document).ready(function(){

    $('#b_2').bind('click', function() {
        document.form_1.action = "skipThisOne";
        document.form_1.submit();
    });

    $('#automode').bind('click', function() {
        checkAutoMode( this );
    });

    checkAutoMode( $('#automode').get(0) );

});

