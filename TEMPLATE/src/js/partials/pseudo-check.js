$(document).ready( function() {
	//Псеудочекбокс
    $(document).on("change", ".pseudo-check__real", function () {
        var el = $(this);
        var wrap = el.closest(".pseudo-check");
        if(el.prop("checked") == true) {
            wrap.addClass("check");
        } else {
            wrap.removeClass("check");
        }
    });
});