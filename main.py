from flask import Flask, render_template, send_file
from gtts import gTTS
from flask_bootstrap import Bootstrap
from forms import InsertText


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jhblugliug;iu;kjb;k'
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    form_1 = InsertText(
    text="Type or copy and paste your text here",
    save_as="<type your file's name followed by .mp3>")
    if form_1.validate_on_submit():
        convert_this = form_1.text.data
        output_path = form_1.save_as.data
        tts = gTTS(text=convert_this, lang='en')
        tts.save(output_path)
    return render_template("index.html", form_1=form_1)


@app.route('/download/<string:my_mp3_file>', methods=['GET', 'POST'])
def download(my_mp3_file):
    return send_file(my_mp3_file, as_attachment=True,  mimetype="audio/ogg")


if __name__ == '__main__':
    app.run(debug=True)

