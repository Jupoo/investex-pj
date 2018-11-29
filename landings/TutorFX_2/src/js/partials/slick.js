$(document).ready( function() {
	$('.js-gal').slick({
		dots: false,
		infinite: true,
		speed: 300,
		slidesToShow: 6,
		slidesToScroll: 6,
		arrows: false,
		responsive: [
			{
				breakpoint: 1200,
				settings: {
					slidesToShow: 4,
					slidesToScroll: 2,
					infinite: true,
					dots: true,
					arrows: false
				}
			},
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 4,
					slidesToScroll: 2,
					infinite: true,
					dots: true,
					arrows: false
				}
			},
			{
				breakpoint: 768,
				settings: {
					slidesToShow: 3,
					slidesToScroll: 2,
					infinite: true,
					dots: true,
					arrows: false
				}
			},
			{
				breakpoint: 576,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 2,
					infinite: true,
					dots: true,
					arrows: false
				}
			}
		]
	});
});