from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)



quiz = [
    {
        "id": "1",
        "question": "Click the area this custom corresponds to",
        "answers": ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "New Zealand",
        "relevant_country": "New Zealand",
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
        "relevant_country": "Japan",
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
        "relevant_country": "Japan",
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
        "relevant_country": "Yemen",
        "media_type": "audio",
        "media": "/static/media/arabicwelcome.mp3",
        "additions": ["ٱلسَّلَامُ عَلَيْكُمْ as-salāmu ʿalaykum"],
        "points": "0",
        "tries": "0",
        "next_question": "5"
    },{
        "id": "5",
        "question": "Click the situation this custom matches",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "Spain",
        "relevant_country": "Spain",
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
        "relevant_country": "Yemen",
        "media": "/static/media/yemen_question.jpg",
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
        "relevant_country": "Japan",
        "media": "",
        "media_type": "audio array",
        "additions": ["Which of these two Japanese “goodbyes” is most formal?", "1", "media/pronunciation_ja_さようなら.mp3", "2", "media/pronunciation_ja_やあ.mp3"],
        "points": "0",
        "tries": "0",
        "next_question": "8"
    },
    {
        "id": "8",
        "question": "Consider the following:",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "Tibet",
        "relevant_country": "Tibet",
        "media": "https://www.homeexchange.com/blog/content/images/2020/03/GettyImages-585181460.jpg",
        "media_type": "image",
        "additions": ["You’re visiting a town, and a child comes up to greet you like this. Where are you most likely?"],
        "points": "0",
        "tries": "0",
        "next_question": "9"
    },
    {
        "id": "9",
        "question": "Listen to the audios and respond to the question below:",
        "answers":  ["Audio 1", "Audio 2"],
        "correct_answer": "Audio 1",
        "relevant_country": "Tibet",
        "media": "",
        "media_type": "audio array",
        "additions": ["The following are Tibetian greetings. Which one corresponds to “Tashi delek”--hello?", "1", "media/pronunciation_bo_བཀྲ་ཤིས་བདེ་ལེགས།.mp3", "2", "media/pronunciation_bo_ག་ལེར་ཕེབས་།.mp3"],
        "points": "0",
        "tries": "0",
        "next_question": "10"
    },
    {
        "id": "10",
        "question": "Listen to the audios and respond to the question below:",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "New Zealand",
        "relevant_country": "New Zealand",
        "media": "",
        "media_type": "audio array",
        "additions": ["Click on the incorrect pairing of greetings", "Spain", "media/pronunciation_es_hola.mp3", "Yemen", "media/Ar-السلام_عليكم.oga", "Japan", "media/pronunciation_ja_こんにちは.mp3", "Tibet", "media/pronunciation_bo_རྗེས་མ་མཇལ་ཡོང་།.mp3", "New Zealand", "media/pronunciation_mi_kia_ora.mp3"],
        "points": "0",
        "tries": "0",
        "next_question": "-1"
    }
    ]   




