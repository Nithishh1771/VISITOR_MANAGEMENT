from flask import Flask,render_template as rt,request ,url_for
from datetime import datetime
from flask_migrate import Migrate
from model import db,Visitor_pass
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/Visitor_Management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

migrate = Migrate(app,db)

@app.route("/",methods=["GET"])
def home():
    return rt("visitor_form.html")


@app.route("/pass",methods=["GET","POST"])
def pass1():
    
    if request.method=='POST':
        uname = request.form["username"]
        mobile =request.form["mobile"]
        gender=request.form["gender"]
        pvisit=request.form["pvisit"]
        Email_ID=request.form["Email_ID"]
        proof=request.files["proof"]
        filename = secure_filename(proof.filename)

        upload_folder = "static/uploads"
        os.makedirs(upload_folder, exist_ok=True)
        proof.save(os.path.join(upload_folder, filename))
        current_time= datetime.now()
        date = current_time.strftime("%d-%m-%y")
        time = current_time.strftime("%I : %M : %S %p")

        manage=Visitor_pass(
            uname= uname,
            mobile=mobile,
            gender=gender,
            pvisit=pvisit,
            Email_ID=Email_ID,
            proof=filename,
            date=date,
            time=time
        )
        db.session.add(manage)
        db.session.commit()

        return rt("pass.html",
            uname=uname,
            mobile=mobile,
            gender=gender,
            pvisit=pvisit,
            Email_ID=Email_ID,
            date=date,
            time=time)
    return "Please submit the form first."

@app.route("/Thank_you")
def tq():
    return rt("Thankyou.html")

if __name__=="__main__":
    app.run(debug=True,)
