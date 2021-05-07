from flask import Flask, render_template, request
from get_csv import get_candidates

app = Flask(__name__)

candidates_list = get_candidates.generate_candidates()
print(candidates_list)

@app.route('/')
def index():
    return render_template('index.html', candidates_list = candidates_list)

if __name__ == '__main__':
    app.run()
