choices = ""

$(document).ready(function(){
    $.each(info["answers"], function(i, ans){
        let new_answer= $("<button type='button' class='ans_option'>"+ans+"</button>")
        $("#answer_choices").append(new_instructor)
    })

    $(".ans_option").click(function(){     
        console.log("picked option")
        console.log(".ans_option").val())
    })