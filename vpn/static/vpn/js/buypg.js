var extra_wage = 3;
var discount_rate = 0;
var $radios = $('input:radio[name=selected_service]');
var buy_option_selected = 1;


function pf(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
if ($radios.is(':checked') === false) {
    $radios.filter('[value=' + buy_option_selected + ']').prop('checked', true);
    $('#trproduct_' + buy_option_selected).removeClass("bg-info").addClass("bg-info");
    if (extra_wage === 0) {
        $("#finalprice").text(pf((buy_option_selected * (100.0 - discount_rate) / 100.0)) + " تومان");
    } else {
        $("#finalprice").text(pf((buy_option_selected * (100.0 - discount_rate + extra_wage) / 100.0)) + " تومان" + " ( " + extra_wage + " % کارمزد درگاه واسط)");
    }
    $("#finalpricetron").text(pf(buy_option_selected * 0.8) + " تومان");
}

function reply_click(i,t) {
    var idx;
    buy_option_selected = i;
    for (idx = 0; idx <= 10; idx++) {
        $('#trproduct_' + idx).removeClass("bg-info");
    }
    var $radios = $('input:radio[name=selected_service]');
    $radios.filter('[value=' + i + ']').prop('checked', true);
    $('#trproduct_' + i).removeClass("bg-info").addClass("bg-info");
    $(".serviceselection").val(i);
    if (extra_wage === 0) {
        $("#finalprice").text(pf((t * (100.0 - discount_rate) / 100.0)) + " تومان");
    } else {
        $("#finalprice").text(pf((t * (100.0 - discount_rate + extra_wage) / 100.0)) + " تومان" + " ( " + extra_wage + " % کارمزد درگاه واسط)");
    }

    $("#finalpricetron").text(pf(t * 0.8) + " تومان");
}
