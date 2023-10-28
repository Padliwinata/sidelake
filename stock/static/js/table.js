$(document).ready( function () {
    $('#example').DataTable({
        columnDefs: [
            { orderable: false, className: 'reorder', targets: 5},
            { orderable: false, className: 'reorder', targets: 6},
            ],
        lengthMenu: [[5,10,25,50,-1], [5,10,25,50, "All"]]
    });
});