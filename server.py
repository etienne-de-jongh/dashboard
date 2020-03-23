from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./login.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('./database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')

# def write_to_csv(data):
#     with open('./database.csv', newline='', mode='a') as database2:
#         username = data['username']
#         password = data['password']
#         remember_me = data['remember_me']
#         csv_writer = csv.writer(database2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([username, password, remember_me])


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
            try:
                data = request.form.to_dict()
                # write_to_csv(data)
                if data['username'] == 'x@x.com':
                    if data['password'] == 'Passw0rd':
                        return redirect('./overview.html')
                return redirect('./login.html')
            except:
                return "did not save to database"
            else:
                return 'Something went wrong. Try again.'