from flask import *
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])

def logpage():
    return render_template('log.html')

@app.route('/n1', methods=['GET','POST'])
def next():
    selected_page = request.form.get('page')
    if selected_page == 'page1':
        return render_template('fquiz.html')
    if selected_page == 'page2':
        return render_template('bquiz.html')
    if selected_page == 'page3':
        return render_template('fuquiz.html')

    return render_template('quiztype.html')

@app.route('/front',methods=['POST'])
def quiz1():
    a = "Please select an option for all questions"
    for i in range(1, 6):  # 5 questions
        option_selected = request.form.get(f"q{i}")  # selected option for current question
        if not option_selected:  # if no option selected for current question
            return a
    answer1 = request.form['q1']
    answer2 = request.form['q2']
    answer3 = request.form['q3']
    answer4 = request.form['q4']
    answer5 = request.form['q5']

    score = 0
    if answer1 == 'a':
        score += 1
    if answer2 == 'a':
        score += 1
    if answer3 == 'b':
        score += 1
    if answer4 == 'b':
        score += 1
    if answer5 == 'b':
        score += 1

    return render_template('results.html', score=score)

@app.route('/back',methods=['POST'])
def quiz2():
    a = "Please select an option for all questions"
    for i in range(1, 6):  # 5 questions
        option_selected = request.form.get(f"q{i}")  # selected option for current question
        if not option_selected:  # if no option selected for current question
            return a
    answer1 = request.form['q1']
    answer2 = request.form['q2']
    answer3 = request.form['q3']
    answer4 = request.form['q4']
    answer5 = request.form['q5']

    score = 0
    if answer1 == 'b':
        score += 1
    if answer2 == 'a':
        score += 1
    if answer3 == 'a':
        score += 1
    if answer4 == 'c':
        score += 1
    if answer5 == 'a':
        score += 1

    return render_template('results.html', score=score)

@app.route('/full',methods=['POST'])
def quiz3():
    a = "Please select an option for all questions"
    for i in range(1, 6):  # 5 questions
        option_selected = request.form.get(f"q{i}")  # selected option for current question
        if not option_selected:  # if no option selected for current question
            return a
    answer1 = request.form['q1']
    answer2 = request.form['q2']
    answer3 = request.form['q3']
    answer4 = request.form['q4']
    answer5 = request.form['q5']

    score = 0
    if answer1 == 'c':
        score += 1
    if answer2 == 'c':
        score += 1
    if answer3 == 'a':
        score += 1
    if answer4 == 'c':
        score += 1
    if answer5 == 'c':
        score += 1

    return render_template('results.html', score=score)

if __name__ == "__main__":
    app.run(debug=True,port=2202,host='0.0.0.0')