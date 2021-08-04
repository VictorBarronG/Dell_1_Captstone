from flask import Flask, request, render_template
import pickle
import Dictionary as Dict 


app = Flask(__name__)
# temp value - to be filled in
numColumns = 1137



data_columns = ['Pclass', 'Age', 'Sibsp', 'Parch', 'Fare', 'Gender','Area of Town']
@app.route('/',methods=["GET","POST"])
def home():
    message = "Welcome to my flask based web application ... !!!"
    return render_template("home.html", message = message, data_columns=data_columns)

trim = 'default trim value!'
# global trimNum
@app.route('/changedTrim',methods=['GET', 'POST'])
def changedTrim():
    data = request.get_data();
    trim=str(data)[2:-1]
    global trimNum 
    trimNum = Dict.trimsDict[trim]
    return 'changedTrim route success'


@app.route('/getResponseLinearReg',methods=["GET","POST"])
def getResponseLinearReg():
    Year = request.form["Year"]
    Make = request.form["Make"]
    Model = request.form["Model"]
    Trim = trimNum
    City = request.form["City"]
    Engine = request.form["Engine"]
    Fuel = request.form["FuelType"]
    Color = request.form["Color"]
    Transmission = request.form["Transmission"]
    Wheel = request.form["WheelSystem"]
    BodyType = request.form["BodyType"]
    Owners = request.form["Owners"]
    Horsepower = request.form["Horsepower"]
    Mileage = request.form["Mileage"]
    MaxSeats = request.form["MaxSeating"]
    Fleet = request.form["Fleet"]
    FrameDamage = request.form["FrameDamage"]
    IsCab = request.form["IsCab"]
    HasAccidents = request.form["HasAccidents"]
    Salvage = request.form["Salvage"]
    Theft = request.form["Theft"]
    
    list = [0] * numColumns

    list[0] = int(City)
    list[1] = int(Fleet)
    list[2] = int(FrameDamage)
    list[3] = int(HasAccidents)
    list[4] = int(Horsepower)
    list[5] = int(IsCab)
    list[6] = int(MaxSeats)
    list[7] = int(Mileage)
    list[8] = int(Owners)
    list[9] = int(Salvage)
    list[10] = int(Theft)
    list[11] = int(Trim)
    list[12] = int(Year)
    list[Dict.columnDict[BodyType]] = 1
    list[Dict.columnDict[Make]] = 1
    list[Dict.columnDict[Model]] = 1
    list[Dict.columnDict[Engine]] = 1
    list[Dict.columnDict[Fuel]] = 1
    list[Dict.columnDict[Color]] = 1
    list[Dict.columnDict[Transmission]] = 1
    list[Dict.columnDict[Wheel]] = 1

    with open("GBR.sav", 'rb') as file:
            pickle_model = pickle.load(file)
            y_pred_from_pkl = pickle_model.predict([list])
    print(y_pred_from_pkl)
    return str(round(y_pred_from_pkl[0], 2))
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)