from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from dynamic_price.pipeline.predicition import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Number_of_Riders = int(request.form['Number_of_Riders'])
            Number_of_Drivers = int(request.form['Number_of_Drivers'])
            Location_Category = (request.form['Location_Category'])
            Customer_Loyalty_Status = (request.form['Customer_Loyalty_Status'])
            Number_of_Past_Rides = int(request.form['Number_of_Past_Rides'])
            Average_Ratings = int(request.form['Average_Ratings'])
            Time_of_Booking = (request.form['Time_of_Booking'])
            Vehicle_Type = (request.form['Vehicle_Type'])
            Expected_Ride_Duration = int(request.form['Expected_Ride_Duration'])
            
         
            data = [
                    Number_of_Riders,
                    Number_of_Drivers,
                    Location_Category,
                    Customer_Loyalty_Status,
                    Number_of_Past_Rides,
                    Average_Ratings,
                    Time_of_Booking,
                    Vehicle_Type,
                    Expected_Ride_Duration
                ]
            data = np.array(data).reshape(1,9)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return render_template("results.html")

    else:
        return "Something is wrong"


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)