
// ! Login View with Isotope in Packery
$('.auth-grid').isotope({
    itemSelector: '.auth-item',
    layoutMode: 'packery',
    resize: true,
    packery: {
        columnWidth: '.auth-item',
        horizontal: false
    },
    sortAscending: true,
    transistion: 300,
    percentPosition: true,
});

// ! Clear Auth Credential Fields from Login Form
$('.auth-clear-entry').click(function (e) {
    $('.form-control').val('');
});
