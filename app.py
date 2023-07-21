import time
from flask import Flask

app=Flask(__name__)

START=time.time()

def elapsed():
    running=time.time() -START
    minutes,seconds=divmod(running,60)
    return seconds

@app.route("/")
def route():
    return "hello all %d" %elapsed()
    
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)