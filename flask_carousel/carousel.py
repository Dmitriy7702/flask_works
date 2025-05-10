from itertools import count

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


default_images = ['mars1.webp', 'mars2.jpg', 'mars3.jpg']


@app.route('/galery', methods=['POST', 'GET'])
def gallery():
    if request.method == 'POST':
        file = request.files.get('new_image')
        if file is not None:
            print(file.content_type)
            name = f'img_{next(count())}.jpg'
            full_name = url_for('static', filename=f'img/{name}')[1:]
            with open(full_name, 'wb') as target_file:
                target_file.write(file.read())
                default_images.append(name)
    return render_template('gallery.html', images=default_images)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
