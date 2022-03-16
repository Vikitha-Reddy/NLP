import languages
from flask import Flask, render_template, request
from textblob import TextBlob
from langdetect import detect
# from google_trans_new import google_translator
# from googletrans import Translator

app = Flask(__name__)

# print(languages.dict_languages)
# !python -m textblob.download_corpora
# !pip install langdetect

@app.route('/', methods=['GET'])
def dropdown():
    lst_languages = languages.dict_languages.keys()
    return render_template('form.html', lst_languages=lst_languages)

@app.route('/submit', methods = ['POST'])
def form_data():
    # translator = google_translator()
    # translator = Translator()

    input_sent = request.form.get('user_data')
    language_to = request.form.get('language')

    input_language = detect(input_sent)[1]

    if input_language == language_to.lower():
        output1 = (f"Your text is in {language_to} language")
        return render_template('predict.html', data = input_sent,data1 = output1)
    else:
        blob = TextBlob(input_sent)
        value = languages.dict_languages[language_to]
        output = blob.translate(to =value)
            # print(output)
        output1 = (f"Your text is in {language_to} language")
        return render_template('predict.html', data = f'{output} ',data1 = output1)

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5000) for local
    app.run(host='0.0.0.0', port=8080) #for server