function goToNext(){
    if(parseInt(learn['next_question'])==-1){
        window.location.href="/quiz/1"
    }else{
        window.location.href="/learn/"+learn['next_question']
    }
}

function goPrev(){
    if(parseInt(learn['prev_question'])==-1){
        window.location.href="/"
    } else{
        window.location.href="/learn/"+learn['prev_question']
    }
}

function hello() {
    $.each(learn["hello"], function(i,item){
        console.log(learn["hello_media"][i])
        let new_topic = ""
        if (learn["hello_media"][i] != null) {
            new_topic= $("<div>" + item + '<br><audio controls> <source src="/static/'+learn["hello_media"][i]+ '"></audio>' + "</div><br>")
            console.log("this is the div audio "+JSON.stringify(new_topic))
        }
        else {
            new_topic= $("<div>" + item + "</div>")
        }
        $("#hello_content").append(new_topic)
    })
}

function goodbye() {
    $.each(learn["goodbye"], function(i,item1){
        let new1= $("<div>"+item1+"</div>")
        $("#goodbye_content").append(new1)
    })
    
}

function hello_description() {
    $.each(learn["hello_description"], function(i,item3){
        let new_description= $("<div>"+item3+"</div>")
        $("#hello_description").append(new_description)
    })
}

function goodbye_description() {
    $.each(learn["goodbye_description"], function(i,item){
        let new_description= $("<div>" + item + "</div>")
        $("#goodbye_description").append(new_description)
    })
}

$(document).ready(function(){
    hello()
    goodbye()
    hello_description()
    goodbye_description()

    $("#next").click(function(){     
        if(parseInt(learn['next_question'])==-1){
            window.location.href="/quiz/1"
        }else{
            window.location.href="/learn/"+learn['next_question']
        }
    })
    
    $("#prev").click(function(){     
        goPrev()
    })
})
