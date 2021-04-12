from flask import Flask
from threading import Thread
# i dont really know what this does because the tutorial i used for this part wasnt very good
app = Flask('')
# i do however know that this is the text on the webpage
@app.route('/')
def home():
    return "I'm alive"
# i dont get the rest of it though
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
