from flask import Flask, render_template, request
from get_csv import get_candidates

party_list = ['new Zealand First Party', 'The Oppotunities Party', 'Climate First',
              'National Party', 'Green Party', 'ACT New Zealand', 'Labour Party']

app = Flask(__name__)

app.debug = True

candidates_list = get_candidates.generate_candidates()
print(candidates_list)

@app.route('/')
def index():
    return render_template('index.html', candidates_list = candidates_list, party_list = party_list)

if __name__ == '__main__':
    app.run()
