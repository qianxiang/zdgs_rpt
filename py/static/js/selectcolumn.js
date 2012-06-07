


$(document).ready(function(){
    
    hide_All_col_name();
    $("#fld_col_name").slideDown("slow");
    $(".radio_report_type").first().css({ color :  "#0000FF", "font-size": "36px" });


    $('input[name="report_type"]').bind('click', function() {
        
        $(".radio_report_type").css({ color : "", "font-size": "" });
        $(this).parent().css({ color : "#0000FF", "font-size": "36px" });


        hide_All_col_name();
        varSelecter = "#" + this.value + "_col_name";
        $(varSelecter).slideDown("slow");
        
    });
});

hide_All_col_name = function(){
    $("#fld_col_name").slideUp("slow");
    $("#sld_col_name").slideUp("slow");
    $("#jld_col_name").slideUp("slow");
    $("#lyd_col_name").slideUp("slow");
    $("#nbdbd_col_name").slideUp("slow");
    $("#rkd_col_name").slideUp("slow");
}
