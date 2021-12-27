import time

from flask import g, Flask


from database import db
from api.api import bp as api_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)


@app.route('/health', methods=['GET'])
def health():
    return 'ok'


app.register_blueprint(api_bp, url_prefix='/api')


@app.before_request
def before():
    g.start = time.time()
    print("This is executed BEFORE each request.")


@app.after_request
def after(response):
    response_time = time.time() - g.start
    print("This is executed after each request.", response_time)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
