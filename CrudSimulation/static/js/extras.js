
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
    var TaskMetaName = $(e.relatedTarget).data('task-name');

    $('.dynamic-content-task-warn').html(`Are you sure you want to delete this <b>${TaskMetaName}</b> Task? This action renders the data unrecoverable! Please do this
    with caution!!!`);
    $('.btn-url-receiver').attr("href", `/data/deleteSpecific/${TaskUUID}`); // ! ES6 TEMPLATE LITERAL
});