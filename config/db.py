from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017/AdServer")



admin_permission = ["get_advertiser", "create_advertiser", "delete_advertiser"]

{
    "role" : "admin",
    "permissions" : ["get_advertiser", "create_advertiser", "delete_advertiser"]
}


print({"admin_permissions" : admin_permission})


