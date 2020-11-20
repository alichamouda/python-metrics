
import psutil
from flask import Flask, render_template, json, request
import os
import factoriel

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

@my_memory_application.route('/factoriel/<number>')
def getFactorialOf(number):
   factorial_arg = factoriel.Factorial_type.ITERATIVE
   if request.args.get('mode') is not None:
      factorial_arg = factoriel.Factorial_type.ITERATIVE if int(request.args.get('mode')) == 1 else factoriel.Factorial_type.RECURSIVE

   response = my_memory_application.response_class(
        response=json.dumps(factoriel.factorial_of(int(number),factorial_arg)),
        status=200,
        mimetype='application/json'
    )
   return response

@my_memory_application.route('/')
def getHome():
   return render_template("welcome.html")

if __name__ == '__main__':
   my_memory_application.run(host='0.0.0.0', port='8080')