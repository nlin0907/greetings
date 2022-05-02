function jump_to_link(current_id){
    let current_link='/learn/'+current_id
    window.location.replace(current_link)
}



var onpage = []
$(document).ready(function(){
    console.log(info["points"])

    if(result.length == 0 && info["points"] < 750){
        $(".container").empty();
        let warning_message= $("<div class='header'>Please complete the quiz first</div>");
        $(".container").append(warning_message);
    }
    else{
        $("#result_list").empty()

        $.each(result, function(i, item){
            var current_id;
            console.log(item["relevant_country"])
            $.each(learn, function(i, item_learn){
                if ((item_learn["country"] == item["relevant_country"])){
                    current_id=item_learn["id"]
                    console.log("on pg", onpage)
                    console.log('/learn/'+current_id)
                }
            })

            //let current_link='/learn/'+current_id
            //let review_link= $("<a href="+current_link+">"+item["relevant_country"]+"</a>")
            const review_link_button=$('<button class="button-result review_link" id= " ' + current_id + '">'+item["relevant_country"]+"</button>");
            if(onpage.indexOf(item["relevant_country"]) == -1){
                onpage.push(item["relevant_country"])
                $("#result_list").append(review_link_button)
                $("#result_list").append($("<br>"))
                $("#result_list").append($("<br>"))
            }
            $('.review_link').click(function(e){
                jump_to_link(e.target.id);
            });
    
            // $("#correct_mark").append()
        })
    }
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


