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
        "next_question": "8"
    },
    {
        "id": "8",
        "question": "Consider the following:",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "Tibet",
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
        "media": "",
        "media_type": "audio array",
        "additions": ["The following are Tibetian greetings. Which one corresponds to “Tashi delek”--hello?", "1", "/media/hello", "2", "/media/other"],
        "points": "0",
        "tries": "0",
        "next_question": "10"
    },
    {
        "id": "10",
        "question": "Listen to the audios and respond to the question below:",
        "answers":  ["Spain", "Yemen", "Japan", "Tibet", "New Zealand"],
        "correct_answer": "New Zealand",
        "media": "",
        "media_type": "audio array",
        "additions": ["Click on the incorrect pairing of greetings", "Spain", "/media/spain", "Yemen", "/media/yemen", "Japan", "/media/japan", "Tibet", "/media/tibet", "New Zealand", "/media/notnz"],
        "points": "0",
        "tries": "0",
        "next_question": "-1"
    }
    ]   



learn = [
{
    "id": "1",
    "country": "Spain",
    "hello_description": ["Touch your right cheeks together and make a kissing sound, then repeat the process on the left side"],
    "hello": [" “Hola” (O-la, Hello)", " “Ey” (Ey, hello) "],
    "hello_media": [" media/pronunciation_es_hola.mp3"],
    "goodbye_description": ["If female: Use the touching cheeks gesture.","If male: typical to shake hands."],
    "goodbye": [" “Adios” (Ah-dee-os, goodbye)", " “Hasta luego” (Hasta lu-ego, see you tomorrow)  "],
    "goodbye_media": ["media/pronunciation_es_adiós.mp3", "media/pronunciation_es_hasta_luego.mp3"],
    "next_question": "2"
}, {
    "id": "2",
    "country": "Yemen",
    "hello_description": [" If male: Shake hands with male Muslims. Some may not shake hands with non-Muslims. If female: Avoid shaking hands due to religious restrictions for them. "],
    "hello": [" “marhaba” (Hello) ", " “As-Salam-u-Alaikum” (Peace by unto you) "],
    "hello_media": [" media/arabicwelcome.mp3", " media/Ar-السلام_عليكم.oga"],
    "goodbye_description": ["You can say the Salam greeting when arriving and leaving a gathering."],
    "goodbye": [" “ma'a as-salaama” (goodbye)"],
    "goodbye_media": ["media/pronunciation_es_adiós.mp3"],
    "next_question": "3"
}, {
    "id": "3",
    "country": "Japan",
    "hello_description": [" Bow from the waist with 45-degrees, with deeper bows to be more formal/respectful. Address everybody in the group, not one single greeting."],
    "hello": [" “こんにちは” (Kon'nichiwa, good afternoon, for semi-formal settings) ", " “やあ”(Ya, hey, exclamation/informal settings) "],
    "hello_media": [" media/pronunciation_ja_こんにちは.mp3", " media/pronunciation_ja_じゃあね.mp3"],
    "goodbye_description": [],
    "goodbye": [" “さようなら” (Saiyonnara, goodbye)", "“じゃあね” (Ja ne, see you)"],
    "goodbye_media": ["media/pronunciation_ja_さようなら.mp3"],
    "next_question": "4"
},{
    "id": "4",
    "country": "New Zealand",
    "hello_description": ["Monks stick out their tongues as a sign of respect or agreement.", "Many press the hands together and place them in front of their chest to show that they “come in peace”."],
    "hello": ["“Tashi delek” (Good fortune, hello)"],
    "hello_media": ["media/pronunciation_bo_བཀྲ་ཤིས་བདེ་ལེགས།.mp3"],
    "goodbye_description": [],
    "goodbye": ["“Kah-leh phe” (Goodbye)", "“Jeh yong” (See you later)"],
    "goodbye_media": ["media/pronunciation_bo_ག་ལེར་ཕེབས་།.mp3", "media/pronunciation_bo_རྗེས་མ་མཇལ་ཡོང་།.mp3"],
    "next_question": "5"

},{
    "id": "5",
    "country": "Tibet",
    "hello_description": ["Hugs and shake hands with eye contact.", "Do not call someone over by yelling “Oi”.", "Maōri greet by pressing noses together."],
    "hello": ["“Kia ora!” (Hi)", "“Teh-nah kweh” (formal, hello)", "“Kia ora, bro!” (Hi, mate)", "“gidday!”"],
    "hello_media": ["media/pronunciation_mi_kia_ora.mp3", "pronunciation_mi_tēnā_koe.mp3"],
    "goodbye_description": [],
    "goodbye": ["“Haere rā ” (formal, goodbye)", "“Kia ora” (informal)"],
    "goodbye_media": ["media/pronunciation_mi_kia_ora.mp3"],
    "next_question": "-1"
}] 
# ROUTES


@app.route('/')
def hello_world():
   return render_template('home.html')   

@app.route('/learn/<id>', methods=['GET', 'POST'])
def learn_country(id=None, learn=learn):
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




