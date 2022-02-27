import pymongo as pymongo

def connectdb():
    client = pymongo.MongoClient("mongodb+srv://natfal:HaA9HeB1nrFcRXTz@cluster0.xz5ni.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    cont = db.continents

    def find_country():
        var = str(input("Please enter word or letter: "))
        for country in countries.find({"Name":{'$regex':var,'$options':'i'}}):
            print(country['Name'])

    find_country()

if __name__ == '__main__':
    connectdb()