from flask import Flask,render_template,request
import mysql.connector
import os

app = Flask(__name__)

#MYSQL Configuration

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MuthuPandas9'
app.config['MYSQL_DB'] = 'pdf_files'

# Upload folder
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mysql = mysql.connector.connect(
  host=app.config['MYSQL_HOST'],
  user=app.config['MYSQL_USER'],
  password=app.config['MYSQL_PASSWORD'],
  database=app.config['MYSQL_DB']
)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['pdf']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as f:
        pdf_data = f.read()
    
    cursor = mysql.cursor()
    user_name = request.form['name']
    year = request.form['year']
    dept = request.form['dept']
    query = "INSERT INTO pdfs (name, data,user_name,year,dept) VALUES (%s, %s,%s,%s,%s)"
    values = (filename, pdf_data,user_name,year,dept)
    cursor.execute(query, values)
    mysql.commit()
    cursor.close()

    return 'PDF file uploaded successfully'

if __name__ == '__main__':
    app.run(debug = True)