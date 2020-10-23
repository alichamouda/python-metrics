import psutil
from flask import Flask, render_template, json
import os

my_memory_application = Flask(__name__)

@my_memory_application.route('/metrics')
def getMemoryPercentage():
   data=dict()
   data['memory_usage']=str(psutil.virtual_memory().percent)
   response = my_memory_application.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
   return response

@my_memory_application.route('/')
def getHome():
   return render_template("welcome.html")

if __name__ == '__main__':
   my_memory_application.run(host='0.0.0.0', port='8080')