
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

$('#actionDeleteSelectedData').on('show.bs.modal', function (e) {
    var TaskUUID = $(e.relatedTarget).data('task-id');
    var TaskMetaName = $(e.relatedTarget).data('task-name');
    console.log(e)

    $('.dynamic-content-task-warn').html(`Are you sure you want to delete this <b>${TaskMetaName}</b> Task? This action renders the data unrecoverable! Please do this
    with caution!!!`);
    $('.btn-url-receiver').attr("href", `/data/deleteSpecific/${TaskUUID}`); // ! ES6 TEMPLATE LITERAL
});

function clearModalContent() {
    return $('.form-control').val("");
}

$('#actionModifyData').on('show.bs.modal', function (e) {
    clearModalContent();
    var TaskUUID = $(e.relatedTarget).data("task-id");
    $(`tr.${TaskUUID}`).addClass("selected-data");
    $('#modifyDataTaskName').val($(".selected-data").children("#taskName").text());
    $("select#modifyDataTaskType option[value='" + $(".selected-data").children("#taskType").html() + "']").prop("selected", true);
    $('#modifyTaskDescription').val($(".selected-data").children("#taskDescription").text());

    $('#taskReference').attr("value", TaskUUID);

    startTime = new Date (($(".selected-data").children("#taskStartTime").text().replace(".", "").replace(".", "").replace(".", "") + " GMT")).toISOString().replace(":00.000Z", "");
    $('#modifyTaskStartTime').val(startTime);
    endTime = new Date (($(".selected-data").children("#taskEndTime").text().replace(".", "").replace(".", "").replace(".", "") + " GMT")).toISOString().replace(":00.000Z", "");
    $('#modifyTaskEndTime').val(endTime);

    console.log("startTime > ",startTime);
    console.log("endTime > ",endTime);

});

$('.cancel-modify-data').click(() => {
    $('tr').removeClass('selected-data');
});

$('#dismissableModalConfirm').click(() => {
    $('#actionExportData').modal('hide');
});