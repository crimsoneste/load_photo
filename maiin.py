import os
from flask import Flask, url_for, request

app = Flask(__name__)
fold = os.path.join('static')
app.config['UPLOAD_FOLDER'] = fold
mars = os.path.join(app.config['UPLOAD_FOLDER'], 'img/mars.jpg').replace("", "/")
css = os.path.join(app.config['UPLOAD_FOLDER'], 'css/style.css').replace("", "/")


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="en">
                        <head>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                          <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                          <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          <title>Отбор астронавтов</title>
                        </head>

                        <body>
                          <h1><center>Загрузка фотографии<center></h1>
                          <h2><center>для участия в миссии<center></h2>
                          <div>
                              <form class="login_form" method="post" enctype="multipart/form-data">
                                  Приложите фотографию
                                  <div class="form-group">
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                            <label for="photo">Файл не выбран</label>
                                  </div>
                                  <img src="{mars}"><img>
                                      <button type="submit" class="btn btn-primary">Отправить</button>
                              </form>
                          </div>
                        </body>
                    </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        if os.path.exists(mars):
            os.truncate(mars, 0)
        with open(mars, "ab+") as file:
            file.write(f.read())
        return f'''<!doctype html>
                    <html lang="en">
                        <head>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                          <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                          <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          <title>Отбор астронавтов</title>
                        </head>

                        <body>
                          <div>
                              <form class="login_form" method="post" enctype="multipart/form-data">
                                  Приложите фотографию
                                  <div class="form-group">
                                              <input type="file" class="form-control-file" id="photo" name="file">
                                  </div>
                                  <img src="{mars}"><img>
                                      <button type="submit" class="btn btn-primary">Отправить</button>
                              </form>
                          </div>
                        </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
