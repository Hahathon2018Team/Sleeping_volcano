from flask import Flask, send_from_directory, url_for, jsonify, render_template, request
import os
import json
from utils import convert_to_date_time, file_len
app = Flask(__name__, static_url_path='')

sample_status_of_sections = [["89793", "OK"], ["89336", "CRASH"], ["89808", "DANGER"]]
ids = ["88942", "89336", "89520", "89589", "89600", "89604", "89639", "89655", "89667", "89709", "89726", "89730", "89731", "89751", "89758", "89760", "89781", "89783", "89788", "89791", "89792", "89793", "89806", "89808", "89815"]
sample_history = [["2018-03-15 20:00:00", "89793", "DANGER"], ["2018-03-30", "89745", "DANGER"]]
sample_external_statistics = [[["2018-04-07 21:19:00", "180"], ["2018-04-07 21:20:00", "190"], ["2018-04-07 21:21:00", "180"]], [["2018-04-07 21:19:00", "180"], ["2018-04-07 21:20:00", "190"], ["2018-04-07 21:21:00", "180"]], [["2018-04-07 21:19:00", "27"], ["2018-04-07 21:20:00", "28"], ["2018-04-07 21:21:00", "28"]]]

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/api/status_of_sections", methods=['POST'])
def status_of_sections():
    sections_statuses = []
    for i in ids:
        sections_statuses += [[i, "OK"]]
    print(sections_statuses)
    return jsonify(sections_statuses)

@app.route("/api/section_statistics", methods=['POST'])
def section_statistics():
    section_id = request.values.get("section_id")
    readfile = open("current_dataset/"+section_id+".csv", "r").readlines()
    timestamps = []
    consumption_return = []
    consumption_supply = []
    pressure_return = []
    pressure_supply = []
    temp_return = []
    temp_supply = []
    for line in readfile: 
        line = [i for i in line.split(',')]
        timestamps += [line[0]]
        temp_supply += [line[6]]
        temp_return += [line[5]]
        pressure_supply += [line[4]]
        pressure_return += [line[3]]
        consumption_supply += [line[2]]
        consumption_return += [line[1]]
    statistics = [[timestamps, temp_supply], [timestamps, temp_return], [timestamps, pressure_supply], [timestamps, pressure_return], [timestamps, consumption_supply], [timestamps, consumption_return]]
    return jsonify(statistics)

@app.route("/api/history", methods=['POST'])
def history():
    return jsonify(sample_history)

@app.route("/api/external_statistics", methods=['POST'])
def external_statistics():
    readfile = open("current_dataset/weatheer.csv", "r").readlines()
    timestamps = []
    return_temp = []
    supply_temp = []
    temperature = []
    for line in readfile: 
        line = [i for i in line.split(',')]
        timestamps += [line[0]]
        return_temp += [line[1]]
        supply_temp += [line[2]]
        temperature += [line[3]]
    statistics = [[timestamps, temperature], [timestamps, supply_temp], [timestamps, return_temp]]
    return jsonify(sample_external_statistics)

@app.route("/api/set_data", methods=['POST'])
def set_data():
    section_id = request.values.get("section_id")
    file_ = open("current_dataset/"+section_id+".csv")
    if file_len("current_dataset/"+section_id+".csv") == 60:
        file_.readline()
        for i in range(59):
            write(file_.readline())
        file_.write(request.values.get("values"))
        file_.close()
    else:
        file_ = open("current_dataset/"+section_id+".csv", "a")
        file_.write(request.values.get("values"))
        file_.close()
    return "OK"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

def main():
    app.run()

if __name__ == '__main__':
    main()