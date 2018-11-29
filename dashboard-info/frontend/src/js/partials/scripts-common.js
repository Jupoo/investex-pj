$(document).ready( function() {
    //var elem = $('.page-header');
    //var h_hght = elem.outerHeight(); // высота шапки
    var h_hght = 0;

	//Плавная прокрутка до якоря
	$(document).on('click', 'a.ancLinks', function () {
		var elementClick = $(this).attr("href");
		var destination = $(elementClick).offset().top - h_hght - 20;//минус высота шапки
		$("html:not(:animated),body:not(:animated)").animate({scrollTop: destination},500);

		return false;
	});
});