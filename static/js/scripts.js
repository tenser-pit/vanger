$('.slider-single').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    useTransform: true,
    asNavFor: '.slider-nav'
});
$('.slider-nav').slick({
    slidesToShow: 4.99999,
    slidesToScroll: 1,
    arrows: true,
    centerMode: true,
    loop: true,
    asNavFor: '.slider-single',
    dots: false,
    focusOnSelect: true,
    VariableWidth: true,
    responsive: [
    {
        breakpoint: 480,
        settings: {
            arrows: false,
            centerMode: true,
            slidesToShow: 3,
        }
    }
]

});
lightbox.option({
    'positionFromTop': 250,
    'maxWidth': 1000,
    'wrapAround': true
})