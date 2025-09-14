document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        dateClick: function(info) {
            const dateStr = info.dateStr; // format: YYYY-MM-DD
            window.location.href = `TaskViewer.html?date=${dateStr}`;
        }

    });
    calendar.render();
});