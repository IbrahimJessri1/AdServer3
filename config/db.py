
from pymongo import MongoClient
from repositries import generics as gen


conn = MongoClient("mongodb://localhost:27017/AdServer")


advertisement_collection = conn.AdServer3.advertisement
interactive_advertisement_collection = conn.AdServer3.interactive_advertisement
user_collection = conn.AdServer3.user
role_permission_collection = conn.AdServer3.role_permission

served_ad_collection = conn.AdServer3.served_ad



#gen.update_many(collection, {}, {"$set" : {"marketing_info.times_served" : 0} })


#print(all_ads[0]["marketing_info"]["max_cpc"])

