from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/',methods =['GET', 'POST'])
def loginpage():
    if request.method == "POST":
        uname = request.form.get('USERNAME')
        pwd = request.form.get('PASSWORD')
        print(uname,pwd)
    return render_template('Login.html')
@app.route('/reg',methods =["GET", "POST"])
def reg():

        fname = request.form.get('firstname')
        ename = request.form.get('email')
        print(fname)
        print(ename)
        return render_template('reg.html')
if __name__ == "__main__":
    app.run(debug=True)