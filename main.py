from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return ''


@app.route('/image_mars')
def image_mars():
    return render_template("main.html", image=url_for('static', filename='img/mars.png'))


@app.route('/promotion_image')
def promotion_image():
    return render_template("promotion_image.html", dictionary={'Человечество вырастает из детства.': 'gray',
                                                               'Человечеству мала одна планета.': 'green',
                                                               'Мы сделаем обитаемыми безжизненные пока '
                                                               'планеты.': 'gray',
                                                               'И начнем с Марса!': 'yellow',
                                                               'Присоединяйся': 'red'},
                           image=url_for('static', filename='img/mars.png'))


if __name__ == '__main__':
    app.run(port=8080)
