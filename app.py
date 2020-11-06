from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        if data == {'email': '', 'subject': '', 'message': ''}:
            return render_template("error.html")
        else:
            write_data_csv(data)
            return render_template("thankyou.html")
    else:
        return "FORM NOT SUBMITTED !!"


@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')
