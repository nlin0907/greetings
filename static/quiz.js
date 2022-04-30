function goToNext(total_points, idx){
    info["points"] = total_points
    curridx = idx
    if(parseInt(info["next_question"])==-1){
        goToResults(total_points);
    }
    else{
        console.log(info)
        submit_question(info)
    }
}

function goToResults(points){
    new_num = info["next_question"]
        $.ajax({
            type: "POST",
            url: "/quiz/" + new_num,                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(info),
            success: function(result){
                let all_data = result["info"]
                console.log("all data", all_data)
                info = all_data
                console.log(info)
                window.location.replace("/results", info=info)
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }

function submit_question(info){
    new_num = info["next_question"]
    $.ajax({
        type: "POST",
        url: "/quiz/" + new_num,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(info),
        success: function(result){
            let all_data = result["info"]
            console.log("all data", all_data)
            info = all_data
            console.log(info)
            window.location.replace("/quiz/" + info["id"], info=info)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function saveResult(info){
    current_id = info["id"]
    $.ajax({
        type: "POST",
        url: "/add_result",              
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(current_id),
        success: function(result){
            let all_data = result["result"]
            console.log("all data", all_data)

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


$(document).ready(function(){

    console.log(info["correct_answer"])
    console.log("result", result)

    if(info["additions"].length!=0){
        if(info["media_type"]=="audio array"){
            $.each(info["additions"], function(i, item){
                if(i==0){
                    let new_topic= $("<div>"+item+"</div>")
                    $("#additional").append(new_topic)
                    console.log("GOODBYEEEE")
                }
                else if(i%2!=0){
                    let new_topic= $("<div>"+item+"</div>")
                    $("#additional").append(new_topic)
                    console.log("OKKKKKK")
                }
                else{
                    //let new_topic=$("<button type='button' value='" + item +"' class='play_audio'>"+"<img src='https://cdn1.iconfinder.com/data/icons/playback-controls/24/172-512.png'>"+"</button>")
                    let new_topic= $('<audio controls> <source src="/static/'+item+ '"></audio>')
                    console.log("HEREEEE")
                    $("#additional").append(new_topic)
                }
            })
        }
        else{
            let new_topic= $("<div>"+info["additions"][0]+"</div>")
            $("#additional").append(new_topic)
        }
    }

    $('#next').prop('disabled', true)
    total_points = info["points"]
    tries = 0
    if(info["id"]=="1"){
        $("#points_calculator").text("0/1000")
        info["points"] = 0
        total_points = 0
    }

    $.each(info["answers"], function(i, ans){
        let new_answer= $("<button type='button' class='btn-lg btn-primary btn ans_option' value='" + ans +"' class='ans_option'>"+ans+"</button>")
        $("#answer_choices").append(new_answer)

        // $("#correct_mark").append()
    })

    $("#points_calculator").text("Points: "+info["points"]+"/1000")
    $("#question_number").text("Question: "+info["id"]+"/10")

    $(".ans_option").click(function(){     
        current_choice = $(this).attr("value")
        console.log(current_choice)
        tries += 1
        console.log(tries)
        if(current_choice == info["correct_answer"]){
            $(this).css('background-color','#40916c')
            $(this).css('border-color','#40916c')
            console.log("TRIES!" + tries)
            if(tries==1){
                points = 100
                $("#feedback").text("+"+points+"!")
                $("#feedback").css('color','#40916c')
            }
            else if(tries==2){
                points = 50
                console.log("HELLO")
                console.log(points + "points")
                $("#feedback").text("+"+points+"!")
                $("#feedback").css('color','#40916c')
            }else if(tries==3){
                points = 10
                saveResult(info)
                $("#feedback").text("+"+points+"!")
                $("#feedback").css('color','#40916c')
            }
            else{
                points = 0
                saveResult(info)
                $("#feedback").text("+0!")
                $("#feedback").css('color','#40916c')
            }
            $('.ans_option').prop('disabled', true)
            $('#next').prop('disabled', false)
            total_points = String(parseInt(total_points) + points)
            $("#points_calculator").text("Points: "+total_points+"/1000")
            console.log(points)
            
        }else{
            $(this).css('background-color','#D21404 !important')
            $(this).css('border-color','#D21404 !important')
            $(this).css('border','None')
            $("#feedback").text("Try again")
            $("#feedback").css('color','#D21404')
            $('#next').prop('disabled', true)
        }

    })

    $("#next").click(function(){     
        console.log("picked next")
        goToNext(total_points, info["id"])
    })
})
