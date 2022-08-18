from flask import Flask,request
from dbm import save_to_db

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Sahar Keren Banget'

@app.route('/test',methods=['GET','POST'])
def test_application():
    if request.method == 'POST':
        return 'AndA pake metode POST ya hehe'
    elif request.method == 'GET':
        return 'Anda pake metode GET ya, ketauan hehe'
    return 'Anda memasuki rute test'

@app.route('/location',methods=['GET','POST'])
def location_application():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    kecepatan = request.args.get('kecepatan')
    save_to_db(kecepatan=kecepatan,latitude=latitude,longitude=longitude)
    return {
        "message": "Sukses Memasukan data ke database"
    }

if __name__ == '__main__':
    app.run(debug=True)
