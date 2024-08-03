import os
import uuid

from flask import Flask
from flask import request, make_response, render_template, redirect, url_for, Response, send_from_directory,jsonify
import pandas as pd


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myValue = 'library'
    myResult = 10+20
    myList = [10, 20,30,40,50]
    return render_template('index.html', myValue=myValue, myResult=myResult, myList=myList)

@app.route('/other')
def other():
    somme_text = 'some text'
    return render_template(template_name_or_list='other.html', somme_text=somme_text)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


# dynamic url without specifiying it statically.
@app.route('/thisisaredirect')
def thisisaredirect():
    somme_text = 'some text from redirect'
    return render_template(template_name_or_list='thisisaredirect.html', somme_text=somme_text)



@app.route('/redirect_endpoint')
def redirect_enpoint():
    return redirect(url_for('other'))
#change content in the html

@app.route('/index2', methods=['GET', 'POST'])
def index2():
    if request.method == 'GET':
        return render_template('index2.html')
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'ian' and password == 'dejesus':
            return "success"
        else:
            return 'failure'
        
# This route handles file uploads, returning plain text content for text files and HTML table for Excel files
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    
    if file.content_type == 'text/plain':
        return file.read().decode('utf-8')
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
    # return render_template('file_upload.html')


# convert xls/xlsx to a .csv file

@app.route('/convert_csv', methods=['POST'] )
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
    headers = {'Content-Disposition': 'attachment; filename=data.csv'}
    )
    return response 

@app.route('/download_csv', methods=['POST'])
def download_csv():
    file = request.files['file']
    
    df = pd.read_excel(file)
    
    if not  os.path.exists('downloads'):
        os.mkdir('downloads')
    filename = f'{uuid.uuid4()}.csv'
    
    df.to_csv(os.path.join('downloads', filename))
    
    return render_template(template_name_or_list='download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename ,download_name='result.csv')

@app.route('/handle_post', methods=['POST'])
def handle_post():
    greetings= request.json['greetings']
    name= request.json['name']
    
    with open('file.txt', 'w') as f:
        f.write(f'{greetings} , {name} ')
    
    return jsonify({'message': "Successfully Writtern!"})
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    

