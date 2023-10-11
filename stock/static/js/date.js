$('#date').datepicker();
$('#date2').datepicker();
    function formatDateTime(dateTime) {
        const options = {
            year: '2-digit',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        };
    return new Intl.DateTimeFormat('id-ID', options).format(dateTime);
    }

    function updateDateTime() {
        const now = new Date();
        const dateTimeElement = document.getElementById('currentTime');

        const formattedDateTime = formatDateTime(now);
        dateTimeElement.value = formattedDateTime;
    }
    updateDateTime();
    setInterval(updateDateTime, 1000);

    function formatDateTime2(dateTime) {
           const options = {
               year: '2-digit',
               month: '2-digit',
               day: '2-digit',
               hour: '2-digit',
               minute: '2-digit',
               second: '2-digit'
           };
   
           return new Intl.DateTimeFormat('id-ID', options).format(dateTime);
       }

       function updateDateTime2() {
           const now = new Date();
           const dateTimeElement = document.getElementById('currentTime2');

           const formattedDateTime = formatDateTime2(now);
           dateTimeElement.value = formattedDateTime;
       }
       updateDateTime2();
       setInterval(updateDateTime2, 1000);