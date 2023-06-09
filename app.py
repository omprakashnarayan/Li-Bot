from flask import Flask, render_template, jsonify, request
import processor
import os
import webbrowser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())
@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })
if __name__ == '__main__':
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://localhost:8888/")
    app.run(host='0.0.0.0', port='8888', debug=False)
