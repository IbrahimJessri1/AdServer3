
from pymongo import MongoClient
from repositries import generics as gen


conn = MongoClient("mongodb://localhost:27017/AdServer")


collection = conn.AdServer.advertisement


all_ads = gen.get_many(collection,{"marketing_info.max_cpc" : {"$gte" : 1.2}})


#print(all_ads[0]["marketing_info"]["max_cpc"])



