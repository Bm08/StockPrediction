from calendar import month
from msilib.schema import tables
from flask import Flask, render_template, request
import pandas as pd
import pickle 
app = Flask(__name__)
model = pickle.load(open('Arima_Model.pkl','rb')) #read mode
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        months = int(request.form["monthselection"])
       
        if months == 1:
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=3)[0]
            time_index = [['2022-06-01','2022-09-01', '2022-12-01']]
            df = pd.DataFrame(forecast, columns=['P/E Ratio'], index = time_index)
            # time_index = [['2022-06-01','2022-09-01', '2022-12-01']]
            # df = df.join(time_index)
            # df.set_index('Date', inplace= True)

        elif months == 2:
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=6)[0]
            time_index = [['2022-06-01','2022-09-01', '2022-12-01', '2023-03-01', '2023-06-01', '2023-09-01']]
            df = pd.DataFrame(forecast, columns=['P/E Ratio'], index= time_index)       
            # df = df.join(time_index)
            # df.set_index('Date', inplace= True)

        elif months == 3:
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=9)[0]
            time_index = [['2022-06-01','2022-09-01', '2022-12-01', '2023-03-01', '2023-06-01', '2023-09-01', '2023-12-01', '2024-03-01', '2024-06-01']]
            df = pd.DataFrame(forecast, columns=['P/E Ratio'], index= time_index) 
            # df = df.join(time_index)
            # df.set_index('Date', inplace= True)

        elif months == 4:
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=12)[0]
            time_index = [['2022-06-01','2022-09-01', '2022-12-01', '2023-03-01', '2023-06-01', '2023-09-01', '2023-12-01', '2024-03-01', '2024-06-01', '2024-09-01', '2024-12-01', '2025-03-01']]
            df = pd.DataFrame(forecast, columns=['P/E Ratio'], index= time_index) 
            # df = df.join(time_index)
            # df.set_index('Date', inplace= True)

        output =df
        return render_template("index.html", prediction_text= 'Prediction' + 'is$ {}'.format(output))
        # return render_template("index.html", tables=[df.to_html()])
if __name__ == "__main__":
    app.run(debug=True)