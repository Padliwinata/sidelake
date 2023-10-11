$(document).ready(function() {
    $(".edit-stock-button").click(function() {
      var stockId = $(this).data("stock-id");
      var editUrl = "{% url 'edit-stock' 0 %}".replace("0", stockId);
      
      // Mengisi formulir modal dengan data stok yang akan diedit
      $.get(editUrl, function(data) {
        $("#editStockModal .modal-body").html(data);
        $("#editStockModal").modal("show");
      });
    });

    // Mengirim data stok yang diedit ke server melalui AJAX
    $("#editStockForm").submit(function(event) {
      event.preventDefault();
      var formData = $(this).serialize();
      var editUrl = "{% url 'edit-stock' 0 %}".replace("0", stockId);

      $.ajax({
        url: editUrl,
        type: "POST",
        data: formData,
        success: function(response) {
          // Tanggapi respon jika diperlukan
          $("#editStockModal").modal("hide");
          // Refresh halaman atau perbarui tampilan sesuai kebutuhan
        },
        error: function(error) {
          // Tanggapi kesalahan jika diperlukan
        }
      });
    });
  });