"""启动 Flask 并自动打开浏览器"""
import os, webbrowser, threading, time
from flask import Flask, send_from_directory
from backend.api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('frontend', filename)

def open_browser():
    time.sleep(0.5)
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    threading.Thread(target=open_browser, daemon=True).start()
    app.run(debug=False, port=5000)