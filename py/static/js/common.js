

//titleStr = '终端公司制单打印系统 by 陕西仟翔电子有限责任公司'
titleStr = '中国移动终端陕西公司业务单据系统 by 仟翔电子'


$(document).ready(function(){
    titleText = $('title').html();
    titleText = $.trim(titleText);
    if( titleText == '' ){
        $('title').html( titleStr );
    }


});







