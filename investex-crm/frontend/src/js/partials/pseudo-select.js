$(document).ready( function() {
	//Клик вне селекта
    if ($(".pseudo-select").length) {
        $(document).click(function (e) {
            if ($(e.target).closest(".pseudo-select").length) {
                return;
            }
            else {
                $(".pseudo-select__list").removeAttr("style");
                $(".pseudo-select").removeClass("pseudo-select--active");
            }
            e.stopPropagation();
        });
    }
	
	//Раскрытие списка
	$(document).on("click", ".pseudo-select__control", function () {
		var wrap = $(this).closest(".pseudo-select");

		var openSelect = "no";
		if(wrap.hasClass("pseudo-select--active")) {
			openSelect = "yes";
		}

		$(".pseudo-select").removeClass("pseudo-select--active");
		$(".pseudo-select__list").removeAttr("style");

		if(openSelect == "yes") {
			wrap.removeClass("pseudo-select--active");
			wrap.find(".pseudo-select__list").removeAttr("style");
		} else {
			wrap.addClass("pseudo-select--active");
			wrap.find(".pseudo-select__list").css("display","block");
		}
	});

    //Клик по элементу списка
	$(document).on("click", ".pseudo-select__option", function () {
		var el = $(this);
		var select_wrap = el.closest(".pseudo-select");
		var select_text = el.text();
		var data_value = el.attr("data-value");
		
		select_wrap.find(".pseudo-select__option").removeClass("current");
		el.addClass("current");
		select_wrap.find(".pseudo-select__text").text(select_text);
		select_wrap.find(".pseudo-select__list").removeAttr("style");
		
		select_wrap.find('.pseudo-select__real option').removeAttr("selected");
		select_wrap.removeClass("pseudo-select--active");
		select_wrap.find('.pseudo-select__real option[value="'+data_value+'"]').attr("selected","selected").change();
		select_wrap.find('.pseudo-select__real').val(data_value);
	});

	$(document).on("change", ".pseudo-select__real", function () {
		var el = $(this);
		var select_val = el.val();
		var select_wrap = el.closest(".pseudo-select");

		if(select_val != select_wrap.find(".pseudo-select__option.current").attr("data-value")) {
			var select_text = el.find("option[value='"+select_val+"']").text();
			select_wrap.find('.pseudo-select__real option[value="'+select_val+'"]').attr("selected","selected");
			select_wrap.find(".pseudo-select__option").removeClass("current");
			select_wrap.find(".pseudo-select__option[data-value='"+select_val+"']").addClass("current");
			select_wrap.find(".pseudo-select__text").text(select_text);
		}
    });
});