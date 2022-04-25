var onpage = []
$(document).ready(function(){
    $("#result_list").empty()
    $.each(result, function(i, item){
        var current_id;
        console.log(item["correct_answer"])
        $.each(learn, function(i, item_learn){
            if ((item_learn["country"] == item["correct_answer"]) && (jQuery.inArray(item_learn["id"], onpage) !== -1)){
                current_id=item_learn["id"]
                onpage.append(item_learn["id"])
                console.log("on pg", onpage)
                console.log('/learn/'+current_id)
            }
        })
        let current_link='/learn/'+current_id
        let review_link= $("<a href="+current_link+">"+item["correct_answer"]+"</a>")
        
        $("#result_list").append(review_link)
        $("#result_list").append($("<br>"))
    
            // $("#correct_mark").append()
        })
/*
        if (item["media_type"]=="image"){
            let img_tem=$("<img class='media_source quiz_media' src=" + item["media"] + "alt='Image of greeting' width='500' height='400'></img>")
            $("#result_list").append(img_tem)
        }else if(item["media_type"]=="text"){
            let text_tem=$("<div class='media_source quiz_media text-media'>"+item["media"]+"</div>")
            $("#result_list").append(text_tem)
        }else if(item["media_type"]=="audio"){
            let audio_tem=$("<audio controls> <source src="+item['media']+"type='audio/mp3'> </audio>")
            $("#result_list").append(audio_tem)
        }
           
     */     
    

        
    
})