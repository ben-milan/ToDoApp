from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from datetime import datetime

# sorts a CSV file after the criteria "priority"
def CSVFileData(dataFile):
    data = []
    with open(dataFile, mode="r") as dataFile:
        reader = csv.reader(dataFile)
        for row in reader:
            if len(row) >= 5:
                title = row[0]
                priority = row[1]
                date = row[2]
                time = row[3]
                description = row[4]
                data.append({"title": title, "priority": priority, "date": date, "time": time, "description": description})
            else:
                print("Skipping row: ", row)
    
    priority_order = {"High": 1, "Medium": 2, "Normal": 3, "Low": 4}
    
    sorted_data = sorted(data, key=lambda x: priority_order[x["priority"]])
            
    return sorted_data

# returns the number of entrys in a csv file
def fileLength(dataFile):
    counter = 0
    with open(dataFile, mode="r") as dataFile:
        reader = csv.reader(dataFile)
        for row in reader:
            counter += 1
        return counter

def createEntries(self, title, priority, date, time, description):
    entry = QtWidgets.QWidget(self.toDo_list)
    entry.setGeometry(QtCore.QRect(10, 30 + len(self.entries) * 50, 591, 41))
    entry.setLayoutDirection(QtCore.Qt.LeftToRight)
    entry.setObjectName("entry")
        

# functions for the creation of the buttons
def createButton(parent, text, geometry, stylesheet, auto_default=False, object_name=None):
    button = QtWidgets.QPushButton(parent)
    button.setGeometry(geometry)
    button.setStyleSheet(stylesheet)
    button.setAutoDefault(auto_default)
    if object_name:
        button.setObjectName(object_name)
    button.setText(text)
    return button
def getButtonProperties(dataFile):
    id = 0
    data = CSVFileData(dataFile)
    dates = []
    for row in data:
        dates.append(row["date"])
    
    height = 10
    button_properties = []
    rowCount = fileLength(dataFile)
    for i in range(0, rowCount):
        date_string = dates[id]
        date_object = datetime.strptime(date_string, "%d.%m.%Y")
        current_date = datetime.now()
        time_until_today = date_object - current_date
        
        if time_until_today.days <= 0:
            color="#9e2b1e"
        elif time_until_today.days > 0 and time_until_today.days <= 3:
            color="#EF820D"
        else:
            color="#fff200"
        
        button_properties.append({"text": "Button " + str(id), "geometry": QtCore.QRect(500, height, 75, 31), "stylesheet": "QPushButton {\n""background-color: "+ color +";\n""border: 1px solid white;\n""}\n"})
        id += 1
        height += 40
    return button_properties

data = CSVFileData("./data/todoData.csv");
print(data)