import psutil
from flask import Flask, render_template
import os

my_memory_application = Flask(__name__)

@my_memory_application.route('/metrics')
def getMemoryPercentage():
   return render_template("ram_metrics.html",value=str(psutil.virtual_memory().percent))

@my_memory_application.route('/')
def getHome():
   return render_template("welcome.html")

if __name__ == '__main__':
   my_memory_application.run(port='8080')