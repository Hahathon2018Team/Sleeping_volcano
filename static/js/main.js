$(function() {
    $("#history").click(history);
    $("#sections").click(sections);
    $("#external_statistics").click(external_statistics);
});

function history(event) {
    event.preventDefault();
    $.post("/api/history",{},function(data,status) {
        output_html = "<h3>История оповещений</h3><div class='row'><div class='col-12'><input id='search' class='form-control w-100' placeholder='Search' aria-label='Search' type='text'></div></div>\
        <div class='table-responsive'>\
            <table class='table table-striped table-sm'>\
                <thead>\
                        <th>Время</th>\
                        <th>Пункт</th>\
                        <th>Состояние</th>\
                </thead>\
                <tbody id='tbody'>";
        data.forEach(elem => {
            output_html += "<tr id = '"+ elem[1]+"'>";
            output_html += "<td>" + elem[0] + "</td>";
            output_html += "<td>" + elem[1] + "</td>";
            output_html += "<td>" + elem[2] + "</td></tr>";
        });
        output_html += "</tbody></table></div>";
        $(".main").html(output_html);

        $("#search").on("keyup", function() {
            var value = $(this).val().toLowerCase();
            console.log(value);
            $("#tbody tr").filter(function() {
              $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
          });
    });
}

function sections(event) {
    event.preventDefault();
    $.post("/api/status_of_sections", {},function (data,status){
        output_html = "<h3>Участки сети</h3><div class='row'><div class='col-12'><input id='search' class='form-control w-100' placeholder='Search' aria-label='Search' type='text'></div></div>\
        <div class='table-responsive'>\
            <table class='table table-striped table-sm'>\
                <thead>\
                        <th>Пункт</th>\
                        <th>Состояние</th>\
                        <th></th>\
                </thead>\
                <tbody id='tbody'>";
        data.forEach(elem => {
            output_html += "<tr id = '"+ elem[0]+"'>";
            output_html += "<td>" + elem[0] + "</td>";
            output_html += "<td>" + elem[1] + "</td>";
            output_html += "<td><button class='btn btn-sm info'><span data-feather='info'></span></button></td></tr>";
        });
        output_html += "</tbody></table></div>";
        $(".main").html(output_html);

        $(".info").click(info);

        $("#search").on("keyup", function() {
            var value = $(this).val().toLowerCase();
            $("#tbody tr").filter(function() {
              $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
        });
        feather.replace();
    });
}

function info() {
    section_id_ = $(this).parent().parent().attr("id")
    $.post("/api/section_statistics", {section_id:section_id_}, function (data,status) {
        output_html = "<div class ='row'><div class='col-1'><button class='btn btn-sm' id='prev'><span data-feather='arrow-left'><span><button></div><div class='col-auto offset-2'><h3>"+section_id+"</h3></div></div>";
        output_html += "<div class='row'><div class='col'><h5>Входная температура</h5><canvas class='my-4 chartjs-render-monitor charts' id='inputTemp' style='display: block;'></canvas></div><div class='col'><h5>Выходная температура</h5><canvas class='my-4 chartjs-render-monitor charts' id='outputTemp' style='display: block;'></canvas></div></div>";
        output_html += "<div class='row'><div class='col'><h5>Входное давление</h5><canvas class='my-4 chartjs-render-monitor charts' id='inputPressure' style='display: block;'></canvas></div><div class='col'><h5>Выходное давление</h5><canvas class='my-4 chartjs-render-monitor charts' id='outputPressure' style='display: block;'></canvas></div></div>";
        output_html += "<div class='row'><div class='col'><h5>Входной поток</h5><canvas class='my-4 chartjs-render-monitor charts' id='inputFlow' style='display: block;'></canvas></div><div class='col'><h5>Входной поток</h5><canvas class='my-4 chartjs-render-monitor charts' id='outputFlow' style='display: block;'></canvas></div></div>";
        $(".main").html(output_html);
        $("#prev").click(sections);
        feather.replace();
        var ctxInputTemp = document.getElementById("inputTemp");
        var inputTemp = new Chart(ctxInputTemp, {
            type: 'line',
            data: {
            labels: data[0][0],
            datasets: [{
                data: data[0][1],
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#007bff',
                borderWidth: 4,
                pointBackgroundColor: '#007bff'
            }]
            },
            options: {
            scales: {
                yAxes: [{
                ticks: {
                    beginAtZero: false
                }
                }]
            },
            legend: {
                display: false,
            }
            }
        });
        var ctxOutputTemp = document.getElementById("outpuptTemp");
        var outputTemp = new Chart(ctxOutputTemp, {
            type: 'line',
            data: {
            labels: data[1][0],
            datasets: [{
                data: data[1][1],
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#007bff',
                borderWidth: 4,
                pointBackgroundColor: '#007bff'
            }]
            },
            options: {
            scales: {
                yAxes: [{
                ticks: {
                    beginAtZero: false
                }
                }]
            },
            legend: {
                display: false,
            }
            }
        });
        var ctxInputPressure = document.getElementById("inputPressure");
        var inputPressure = new Chart(ctxInputPressure, {
            type: 'line',
            data: {
            labels: data[2][0],
            datasets: [{
                data: data[2][1],
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#007bff',
                borderWidth: 4,
                pointBackgroundColor: '#007bff'
            }]
            },
            options: {
            scales: {
                yAxes: [{
                ticks: {
                    beginAtZero: false
                }
                }]
            },
            legend: {
                display: false,
            }
            }
        });
        var ctxOutputPressure = document.getElementById("outputPressure");
        var outptuPressure = new Chart(ctxOutputPressure, {
            type: 'line',
            data: {
            labels: data[3][0],
            datasets: [{
                data: data[3][1],
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#007bff',
                borderWidth: 4,
                pointBackgroundColor: '#007bff'
            }]
            },
            options: {
            scales: {
                yAxes: [{
                ticks: {
                    beginAtZero: false
                }
                }]
            },
            legend: {
                display: false,
            }
            }
        });
        var ctxInputFlow = document.getElementById("inputFlow");
        var inputFlow = new Chart(ctxInputFlow, {
            type: 'line',
            data: {
            labels: data[4][0],
            datasets: [{
                data: data[4][1],
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#007bff',
                borderWidth: 4,
                pointBackgroundColor: '#007bff'
            }]
            },
            options: {
            scales: {
                yAxes: [{
                ticks: {
                    beginAtZero: false
                }
                }]
            },
            legend: {
                display: false,
            }
            }
        });
        var ctxOutputFlow = document.getElementById("outputFlow");
        var outputFlow = new Chart(ctxOutputFlow, {
            type: 'line',
            data: {
            labels: data[4][0],
            datasets: [{
                data: data[4][1],
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#007bff',
                borderWidth: 4,
                pointBackgroundColor: '#007bff'
            }]
            },
            options: {
            scales: {
                yAxes: [{
                ticks: {
                    beginAtZero: false
                }
                }]
            },
            legend: {
                display: false,
            }
            }
        });
    });
}

function external_statistics(event) {
    event.preventDefault();
}