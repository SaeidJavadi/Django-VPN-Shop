var extra_wage = 3; // extra fee percentage
var discount_rate = 0; // discount rate percentage
var $radios = $('input:radio[name=selected_service]');
var buy_option_selected = 0;

// Function to format numbers with commas
function pf(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// If no service is selected, select the default option
if ($radios.is(':checked') === false) {
    $radios.filter('[value=' + buy_option_selected + ']').prop('checked', true);
    $('#trproduct_' + buy_option_selected).removeClass("bg-info").addClass("bg-info");

    if (extra_wage === 0) {
        $("#finalprice").text(pf((buy_option_selected * (100.0 - discount_rate) / 100.0)) );
    } else {
        $("#finalprice").text(pf((buy_option_selected * (100.0 - discount_rate + extra_wage) / 100.0))  + " ( " + extra_wage + " % gateway fee)");
    }
    $("#finalpricetron").text(pf(buy_option_selected * 0.8) );
}

// Function called when a service option is clicked
function reply_click(i, t) {
    var idx;
    buy_option_selected = i;

    // Remove highlight from all rows
    for (idx = 0; idx <= 10; idx++) {
        $('#trproduct_' + idx).removeClass("bg-info");
    }

    // Select the clicked radio button
    var $radios = $('input:radio[name=selected_service]');
    $radios.filter('[value=' + i + ']').prop('checked', true);
    $('#trproduct_' + i).removeClass("bg-info").addClass("bg-info");
    $(".serviceselection").val(i);

    // Update final price
    if (extra_wage === 0) {
        $("#finalprice").text(pf((t * (100.0 - discount_rate) / 100.0)) );
    } else {
        $("#finalprice").text(pf((t * (100.0 - discount_rate + extra_wage) / 100.0))  + " ( " + extra_wage + " % gateway fee)");
    }

    // Update Tron price
    $("#finalpricetron").text(pf(t * 0.8) );
}
