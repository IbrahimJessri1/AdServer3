
from calendar import c
from uuid import uuid4
from pymongo import MongoClient
from enum import Enum


conn = MongoClient("mongodb://localhost:27017/AdServer")


admin_permission = ["self_update_user", "update_advertisement", "delete_advertisement", "get_advertisement","delete_user","self_delete_user", "self_get_user", "get_user"]

{
    "role" : "admin",
    "permissions" :admin_permission
}


advertiser_permission = ["self_update_user", "self_delete_user", "self_get_user", "create_ad", "self_delete_ad", "self_update_ad", "self_get_ad", "self_update_account_adv", "self_get_adv"]

{
    "role" : "advertiser",
    "permissions" :advertiser_permission
}
