from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.utils import secure_filename
import os
import pandas as pd
from agent import get_agent_response

app = Flask(__name__)
app.secret_key = "ai-analyst-secret"
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            df = pd.read_csv(filepath)
            session['csv'] = df.to_json()  # store df as JSON
            session['chat_history'] = []
            return redirect('/chat')
        else:
            return "Please upload a valid CSV file."
    return '''
        <!doctype html>
        <title>Upload CSV</title>
        <h1>Upload your CSV file</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
    '''

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'csv' not in session:
        return redirect('/')

    df = pd.read_json(session['csv'])
    chat_history = session.get('chat_history', [])
    mode = request.form.get('mode', 'agent')

    if request.method == 'POST':
        question = request.form['question']
        answer = get_agent_response(df, question)
        chat_history.append((question, answer))
        session['chat_history'] = chat_history

    return render_template('chat.html', chat_history=chat_history, mode=mode)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)