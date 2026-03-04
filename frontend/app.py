from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
from flask_login import LoginManager, login_user, login_required
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
import jwt
import datetime

client = MongoClient('localhost', 27017)
# db = client.KKK # name 대기

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
bcrypt = Bcrypt(app) # bcrypt 초기화

login_manager = LoginManager()
login_manager.init_app(app) # login_manager 애플리케이션과 연계
login_manager.login_view = "login" # 로그인 안했을때 이동할 route

# 로그인 페이지
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return "JSON 형식이 아닙니다.", 400

    id = data.get("id")
    pw = data.get("pw")

    if not id or not pw:
        return "ID or PW 누락", 400

    user = db.users.find_one({"id" : id})
    if user and bcrypt.check_password_hash(user["pw"], pw):

        token = jwt.encode({
            "user_id" : user["id"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config["SECRET_KEY"], algorithm="HS256")

        response = make_response(redirect(url_for("daily_mood"))) # 로그인 성공 메인페이지 이동
        response.set_cookie(
            "token",
            token,
            httponly=True,
            samesite="LAX"
        )
        return response
    return "로그인실패", 401

# 회원가입
@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        id = request.json["id"]
        email = request.json["email"]
        pw = request.json["pw"]

        # 중복 ID / Email 확인
        
        hash_pw = bcrypt.generate_password_hash(pw).decode("utf-8") # pw 해쉬암호화

        db.users.insert_one({
            "id" : id,
            "email" : email,
            "pw" : hash_pw
            })            
        return redirect(url_for("login"))

    return render_template("register.html")
    
    
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)