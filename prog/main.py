from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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