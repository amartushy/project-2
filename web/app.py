"""
Adrian Martushev's Flask API.
"""


from flask import Flask, send_from_directory
import os
import configparser

app = Flask(__name__)

@app.route("/")
def hello():
   return "UOCIS docker demo!\n"



@app.route('/<path:filename>')
def serve_file(filename):
    if ".." in filename or "~" in filename:
        return send_from_directory('pages', '403.html'), 403
    if os.path.exists(f'pages/{filename}'):
        return send_from_directory('pages', filename), 200
    else:
        return send_from_directory('pages', '404.html'), 404

if __name__ == '__main__':
    config = configparser.ConfigParser()
    if os.path.exists('credentials.ini'):
        config.read('credentials.ini')
    else:
        config.read('default.ini')

    port = int(config.get('SERVER', 'PORT'))
    debug_mode = config.getboolean('SERVER', 'DEBUG')

    app.run(host='0.0.0.0', port=port, debug=debug_mode)



