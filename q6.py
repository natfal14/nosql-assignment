import pymongo as pymongo

def connectdb():
    client = pymongo.MongoClient("mongodb+srv://natfal:HaA9HeB1nrFcRXTz@cluster0.xz5ni.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    cont = db.continents

    def poporder():
        for country in countries.find({}).sort("Population"):
            print(country['Name'], country['Population'])

    poporder()