learn = [
{
    "id": "1",
    "country": "Spain",
    "hello_description": ["Touch your right cheeks together and make a kissing sound, then repeat the process on the left side."],
    "hello": ["“Hola” (O-la, Hello)"],
    "hello_media": ["media/pronunciation_es_hola.mp3"],
    "goodbye_description": ["<b>If female:</b> Use the touching cheeks gesture.","<b>If male: </b> typical to shake hands."],
    "goodbye": ["“Adios” (Ah-dee-os, goodbye)", "“Hasta luego” (Hasta lu-ego, see you tomorrow)  "],
    "goodbye_media": ["media/pronunciation_es_adiós.mp3", "media/pronunciation_es_hasta_luego.mp3"],
    "next_question": "2",
    "prev_question": "-1",
    "media": "https://thumbs.gfycat.com/PresentNextBluegill-max-1mb.gif"
}, {
    "id": "2",
    "country": "Yemen",
    "hello_description": ["<b>If male:</b> Shake hands with male Muslims. Some may not shake hands with non-Muslims.", "<b>If female:</b> Avoid shaking hands due to religious restrictions for them.", "Use your <b>right hand</b> when shaking hands."],
    "hello": [" “marhaba” (Hello) ", "“As-Salam-u-Alaikum” (Peace by unto you)"],
    "hello_media": ["media/arabicwelcome.mp3", "media/Ar-السلام_عليكم.oga"],
    "goodbye_description": ["You can say the Salam greeting when arriving and leaving a gathering."],
    "goodbye": [" “ma'a as-salaama” (goodbye)"],
    "goodbye_media": ["media/pronunciation_es_adiós.mp3"],
    "next_question": "3",
    "prev_question": "1",
    "media": "https://scoopempire.com/wp-content/uploads/2018/10/shake_1-1.jpg"
}, {
    "id": "3",
    "country": "Japan",
    "hello_description": [" Bow from the waist with 45-degrees, with deeper bows to be more formal/respectful.", "Address everybody in the group, not one single greeting."],
    "hello": [" “こんにちは” (Kon'nichiwa, good afternoon, semi-formal settings) ", " “やあ”(Ya, hey, exclamation/informal settings) "],
    "hello_media": ["media/pronunciation_ja_こんにちは.mp3", "media/pronunciation_ja_じゃあね.mp3"],
    "goodbye_description": [],
    "goodbye": [" “さようなら” (Saiyonnara, goodbye)", "“じゃあね” (Ja ne, see you)"],
    "goodbye_media": ["media/pronunciation_ja_さようなら.mp3"],
    "next_question": "4",
    "prev_question": "2",
    "media": "https://c.tenor.com/GBGNBFPsDV4AAAAC/bow-japanese.gif"
},{
    "id": "4",
    "country": "Tibet",
    "hello_description": ["Monks stick out their tongues as a sign of respect or agreement.", "Many press the hands together and place them in front of their chest to show that they “come in peace”."],
    "hello": ["“Tashi delek” (Good fortune, hello)"],
    "hello_media": ["media/pronunciation_bo_བཀྲ་ཤིས་བདེ་ལེགས།.mp3"],
    "goodbye_description": [],
    "goodbye": ["“Kah-leh phe” (Goodbye)", "“Jeh yong” (See you later)"],
    "goodbye_media": ["media/pronunciation_bo_ག་ལེར་ཕེབས་།.mp3", "media/pronunciation_bo_རྗེས་མ་མཇལ་ཡོང་།.mp3"],
    "next_question": "5",
    "prev_question": "3",
    "media": "https://www.travelordietrying.com/wp-content/uploads/2017/03/11747360-greetingspreview2-1487274955-650-b0a16e3e93-1487335826.jpg"
},{
    "id": "5",
    "country": "New Zealand",
    "hello_description": ["Hugs and shake hands with eye contact.", "<b>Do not</b> call someone over by yelling “Oi”.", "Maōri greet by pressing noses together."],
    "hello": ["“Kia ora!” (Hi)", "“Teh-nah kweh” (formal, hello)"],
    "hello_media": ["media/pronunciation_mi_kia_ora.mp3", "media/pronunciation_mi_tēnā_koe.mp3"],
    "goodbye_description": [],
    "goodbye": ["“Haere rā ” (formal, goodbye)", "“Kia ora” (informal)"],
    "goodbye_media": ["media/pronunciation_mi_kia_ora.mp3"],
    "next_question": "-1",
    "prev_question": "4",
    "media": "https://www.travelordietrying.com/wp-content/uploads/2017/03/pablo-10-3.png"
}] 

result=[]

# ROUTES

@app.route('/')
def hello_world():
   return render_template('home.html')   

@app.route('/learn/<id>', methods=['GET', 'POST'])
def learn_country(id=None, learn=learn):
   
    if request.method=="POST":
        json_data = request.get_json()
        if json_data is not None:
            id = json_data["id"]
            idx = int(id) - 1
            new_idx = int(json_data["next_question"]) - 1
            print("first", learn[idx])
            learn[idx] = json_data
            print("second", learn[idx])
    else:
        idx = int(id)
        new_idx = int(id) - 1
    return render_template('learn.html',id=id, learn=learn[new_idx])

# AJAX FUNCTIONS
@app.route('/quiz/<id_num>', methods=['GET', 'POST'])
def answer_quiz(id_num=None):
    global quiz
    global result
    if request.method=="POST":
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
        return render_template('quiz.html', info=quiz[new_idx],result=result)

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
    global result
    global learn
    return render_template('results.html', info=quiz[len(quiz)-1],result=result,learn=learn)

@app.route('/quiz')
def display_quizhome():
    global result
    result=[]
    return render_template('quizhome.html')

@app.route('/add_result',methods=['GET','POST'])
def add_result():
    global result
    global quiz
    json_data = request.get_json()
    current=quiz[int(json_data)-1]
    result.append(current)

    return jsonify(result=result)

if __name__ == '__main__':
   app.run(debug = True)




