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
        "media_type": "image",
        "additions": [],
        "points": "0",
        "tries": "0",
        "next_question": "2"
    }, {
        "id": "2",
        "question": "Click the country this custom matches",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "Japan",
        "media": "https://c.tenor.com/GBGNBFPsDV4AAAAC/bow-japanese.gif",
        "media_type": "image",
        "additions": [],
        "points": "0",
        "tries": "0",
        "next_question": "3"
    },
    {
        "id": "3",
        "question": "Click the situation this custom matches",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "Japan",
        "media": "You should avoid eye contact in conversations",
        "media_type": "text",
        "additions": [],
        "points": "0",
        "tries": "0",
        "next_question": "4"
    },
    {
        "id": "4",
        "question": "Select the area where you would hear the following words:",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "Yemen",
        "media": "media/arabicwelcome.mp3",
        "media_type": "audio",
        "additions": ["ٱلسَّلَامُ عَلَيْكُمْ as-salāmu ʿalaykum"],
        "points": "0",
        "tries": "0",
        "next_question": "5"
    },{
        "id": "5",
        "question": "Click the situation this custom matches",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "Spain",
        "media": "https://letsbuyinspain.com/wp-content/uploads/2016/08/cheek-kiss-greeting-e1450117959995-1024x666.jpg",
        "media_type": "image",
        "additions": [],
        "points": "0",
        "tries": "0",
        "next_question": "6"
    },
    {
        "id": "6",
        "question": "Consider the following scenario",
        "answers":  ["Shake her hand", "Bow", "Say As-Salam-u-Alaikum", "Rub your nose against hers"],
        "correct_answer": "Say As-Salam-u-Alaikum",
        "media": "https://media.gettyimages.com/photos/happy-arabic-girl-picture-id154917566?s=612x612",
        "media_type": "image",
        "additions": ["You’re in Yemen, and are introduced to your friend Abbud’s wife. How do you greet her?"],
        "points": "0",
        "tries": "0",
        "next_question": "7"
    },
    {
        "id": "7",
        "question": "Listen to the audios and respond to the question below",
        "answers":  ["Audio 1", "Audio 2"],
        "correct_answer": "Audio 1",
        "media": "",
        "media_type": "audio array",
        "additions": ["Which of these two Japanese “goodbyes” is most formal?", "1", "media/formal", "2", "media/informal"],
        "points": "0",
        "tries": "0",
        "next_question": "-1"
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
        print("first", quiz[idx])
        quiz[idx] = json_data
        print("second", quiz[idx])
    else:
        idx = int(id_num)
        new_idx = int(id_num) - 1
        return render_template('quiz.html', info=quiz[new_idx])

    print("points", quiz[idx]["points"])
    if new_idx == 0:
        quiz[new_idx]["points"] = "0"
    else:
        quiz[new_idx]["points"] = quiz[new_idx-1]["points"]
    print("new quiz",quiz)
    return jsonify(info=quiz[new_idx])

@app.route('/results', methods=['GET','POST'])
def display_results():
    print("here")
    global quiz
    return render_template('results.html', info=quiz[len(quiz)-1])

if __name__ == '__main__':
   app.run(debug = True)




