import pymongo as pymongo

def connectdb():
    client = pymongo.MongoClient("mongodb+srv://natfal:HaA9HeB1nrFcRXTz@cluster0.xz5ni.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    cont = db.continents

    def continents():
        agg = [
            {
                '$project': {
                    'name': "$name",
                    'countries': {'$size': "$countries"}}
            }
        ]
        cont = countries.aggregate(agg)
        for continent in cont:
            print(continent)

    continents()


if __name__ == '__main__':
    connectdb()