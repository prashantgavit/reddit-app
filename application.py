from flask import *
from utils.reddit_fetch import get_reddit_data

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    # request1 = dict(request.form)
    subreddit = request.form['subreddit']
    startdate = request.form['startdate']
    enddate = request.form['enddate']
    data = get_reddit_data(startdate, enddate, subreddit)
    resp = make_response(data.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=reddit_data.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
    return render_template(print("Data is gettting processed"))


@app.route('/')
def start_page():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
