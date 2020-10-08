from flask import *
from flask import jsonify
from flask import request
from flask_cors import CORS

import sqlite3


app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False


@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/buy-single-phone",methods=["GET"])
def buy_single_phone():
  return render_template("buy-single-phone.html")


@app.route("/admin",methods=["GET","POST"])
def admin():
  conn = sqlite3.connect('image.db')
  cursor = conn.cursor()

  if request.method == "POST":
    id = request.form.get("product_id")
    name = request.form.get("product_name")
    photo = request.form.get("filebutton")

    cursor.execute(" INSERT INTO new_employee (id, name,photo) VALUES (? ,?, ?)",(id, name, photo))
    conn.commit()
  return render_template("admin.html")

@app.route("/admin/product-view",methods=["GET"])

def product_view():
  conn = sqlite3.connect('image.db')
  cursor = conn.cursor()
  cursor.execute("select * from new_employee")

  data = cursor.fetchall()
  
  return render_template('update.html', data=data)



if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1',port=8027)
    
