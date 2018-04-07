$(function(){
    $("#dashboard").click(dashboard);
    $("#sections").click(section_event);
    $("#history").click(history_event);
});

function dashboard(event){
    event.preventDefault();
    bar_user = "<div class='row'><div class ='col-10 content'><h6>Send one of this links to librarian</h6></div></div>";
    $(".main").html(bar_user);
    refresh_statistic();
    $("#show_statistics").click(show_statistics);
}

function statistics(){
    
}

function section_event(event){

}

function history_event(event){

}

function invite_links(){
    $.post("/api/get_verification_links",{},function(data,status){
        output_html = "<div class='row'><div class='col-3'><h3>Send one of this links to librarian</h3></div></div>";
        data.forEach(elem => {
            output_html += elem + "</br>";
        });
        $(".content").html(output_html);
        feather.replace();
        $("#add").click(generate_link);
    });
}

function generate_link(){
    $.post("/api/generate_invite_link",{},function (data,status){
        invite_links();
    });
}
