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
        output_html = "<button class='btn btn-sm' id='prev'><span data-feather='arrow-left'><span><button>";
        console.log(data)
        $(".main").html(output_html);
        $("#prev").click(sections);
        feather.replace();
    });
}

function external_statistics(event) {
    event.preventDefault();
}