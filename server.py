from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 2
data = [
    {
        "id": 1,
        "name": "michael scott"
    },
    {
        "id": 2,
        "name": "jim halpert"
    },
]

quiz = [
    {
        "id": "1",
        "question": "Click the area this custom corresponds to",
        "answers": ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "New Zealand",
        "media": "https://www.nzmanukagroup.com/files/cache/1d6f5c65ebb8a79e68ac15b033fc34a4_f45.jpg",
        "points": "0",
        "chosen_answer": "",
        "tries": "0",
        "next_question": "2"
    }, {
        "id": "2",
        "question": "Click the country this custom matches",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "Japan",
        "chosen_answer": "",
        "media": "https://c.tenor.com/GBGNBFPsDV4AAAAC/bow-japanese.gif",
        "points": "0",
        "tries": "0",
        "next_question": "3"
    }
    ]   
# ROUTES

@app.route('/hi')
def hello():
   return 'Hi hi hi hi hi hi hi hi hi'


@app.route('/')
def hello_world():
   return render_template('hello_world.html')   


@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello_name.html', name=name) 


@app.route('/people')
def people():
    return render_template('people.html', data=data)  


# AJAX FUNCTIONS

# ajax for people.js
@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    global data 
    global current_id 

    json_data = request.get_json()   
    name = json_data["name"] 
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_name_entry = {
        "name": name,
        "id":  current_id
    }
    data.append(new_name_entry)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)

@app.route('quiz', methods=['GET', 'POST'])
def answer_quiz(quiz_response=None):
    global quiz

    json_data = request.get_json()
    id_num = json_data["id_num"]
    idx = int(id_num) - 1
    choice = json_data["choice"]
    points = json_data["points"]

    if choice == quiz[idx]["correct_answer"]:
        #Set up the points
        if quiz[idx]["tries"] == "1":
            if idx == 0:
                quiz[idx]["points"] = "0"
            else:
                quiz[idx]["points"] = quiz[idx-1]["points"]
        elif quiz[idx]["tries"] == "1":
            quiz[idx]["points"] = str(int(quiz[idx][points]) + 100)
        elif quiz[idx]["tries"] == "2":
            quiz[idx]["points"] = str(int(quiz[idx][points]) + 50)
        elif quiz[idx]["tries"] == "3":
            quiz[idx]["points"] = str(int(quiz[idx][points]) + 10)
        else:
           quiz[idx]["points"] = quiz[idx]["points"]

    else:
        previous_choice = {'choice': choice, 'right': 'no'}

    return render_template('question.html', info=quiz[idx], previous_choice=previous_choice)

 


if __name__ == '__main__':
   app.run(debug = True)




