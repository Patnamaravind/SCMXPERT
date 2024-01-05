import pymongo
dburl="mongodb://localhost:27017"
connection=pymongo.MongoClient(dburl)

projectdb=connection["aravind"]
test=projectdb["test"]
shipment=projectdb["shipmentdata"]
signup=projectdb["signup"]
