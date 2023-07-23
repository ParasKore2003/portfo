"""Modules required for this program"""
import csv
from flask import Flask, render_template,request, redirect
app = Flask(__name__)

@app.route("/")
def my_home():
    """navigates to home page"""
    return render_template('index.html')

def write_to_file(data):
    """stores data in localfile"""
    with open('./web_development/database.txt', mode='a', encoding='utf-8') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    """stores data in csv format"""
    with open('./database.csv',newline='', mode='a', encoding='utf-8') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='\"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """stores data and redirects to the thank you page"""
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Data not saved to the database'
    else:
        return 'Something went wrong, Try again'

#dynamically writes the routes so we dont have to make individual entries
@app.route("/<string:page_name>")
def html_page(page_name):
    """navigates to the selected page"""
    return render_template(page_name)
