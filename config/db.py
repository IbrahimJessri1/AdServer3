
from pymongo import MongoClient
from repositries import generics as gen


conn = MongoClient("mongodb://localhost:27017/AdServer3")


advertisement_collection = conn.AdServer3.advertisement
interactive_advertisement_collection = conn.AdServer3.interactive_advertisement
user_collection = conn.AdServer3.user
role_permission_collection = conn.AdServer3.role_permission

served_ad_collection = conn.AdServer3.served_ad



# advertisement_collection.delete_many({})
# interactive_advertisement_collection.delete_many({})
# served_ad_collection.delete_many({})

#gen.update_many(collection, {}, {"$set" : {"marketing_info.times_served" : 0} })


#print(all_ads[0]["marketing_info"]["max_cpc"])

# advertisement_collection.delete_many({})
# interactive_advertisement_collection.delete_many({})
# served_ad_collection.delete_many({})