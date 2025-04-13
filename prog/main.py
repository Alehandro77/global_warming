from flask import Flask, render_template,request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'CFijugJGSDUgUDGvcUGDGDSugSDuvchLSDhvisv'  # Замените на что-то случайное!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<News {self.id}>'
    


@app.route('/', methods=['GET','POST'])
def glav():
    news = News.query.order_by(News.id).all()
    return render_template('glav.html', news=news)


@app.route('/plus', methods=['GET','POST'])
def plus():
    return render_template('plus.html')

@app.route('/qvis', methods=['GET','POST'])
def qvis():
    if request.method == 'POST':

        ball = 0

        v1 = request.form['v1']
        v2 = request.form['v2']
        v3 = request.form['v3']
        v4 = request.form['v4']
        v5 = request.form['v5']
        v6 = request.form['v6']
        v7 = request.form['v7']
        v8 = request.form['v8']
        v9 = request.form['v9']
        v10 = request.form['v10']

        if v1 == 'o3':
            ball += 1

        if v2 == 'o3':
            ball += 1

        if v3 == 'o4':
            ball += 1

        if v4 == 'o3':
            ball += 1

        if v5 == 'o3':
            ball += 1

        if v6 == 'o2':
            ball += 1

        if v7 == 'o2':
            ball += 1

        if v8 == 'o3':
            ball += 1

        if v9 == 'o2':
            ball += 1

        if v10 == 'o3':
            ball += 1



        if ball == 1:
            ful_mes = "Вы ответили правильно на " + str(ball)+ ' вопрос'

        elif ball >= 2 and ball <= 4:
            ful_mes = "Вы ответили правильно на " + str(ball)+ ' вопроса'

        elif ball >= 5 or ball == 0:
            ful_mes = "Вы ответили правильно на " + str(ball)+ ' вопросов'

        flash(ful_mes, 'info')
        return render_template('qvis.html')
    else:
        return render_template('qvis.html') 

@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        link =  request.form['link']
        text =  request.form['text']
        news = News(title=title, link=link, text=text)
        db.session.add(news)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('plus.html')
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Создаем таблицы (если их еще нет)
    app.run(debug=True)
