import csv
import numpy as np

def getDataSource(data_path):
    marks= []
    Days_Present= []
    with open(data_path ) as f:
        df = csv.DictReader(f)
        for i in df:
            marks.append(float(i["Marks"]))
            Days_Present.append(float(i["Days_Present"]))
            
    return {"x":marks,"y":Days_Present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation)

def setup():
    data_path = "./data.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()


    