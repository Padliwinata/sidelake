$(document).ready( function () {
    $('#example').DataTable({
        columnDefs: [
            { orderable: false, className: 'reorder', targets: 8},
            { orderable: false, className: 'reorder', targets: 9},
            ],
        lengthMenu: [[5,10,25,50,-1], [5,10,25,50, "All"]]
    });
});