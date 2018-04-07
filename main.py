from flask import Flask, send_from_directory, url_for, jsonify, render_template, request
import os
import json
from utils import convert_to_date_time, file_len
app = Flask(__name__, static_url_path='')

sample_status_of_sections = [["88942", "OK"], ["89336", "CRASH"], ["88745", "DANGER"]]
sample_section_statistics = [[["2018-04-07 21:19:00", "2018-04-07 21:20:00", "2018-04-07 21:21:00"],["180", "190", "180"]],[["2018-04-07 21:19:00", "2018-04-07 21:20:00", "2018-04-07 21:21:00"],["200", "170", "190"]],[["2018-04-07 21:19:00", "2018-04-07 21:20:00", "2018-04-07 21:21:00"],["60", "70", "80"]],[["2018-04-07 21:19:00", "2018-04-07 21:20:00", "2018-04-07 21:21:00"],["70", "50", "90"]],[["2018-04-07 21:19:00", "2018-04-07 21:20:00", "2018-04-07 21:21:00"],["3", "3", "2"]],[["2018-04-07 21:19:00", "2018-04-07 21:20:00", "2018-04-07 21:21:00"],["4", "5", "2"]]]
#sample_section_statistics = [[] for i in [[["2018-04-07 21:19:00", "180"], ["2018-04-07 21:20:00", "190"], ["2018-04-07 21:21:00", "180"]],[["2018-04-07 21:19:00", "200"], ["2018-04-07 21:20:00", "170"], ["2018-04-07 21:21:00", "190"]],[["2018-04-07 21:19:00", "60"], ["2018-04-07 21:20:00", "70"], ["2018-04-07 21:21:00", "80"]],[["2018-04-07 21:19:00", "70"], ["2018-04-07 21:20:00", "50"], ["2018-04-07 21:21:00", "90"]],[["2018-04-07 21:19:00", "3"], ["2018-04-07 21:20:00", "3"], ["2018-04-07 21:21:00", "2"]],[["2018-04-07 21:19:00", "4"], ["2018-04-07 21:20:00", "5"], ["2018-04-07 21:21:00", "2"]]]]
sample_history = [["2018-03-15 20:00:00", "88942", "DANGER"], ["2018-03-30", "89745", "DANGER"]]
sample_external_statistics = [[["2018-04-07 21:19:00", "180"], ["2018-04-07 21:20:00", "190"], ["2018-04-07 21:21:00", "180"]], [["2018-04-07 21:19:00", "180"], ["2018-04-07 21:20:00", "190"], ["2018-04-07 21:21:00", "180"]], [["2018-04-07 21:19:00", "27"], ["2018-04-07 21:20:00", "28"], ["2018-04-07 21:21:00", "28"]]]

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/api/status_of_sections", methods=['POST'])
def status_of_sections():
    return jsonify(sample_status_of_sections)

@app.route("/api/section_statistics", methods=['POST'])
def section_statistics():
    section_id = request.values.get("id_section")
    readfile = open("/current_datalist/"+section_id+".csv", "r").readlines()
    timestamps = [i[0] for i in readfile]
    consumption_return = [i[1] for i in readfile]
    consumption_supply = [i[2] for i in readfile]
    pressure_return = [i[3] for i in readfile]
    pressure_supply = [i[4] for i in readfile]
    temp_return = [i[5] for i in readfile]
    temp_supply = [i[6] for i in readfile]
    statistics = [[timestamps, temp_supply], [timestamps, temp_return], [timestamps, pressure_supply], [timestamps, pressure_return], [timestamps, consumption_supply], [timestamps, consumption_return]]
    return jsonify(statistics)

@app.route("/api/history", methods=['POST'])
def history():
    return jsonify(sample_history)

@app.route("/api/external_statistics", methods=['POST'])
def external_statistics():
    return jsonify(sample_external_statistics)

@app.route("/api/set_data", methods=['POST'])
def set_data():
    section_id = request.values.get("section_id")
    readfile = open("current_dataset/"+section_id+".csv", "r")
    if file_len("current_dataset/"+section_id+".csv") == 60:
        rendfile = open("current_dataset/"+section_id+".csv", "w")
        readfile.readline()
        readfile.readline()
        for i in range(59):
            write(readfile.readline)
        write(request.values.get("values"))
        rendfile.close()
    else:
        rendfile = open("current_dataset/"+section_id+".csv", "a")
        write(request.values.get("values"))
        rendfile.close()
    return "OK"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

def main():
    app.run()

if __name__ == '__main__':
    main()