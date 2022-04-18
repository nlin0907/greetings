function goToNext(){
    console.log(parseInt(learn["id"]))
    if(parseInt(learn['next_question'])==-1){
        window.location.href="/quiz/1"
    }else{
        window.location.href="/learn/"+learn['next_question']
    }
}
function hello() {
    $.each(learn["hello"], function(i,item){
        console.log(item)
        let new_topic= $("<div>" + item + "</div>")
        $("#hello_content").append(new_topic)
    })
}

function goodbye() {
    $.each(learn["goodbye"], function(i,item1){
        console.log(item1)
        let new1= $("<div>"+item1+"</div>")
        $("#goodbye_content").append(new1)
    })
}

function hello_description() {
    $.each(learn["hello_description"], function(i,item3){
        console.log("here")
        console.log(item3)
        let new_description= $("<div>"+item3+"</div>")
        console.log("new_description:" + new_description)
        $("#hello_description").append(new_description)
    })
}

function goodbye_description() {
    $.each(learn["goodbye_description"], function(i,item){
        console.log(item)
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
        console.log("picked next")
        if(parseInt(learn['next_question'])==-1){
            window.location.href="/quiz/1"
        }else{
            window.location.href="/learn/"+learn['next_question']
        }
    })
})