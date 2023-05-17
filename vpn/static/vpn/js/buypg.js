var extra_wage = 3;
var arraypricelist = [300000, 500000, 900000, 450000, 750000, 1400000, 600000, 900000, 1600000, 2500000];
var arrayids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var discount_rate = 0;
var $radios = $('input:radio[name=selected_service]');
var buy_option_selected = 1;
var time_expire = 0;
var time_total = 0;

var transid = "";

function pf(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
if ($radios.is(':checked') === false) {
    $radios.filter('[value=' + buy_option_selected + ']').prop('checked', true);
    $('#trproduct_' + buy_option_selected).removeClass("bg-info").addClass("bg-info");
    if (extra_wage === 0) {
        $("#finalprice").text(pf((arraypricelist[buy_option_selected] * (100.0 - discount_rate) / 100.0)) + " تومان");
    } else {
        $("#finalprice").text(pf((arraypricelist[buy_option_selected] * (100.0 - discount_rate + extra_wage) / 100.0)) + " تومان" + " ( " + extra_wage + " % کارمزد درگاه واسط)");
    }
    $("#finalpricetron").text(pf(arraypricelist[buy_option_selected] * 0.8) + " تومان");
}

function reply_click(i) {
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
        $("#finalprice").text(pf((arraypricelist[i] * (100.0 - discount_rate) / 100.0)) + " تومان");
    } else {
        $("#finalprice").text(pf((arraypricelist[i] * (100.0 - discount_rate + extra_wage) / 100.0)) + " تومان" + " ( " + extra_wage + " % کارمزد درگاه واسط)");
    }

    $("#finalpricetron").text(pf(arraypricelist[i] * 0.8) + " تومان");
}

function CopyCB(in_mode) {
    var in_copy_str = "";
    if (in_mode == "address") {
        in_copy_str = $("#crypto_address").val();
    } else if (in_mode == "amount") {
        in_copy_str = $("#crypto_amount").val();
    }
    var elem = document.createElement("textarea");
    document.body.appendChild(elem);
    elem.value = in_copy_str;
    elem.select();
    document.execCommand("copy");
    document.body.removeChild(elem);
}



var updatefunc = function () {
    if ($('#cryptopaymentModal').hasClass('show')) {
        if (time_expire > 100) {
            var timenow = Math.round((new Date()).getTime() / 1000);
            if (time_expire > timenow) {
                var remainsec = time_expire - timenow;
                var percent = Math.round(remainsec / time_total * 100);
                var s = new Date(remainsec * 1000).toISOString().substr(11, 8);

                $("#timeleft").text(s);
                $('#progressbarwaittime').css('width', percent + '%').attr('aria-valuenow', percent);

                if (timenow % 10 == 3) {
                    $.ajax({
                        type: "POST",
                        url: "/cryptopaymentappi_ewbdk3wkigju2w3dkgjwyedgkjusfkau32/",
                        data: JSON.stringify({
                            req: "inquiry",
                            tid: transid
                        }),
                        headers: {
                            'X-CSRFToken': 'c1hCuY8c96mibu8Vyn97FGTYxYOT9hMSuXDem3hTe2Cnt9FJYTntQlFwWeMn0eNx'
                        },
                        success: function (d) {
                            if (d.status_ok.trim() === "ok") {

                                $("#p1").hide();
                                $("#p2").hide();
                                $("#p3").hide();
                                $("#p4").hide();
                                $("#crypto_qrcode_img").attr("src", "data:image/png;base64,");
                                $("#crypto_qrcode_img").hide();

                                $("#cryptodesc").text('تبریک! تراکنش شما با موفقیت دریافت و اکانت شما شارژ گردید');
                                // $("#cryptodesc").hide();

                                $("#statustext").text(d.status_str);
                                $("#cryptostatusbtn").removeClass("btn-outline-primary").addClass("btn-success");

                                $("#cryptostatusbtn").prop('name', 'data');
                                $("#cryptostatusbtn").prop('value', d.deliver_post_data);
                                $('#cryptostatusbtn').prop('type', "submit");

                                $("#formpost").prop('action', d.deliver_action_url);

                                clearInterval(updatefunc_timer);

                                const audio = new Audio('https://v5gnet.shop/static/sound/arrow.wav');
                                audio.play();
                            }
                        },
                        error: function (errMsg) { }
                    });
                }
            } else {
                $("#timeleft").text("expired!");
            }
        }
    }
}
var updatefunc_timer = setInterval(updatefunc, timeout = 1000);

function cryptopay(name) {
    $("#cryptopaymentModal").modal({
        backdrop: "static ",
        keyboard: false
    }, "show");


    $("#statustext").text('updating...');
    $("#crypto_address").val('');
    $("#crypto_amount").val('');
    $("#cryptodesc").text('');
    $("#crypto_qrcode_img").attr("src", "data:image/png;base64,");
    time_expire = 0;
    time_total = 0;

    $.ajax({
        type: "POST",
        url: "/cryptopaymentappi_ewbdk3wkigju2w3dkgjwyedgkjusfkau32/",
        data: JSON.stringify({
            req: "make",
            currency: name,
            id: arrayids[buy_option_selected]
        }),
        headers: {
            'X-CSRFToken': 'c1hCuY8c96mibu8Vyn97FGTYxYOT9hMSuXDem3hTe2Cnt9FJYTntQlFwWeMn0eNx'
        },
        success: function (d) {
            if (d.s.trim() === "makeok") {
                $('#cryptostatusbtn').prop('type', "button");

                $("#statustext").text(d.status_str);
                $("#cryptodesc").text(d.desc);
                $("#crypto_address").val(d.wallet_address);
                $("#crypto_amount").val(d.amount);
                $("#crypto_qrcode_img").attr("src", "data:image/png;base64," + d.qrcode);

                time_expire = d.time_expire;
                time_total = time_expire - d.time_start;
                transid = d.transid;

            }
        },
        error: function (errMsg) { }
    });

}