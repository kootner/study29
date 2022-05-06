from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.nftca.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/study29", methods=["GET"])
def restaurant_get():
    restaurant_list = list(db.study29.find({}, {'_id': False}))
    return jsonify({'restaurants': restaurant_list})


@app.route("/study29", methods=["POST"])
def restaurant_post():
    restaurant_receive = request.form['restaurant_give']
    comment_receive = request.form['comment_give']
    menu_receive = request.form['menu_give']
    pick_receive = request.form['pick_give']
    url_receive = request.form['url_give']
    score_receive = request.form['score_give']
    img_receive = request.form['img_give']

    doc = {
        'restaurant': restaurant_receive,
        'comment': comment_receive,
        'menu': menu_receive,
        'pick': pick_receive,
        'url': url_receive,
        'score': score_receive,
        'img': img_receive
    }

    db.study29.insert_one(doc)

    return jsonify({'msg': '맛집 등록 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
