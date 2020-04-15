
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

$('#actionDeleteSelectedData').on('show.bs.modal', function(e) {
    var TaskUUID = $(e.relatedTarget).data('task-id');
    $('.btn-url-receiver').attr("href", `/data/deleteSpecific/${TaskUUID}`); // ! ES6 TEMPLATE LITERAL
});