from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.nftca.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/*********", methods=["GET"])
def restaurant_get():
    restaurant_list = list(db.study29.find({}, {'_id': False}))
    return jsonify({'restaurants' : restaurant_list})

@app.route("/*********", methods=["POST"])
def restaurant_post():
    restaurant_receive = request.form['restaurant_give']
    address_receive = request.form['address_give']
    img_receive = request.form['img_give']
    menu_receive = request.form['menu_give']

    doc = {
        'name': restaurant_receive,
        'address': address_receive,
        'img':img_receive,
        'menu':menu_receive
    }

    db.study29.insert_one(doc)

    return jsonify({'msg': '맛집 등록 완료!'})