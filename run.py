from flask import Flask, render_template, render_template_string, Markup

from script import convert_text_to_html

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5000'


@app.route("/home", methods=['GET'])
def home():
    html = convert_text_to_html('snippet.txt')
    return render_template('snippets.html', html=Markup(html))

app.run(debug=True)
