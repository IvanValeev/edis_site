from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    
    info = {
        "name": "Ірина Швидка",
        "email": "test@gmail.com",
        "phone": "+380 ** *** ***",
        "about": "Цей сайт присвячено котячому розпліднику Ediscaprise.",
        "facebook": "facebook",
        "instagram": "instagram"
        }
    
    return render_template("index.html", info=info)

if __name__ == "__main__":
    app.run(debug=True)