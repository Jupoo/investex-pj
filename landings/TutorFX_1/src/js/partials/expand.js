$(document).ready( function() {
	//---------Разворачивание скрытого контента по кнопке-------------//
	$(document).on('click', '.js-expand-btn', function () {
		var btn = $(this);

        btn_body =  $(".js-expand-body");

        btn_body.slideToggle("400", function () {
            if(btn.hasClass('active')) {
                btn.removeClass('active');
            }
            else {
                btn.addClass('active');
            }

            if(btn_body.css("display") == "block") {
                var destination = btn_body.offset().top;
                $("html:not(:animated),body:not(:animated)").animate({scrollTop: destination},500);
            }
        });

        return false;
    });
});