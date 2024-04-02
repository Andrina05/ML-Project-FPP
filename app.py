from flask import Flask,request,render_template
from flask_cors import cross_origin
import pickle
import pandas as pd
import gzip

chunk_size=1024
def model_loader(model_path, chunk_size=107374182):
    with gzip.open(model_path, 'rb') as file:
        buffer = b''
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            buffer += chunk
        model = pickle.loads(buffer)
    return model
model = model_loader("flight_rf.pkl.gz")

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
	return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':
        airline=request.form['airline']
        if(airline=='Vistara'):
            Vistara = 1
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 0
        elif (airline=='Air_India'):
            Vistara = 0
            Air_India = 1
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 0
        elif (airline=='SpiceJet'):
            Vistara = 0
            Air_India = 0
            SpiceJet = 1
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 0
        elif (airline=='GO_FIRST'):
            Vistara = 0
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 1
            Indigo = 0
            AirAsia = 0
        elif (airline=='Indigo'):
            Vistara = 0
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 1
            AirAsia = 0
        elif (airline=='AirAsia'):
            Vistara = 0
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 1

        class1 = request.form['class']
        if(class1 == 'Business'):
            class_business = 1
            class_economy = 0
        elif(class1 == 'Economy'):
            class_business = 0
            class_economy = 1

        Source = request.form["Source"]
        if (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Hyderabad = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore = 0
        elif (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Hyderabad = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore = 0
        elif (Source == 'Hyderabad'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Hyderabad = 1
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore = 0
        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Hyderabad = 0
            s_Mumbai = 0
            s_Chennai = 1
            s_Bangalore = 0
        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Hyderabad = 0
            s_Mumbai = 1
            s_Chennai = 0
            s_Bangalore = 0
        elif(Source == 'Bangalore'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Hyderabad = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore = 1

        Destination = request.form["Destination"]
        if (Destination == 'Kolkata'):
            d_Delhi = 0
            d_Kolkata = 1
            d_Hyderabad = 0
            d_Mumbai = 0
            d_Chennai = 0
            d_Bangalore = 0
        elif (Destination == 'Delhi'):
            d_Delhi = 1
            d_Kolkata = 0
            d_Hyderabad = 0
            d_Mumbai = 0
            d_Chennai = 0
            d_Bangalore = 0
        elif (Destination == 'Hyderabad'):
            d_Delhi = 0
            d_Kolkata = 0
            d_Hyderabad = 1
            d_Mumbai = 0
            d_Chennai = 0
            d_Bangalore = 0
        elif (Destination == 'Chennai'):
            d_Delhi = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_Mumbai = 0
            d_Chennai = 1
            d_Bangalore = 0
        elif (Destination == 'Mumbai'):
            d_Delhi = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_Mumbai = 1
            d_Chennai = 0
            d_Bangalore = 0
        elif(Destination == 'Bangalore'):
            d_Delhi = 0
            d_Kolkata = 0
            d_Hyderabad = 0
            d_Mumbai = 0
            d_Chennai = 0
            d_Bangalore = 1
            
        Departure_time = request.form["Departure_time"]
        if(Departure_time == 'Early_Morning'):
            dep_early_morning = 1
            dep_morning = 0
            dep_afternoon = 0
            dep_evening = 0
            dep_night = 0
            dep_late_night = 0
        elif(Departure_time == 'Morning'):
            dep_early_morning = 0
            dep_morning = 1
            dep_afternoon = 0
            dep_evening = 0
            dep_night = 0
            dep_late_night = 0
        elif(Departure_time == 'Afternoon'):
            dep_early_morning = 0
            dep_morning = 0
            dep_afternoon = 1
            dep_evening = 0
            dep_night = 0
            dep_late_night = 0
        elif(Departure_time == 'Evening'):
            dep_early_morning = 0
            dep_morning = 0
            dep_afternoon = 0
            dep_evening = 1
            dep_night = 0
            dep_late_night = 0
        elif(Departure_time == 'Night'):
            dep_early_morning = 0
            dep_morning = 0
            dep_afternoon = 0
            dep_evening = 0
            dep_night = 1
            dep_late_night = 0
        elif(Departure_time == 'Late_Night'):
            dep_early_morning = 0
            dep_morning = 0
            dep_afternoon = 0
            dep_evening = 0
            dep_night = 0
            dep_late_night = 1

        Arrival_time = request.form["Arrival_time"]
        if(Arrival_time == 'Early_Morning'):
            arr_early_morning = 1
            arr_morning = 0
            arr_afternoon = 0
            arr_evening = 0
            arr_night = 0
            arr_late_night = 0
        elif(Arrival_time == 'Morning'):
            arr_early_morning = 0
            arr_morning = 1
            arr_afternoon = 0
            arr_evening = 0
            arr_night = 0
            arr_late_night = 0
        elif(Arrival_time == 'Afternoon'):
            arr_early_morning = 0
            arr_morning = 0
            arr_afternoon = 1
            arr_evening = 0
            arr_night = 0
            arr_late_night = 0
        elif(Arrival_time == 'Evening'):
            arr_early_morning = 0
            arr_morning = 0
            arr_afternoon = 0
            arr_evening = 1
            arr_night = 0
            arr_late_night = 0
        elif(Arrival_time == 'Night'):
            arr_early_morning = 0
            arr_morning = 0
            arr_afternoon = 0
            arr_evening = 0
            arr_night = 1
            arr_late_night = 0
        elif(Arrival_time == 'Late_Night'):
            arr_early_morning = 0
            arr_morning = 0
            arr_afternoon = 0
            arr_evening = 0
            arr_night = 0
            arr_late_night = 1

        duration_days = int(request.form['duration_days'])
        duration_hours = int(request.form['duration_hours'])
        duration_mins = int(request.form['duration_mins'])

        no_of_stops = int(request.form['no_of_stops'])

        days_left = int(request.form['days_left'])
        
        output = model.predict([
            [days_left, duration_days, duration_hours, duration_mins, no_of_stops,
            AirAsia, Air_India, GO_FIRST, Indigo, SpiceJet, Vistara,
            s_Bangalore, s_Chennai, s_Delhi, s_Hyderabad, s_Kolkata, s_Mumbai, 
            d_Bangalore, d_Chennai, d_Delhi, d_Hyderabad, d_Kolkata, d_Mumbai,
            dep_afternoon, dep_early_morning, dep_evening, dep_late_night, dep_morning, dep_night,
            arr_afternoon, arr_early_morning, arr_evening, arr_late_night, arr_morning, arr_night,
            class_business, class_economy]])

        output = round(output[0],2)
        return render_template('home.html',predictions='Your approximate fare is Rs. {}'.format(output))


if __name__ == '__main__':
	app.run(debug=True)