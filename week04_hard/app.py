## 필요한 모듈(flask, pymongh) import
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# flask를 이용하여 서버 생성
app = Flask(__name__)

## pymongo를 이용하여 mongoDB 호출 및 생성
client = MongoClient('localhost', 27017)
db = client.dbsparta

## index.html 페이지 불러오기
@app.route('/')
def home():
    return render_template('index.html')

## Create : 사용자로부터 입력받아 MongoDB에 저장하는 API
@app.route('/order', methods=['POST'])
def receive_order():
    receive_name = request.form['name_give']
    receive_count = request.form['give_count']
    receive_address = request.form['give_address']
    receive_phone = request.form['give_phone']
    doc = {
        'name': receive_name,
        'count': receive_count,
        'address': receive_address,
        'phone': receive_phone
    }
    db.order_hard.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문완료!'})

## Read : 모든 주문리스트를 불러오는 API
@app.route('/order', methods=['GET'])
def show_order():
    orders = list(db.order_hard.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
