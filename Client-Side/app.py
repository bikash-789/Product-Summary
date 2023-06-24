from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL, MySQLdb
app = Flask(__name__)
app.secret_key = "caircocoders-ednalan"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'aiproject'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/searching", methods=["POST", "GET"])
def searching():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        search_word = request.form['search_text']
        print(search_word)
        '''if search_word == '':
            query = "SELECT * from employee ORDER BY id"
            cur.execute(query)
            employee = cur.fetchall()
        else:'''
        query = "SELECT * from products WHERE Name LIKE '%{}%' ".format(
                search_word, search_word, search_word)
        cur.execute(query)
        numrows = int(cur.rowcount)
        product = cur.fetchall()
        print(numrows)
        return render_template('response.html', product=product, numrows=numrows, search_word=search_word)
    return render_template('index.html')
    #return jsonify({'htmlresponse': render_template('response.html', employee=employee, numrows=numrows)})
if __name__ == "__main__":
    app.run(debug=True)