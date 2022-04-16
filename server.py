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

@app.route('/quiz/<id_num>', methods=['GET', 'POST'])
def answer_quiz(id_num=None):
    global quiz

    json_data = request.get_json()
    if json_data is not None:
        id_num = json_data["id"]
        idx = int(id_num) - 1
        new_idx = int(json_data["next_question"]) - 1
        quiz[idx] = json_data
    else:
        idx = int(id_num)
        new_idx = int(id_num) - 1
        return render_template('quiz.html', info=quiz[new_idx])

    if new_idx == 0:
        quiz[new_idx]["points"] = "0"
    else:
        quiz[new_idx]["points"] = quiz[new_idx-1]["points"]

    return jsonify(info=quiz[new_idx])

 


if __name__ == '__main__':
   app.run(debug = True)




