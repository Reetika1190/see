from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ritika@12345'
app.config['MYSQL_DB'] = 'FP'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':

        userDetails = request.form
    
        name = userDetails['name']
        id = userDetails['id']

        course = userDetails['course']
        no = userDetails['no']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, id) VALUES (%s, %s)", (name, id))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('student.html')

@app.route('/course', methods=['GET', 'POST'])
def course():
    if request.method == 'POST':


    
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO myuser(course, no) VALUES ( %s, %s)", (course, no))
        
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('course.html')
    return redirect(url_for('users'))
    


    
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    userDetails = cur.fetchall()
    return render_template('users.html')
    cur.close()
      
    
if __name__ == '__main__':
    app.run(debug=True)




