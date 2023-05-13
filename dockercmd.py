import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/axonlogs',methods=['GET', 'POST'])
def ViewLogs():
    logs= []
    if request.method == 'POST':
        log_since = int(request.form['log_since'])
        time_unit = request.form['time_unit']
        logs = GetLog(log_since, time_unit)
        return render_template('logs.html', logs=logs)
    else:
        return render_template('logs.html', logs=logs)

def GetLog(log_since, time_unit):
    logTimeimMin = str(log_since)+time_unit
    output = []
    p = subprocess.Popen("docker logs axon3 --since="+logTimeimMin, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        output.append(line.decode("utf-8").strip())
    return output


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 