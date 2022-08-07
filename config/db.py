
from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017/AdServer")

collection = conn.AdServer.role_permission



admin_permission = ["self_update_user", "update_advertisement", "delete_advertisement", "get_advertisement","delete_user","self_delete_user", "self_get_user", "get_user"]

#collection.insert_one(
{
    "role" : "admin",
    "permissions" :admin_permission
}
#)

advertiser_permission = ["self_update_user", "self_delete_user", "self_get_user", "create_ad", "self_delete_ad", "self_update_ad", "self_get_ad", "self_update_account_adv", "self_get_adv"]


#collection.insert_one(
{
    "role" : "advertiser",
    "permissions" :advertiser_permission
}
#)


###add admin
# admin = User(username='admin1', password=hashing.Hash.bcrypt('123'), role='admin', create_date=str(datetime.datetime.now()))
# conn.AdServer.user.delete_many({"role" : 'admin'})
# conn.AdServer.user.insert_one(dict(admin))