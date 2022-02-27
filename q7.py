import pymongo as pymongo

def connectdb():
    client = pymongo.MongoClient("mongodb+srv://natfal:HaA9HeB1nrFcRXTz@cluster0.xz5ni.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    cont = db.continents

    for continents in countries.find({
        'Name':
            {'$regex': 'u', '$options': 'i'}, 'Population': {'$gt': 100000}
    }
    ).sort("population"):
        print(continents['Name'], continents['Population'])

    connectdb()