import pymongo as pymongo

def connectdb():
    client = pymongo.MongoClient("mongodb+srv://natfal:HaA9HeB1nrFcRXTz@cluster0.xz5ni.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    cont = db.continents

    countries.update_one({'Name': 'Canada'}, {'$set': {'Population': 37742154}})
    countries.update_one({'Name': 'China'}, {'$set': {'Population': 1439323776}})
    countries.update_one({'Name': 'Egypt'}, {'$set': {'Population': 105516428}})
    countries.update_one({'Name': 'France'}, {'$set': {'Population': 65273511}})
    countries.update_one({'Name': 'USA'}, {'$set': {'Population': 334210037}})




if __name__ == '__main__':
    connectdb()