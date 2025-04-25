from flask import Flask, render_template, request
app = Flask(__name__)




@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/request_example',methods = ['POST', 'GET'])
def request_example():
    result = ""
    result2 = ""
    if request.method == 'POST':
        #password check
        password = request.form.get("check_pass")
        if password:
            result2 = len(password) >= 8
            result2 = "Password is valid" if result else "Password is invalid"
    elif request.method == 'GET':
        #currency conversion
        hkd_value = request.args.get("hkd_value")
        if hkd_value:
            jpy_value = int(hkd_value) * 17
            result = f"{jpy_value:.2f} JPY"
    return render_template("request_example.html", data=result, data2=result2)



if __name__ == '__main__':
    app.debug = True  # setting the debugging option for the application instance
    app.run(host='0.0.0.0', port=5001)
