window.onload = function() {
            let today = new Date().toISOString().split('T')[0];
            document.getElementById("date").value = today;
        };