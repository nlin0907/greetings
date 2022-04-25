$(document).ready(function(){
    $.each(result, function(i, item){
        $("#result_list").empty()
        console.log(item["media"])

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
           
          
    

        
    })
})