from flask import Flask,request,jsonify,render_template,send_file
app = Flask(__name__)
app.config["DEBUG"]=True
from optimize import Optimize
import json
@app.route('/',methods=["GET","POST"])
def home():
    return render_template('index2.html')

@app.route('/portfolio',methods=["GET","POST"])
def portfolio():
    stocks = str(request.form['stock'])
    stocks = [x.strip() for x in stocks.split(',')]
    output= Optimize(stocks,'full')
    return render_template('portfolio.html',data={'stockNames':stocks,\
                                                 'output':output['allocation'],\
                                                 'maxSharpe':output['maxSharpeRatio'],\
                                                 'stockData':output['stockData']})
                                        

if __name__ == '__main__':
    app.run()
