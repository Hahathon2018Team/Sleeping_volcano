from flask import Flask,send_from_directory, url_for, jsonify
import os
app = Flask(__name__, static_url_path='')

sample_status_of_sections = [["88942", "OK"], ["89336", "CRASH"], ["88745", "DANGER"]]
sample_section_statistics = [[["2018-04-07 21:19:00", "180"], ["2018-04-07 21:20:00", "190"], ["2018-04-07 21:21:00", "180"]],[["2018-04-07 21:19:00", "200"], ["2018-04-07 21:20:00", "170"], ["2018-04-07 21:21:00", "190"]],[["2018-04-07 21:19:00", "60"], ["2018-04-07 21:20:00", "70"], ["2018-04-07 21:21:00", "80"]],[["2018-04-07 21:19:00", "70"], ["2018-04-07 21:20:00", "50"], ["2018-04-07 21:21:00", "90"]],[["2018-04-07 21:19:00", "3"], ["2018-04-07 21:20:00", "3"], ["2018-04-07 21:21:00", "2"]],[["2018-04-07 21:19:00", "4"], ["2018-04-07 21:20:00", "5"], ["2018-04-07 21:21:00", "2"]]]
sample_history = [["2018-03-15 20:00:00", "88942", "DANGER"], ["2018-03-30", "89745", "DANGER"]]
sample_external_statistics = [[["2018-04-07 21:19:00", "180"], ["2018-04-07 21:20:00", "190"], ["2018-04-07 21:21:00", "180"]], [["2018-04-07 21:19:00", "180"], ["2018-04-07 21:20:00", "190"], ["2018-04-07 21:21:00", "180"]], [["2018-04-07 21:19:00", "27"], ["2018-04-07 21:20:00", "28"], ["2018-04-07 21:21:00", "28"]]]

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/status_of_sections", methods=['POST'])
def status_of_sections():
    return jsonify(sample_status_of_sections)

@app.route("/api/section_statistics", methods=['POST'])
def section_statistics():
    return jsonify(sample_section_statistics)

@app.route("/api/history", methods=['POST'])
def history():
    return jsonify(sample_history)

@app.route("/api/external_statistics", methods=['POST'])
def external_statistics():
    return jsonify(sample_external_statistics)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

def main():
    app.run()

if __name__ == '__main__':
    main()