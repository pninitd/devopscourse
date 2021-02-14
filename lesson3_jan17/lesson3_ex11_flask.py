import io

from flask import Flask

app = Flask(__name__)

# accessed via <HOST>:<PORT>/content/<file_name>
@app.route('/content')
@app.route('/content/<file_name>')
def read_user_file(file_name='no file passed'):
    content = read_content(file_name)
    if content is None or content == '':
        return 'Error reading file: ' + file_name, 400
    else:
        return 'file content: ' + content, 200  # status code


# accessed via <HOST>:<PORT>/register/<file_name>
@app.route('/register')
@app.route('/register/<file_name>')
def write_user_file(file_name=''):
    if file_name != '':
        is_success = write_content(file_name)
        if is_success is True:
            return 'success', 201
        else:
            return 'Error writing to file: ' + file_name, 400  # status code
    else:
        return 'no file passed ', 400  # status code


def read_content(input_file):
    content = ""
    try:
        if input_file != None:
            try:
                with open(input_file, 'r+', encoding='utf-8') as file:
                    content = file.read()
            except IOError as e:
                print("I/O error:", e)
            finally:
                file.close()
    finally:
        return content


def write_content(input_file):
    content = "“hello”"
    is_success = False
    try:
        if input_file != None:
            try:
                with open(input_file, 'a+', encoding='utf-8') as file:
                    file.write(content)
                    is_success = True
            except IOError as e:
                print("I/O error:", e)
            finally:
                file.close()
    finally:
        return is_success


app.run(host='127.0.0.1', debug=True, port=30000)
