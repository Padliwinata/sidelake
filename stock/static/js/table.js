$(document).ready( function () {
    $('#example').DataTable({
        columnDefs: [
            { orderable: false, className: 'reorder', targets: 7},
            { orderable: false, className: 'reorder', targets: 8},
            ],
        lengthMenu: [[5,10,25,50,-1], [5,10,25,50, "All"]]
    });
});