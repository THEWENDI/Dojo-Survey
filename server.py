from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'what sup?'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit_survey():
    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usercomment'] = request.form['comment']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template("show.html", name_on_template=session['username'], location_on_template=session['userlocation'],language_on_template=session['userlanguage'],comment_on_template=session['usercomment'])

if __name__ == "__main__":
    app.run(debug=True, port = 5001)

