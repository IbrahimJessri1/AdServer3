
from calendar import c
from uuid import uuid4
from pymongo import MongoClient
from enum import Enum


conn = MongoClient("mongodb://localhost:27017/AdServer")


# admin_permission = ["get_advertiser", "create_advertiser", "delete_advertiser"]

# {
#     "role" : "admin",
#     "permissions" : ["get_advertiser", "create_advertiser", "delete_advertiser"]
# }


# print({"admin_permissions" : admin_permission})


# def get_dict(obj):
#     res = {}
#     for att in dir(obj):
#         if att.startswith('__'):
#             continue
#         value = getattr(obj, att)
#         if type(value).__name__ == 'int':
#             res[att] = str(value)
#         elif type(value).__name__ == 'float':
#             res[att] = str(value)
#         elif type(value).__name__ == 'list':
#             res[att] = value
#         elif type(value).__name__ == 'str':
#             res[att] = value
#         else:
#             res[att] = get_dict(value)
#     return res


# class c(str, Enum):
#     NAME= "name"

# print(type(c).__name__)


# class c:
#     name = 'hi'

# print(dir(c))

# ob = c()

# print(get_dict(c))

# ob = c()
# print(getattr(ob, 'name'))



# # print(dir(ob))
# d = 1
# print(type(d).__name__)


