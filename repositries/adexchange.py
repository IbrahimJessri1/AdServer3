from repositries import generics as gen
from models.ssp import Ad_Request, UserInfo
from models.users import Membership, MembershipProbabilities
from models.advertisement import Language, TargetAge
from .utilites import probability_get, rand
from config.db import advertisement_collection, interactive_advertisement_collection, user_collection, served_ad_collection
from models.ssp import ApplyAd
from uuid import uuid4
from .utilites import get_weight_user_info

times_served_weight = 0.1
pay_weight = 0.2
ctr_weight = 0.15
cat_weight = 1.5


def negotiate_interactive(request : Ad_Request):
    ad_collection= interactive_advertisement_collection
    adv_collection = user_collection
    query = {"$and": [{"marketing_info.max_cpc" : {"$gt" : request.min_cpc}}, {"ad_info.type" : request.type.value}]}
    all_ads = gen.get_many(ad_collection, query)
    all_ads_advertisers = []
    for ad in all_ads:
        all_ads_advertisers.append(gen.get_one(adv_collection, {"username" : ad["ad_info"]["advertiser_username"]}))
    normal_ads = []
    premium_ads = []
    vip_ads = []

    for index in range(len(all_ads)):
        if all_ads_advertisers[index]["membership"] == Membership.NORMAL:
            normal_ads.append(all_ads[index])
        elif all_ads_advertisers[index]["membership"] == Membership.PREMIUM:
            premium_ads.append(all_ads[index])
        else:
            vip_ads.append(all_ads[index])
    param = []
    if len(normal_ads) != 0:
        param.append((Membership.NORMAL.value, float(MembershipProbabilities.NORMAL.value)))

    if len(premium_ads) != 0:
        param.append((Membership.PREMIUM.value, float(MembershipProbabilities.PREMIUM.value)))

    if len(vip_ads) != 0:
        param.append((Membership.VIP.value, float(MembershipProbabilities.VIP.value)))


    if len(param) == 0:
        return {"cpc" : 0, "id" : '-1'}
    ad_membership = probability_get(param)
    ad_list = []
    if ad_membership == Membership.NORMAL.value:
        ad_list = normal_ads
    elif ad_membership == Membership.PREMIUM.value:
        ad_list = premium_ads
    else:
        ad_list = vip_ads

    final_ad_list = []
    
    total_times_served = 0
    total_raise_amount = 0



    for index in range(len(ad_list)):
        ad = ad_list[index]
        total_times_served += ad["marketing_info"]["impressions"]
        raise_percentage = rand(ad["marketing_info"]["raise_percentage"] / 2, ad["marketing_info"]["raise_percentage"], 3)
        diff = (ad["marketing_info"]["max_cpc"] - request.min_cpc)
        actual_raise = max(min(ad["marketing_info"]["max_cpc"] - request.min_cpc, request.min_cpc * raise_percentage), rand(diff * 0.2, diff * 0.3, 3))
        total_raise_amount += actual_raise
        final_ad_list.append((index, 0, actual_raise))

    




    for i in range(len(ad_list)):
        ad = ad_list[i]
        res = get_weight_user_info(request.user_info, ad)
        weight_gained = res[0]
        total_weight = res[1]

        if request.categories is not None:
            for cat in request.categories.categories_list:
                total_weight += 1.5
                if cat in ad["categories"]:
                    weight_gained += 1.5

        final_weight = 0
        if total_weight != 0:
            final_weight = weight_gained / total_weight
        if total_times_served != 0:
            final_weight -= (int(ad["marketing_info"]["impressions"]) / total_times_served) * times_served_weight

        ctr = 0
        if ad["marketing_info"]["impressions"] != 0:
            ctr = ad["marketing_info"]["clicks"] / ad["marketing_info"]["impressions"]
        final_weight += ctr * ctr_weight


        final_weight += (final_ad_list[i][2] / total_raise_amount) * pay_weight
        

        final_ad_list[i] = (i, final_weight, final_ad_list[i][2] + request.min_cpc)

    final_ad_list.sort(key= lambda x : x[1], reverse= True)


    return final_ad_list
    





def negotiate(request : Ad_Request):
    ad_collection = advertisement_collection
    adv_collection = user_collection
    query = {"$and": [{"marketing_info.max_cpc" : {"$gt" : request.min_cpc}}, {"ad_info.type" : request.type.value}]}
    all_ads = gen.get_many(ad_collection, query)
    all_ads_advertisers = []
    for ad in all_ads:
        all_ads_advertisers.append(gen.get_one(adv_collection, {"username" : ad["ad_info"]["advertiser_username"]}))
    normal_ads = []
    premium_ads = []
    vip_ads = []

    for index in range(len(all_ads)):
        if all_ads_advertisers[index]["membership"] == Membership.NORMAL:
            normal_ads.append(all_ads[index])
        elif all_ads_advertisers[index]["membership"] == Membership.PREMIUM:
            premium_ads.append(all_ads[index])
        else:
            vip_ads.append(all_ads[index])
    param = []
    if len(normal_ads) != 0:
        param.append((Membership.NORMAL.value, float(MembershipProbabilities.NORMAL.value)))

    if len(premium_ads) != 0:
        param.append((Membership.PREMIUM.value, float(MembershipProbabilities.PREMIUM.value)))

    if len(vip_ads) != 0:
        param.append((Membership.VIP.value, float(MembershipProbabilities.VIP.value)))


    if len(param) == 0:
        return {"cpc" : 0, "ad_id" : '-1'}
    ad_membership = probability_get(param)
    ad_list = []
    if ad_membership == Membership.NORMAL.value:
        ad_list = normal_ads
    elif ad_membership == Membership.PREMIUM.value:
        ad_list = premium_ads
    else:
        ad_list = vip_ads

    final_ad_list = []
    
    total_times_served = 0
    total_raise_amount = 0

    for index in range(len(ad_list)):
        ad = ad_list[index]
        total_times_served += ad["marketing_info"]["impressions"]
        raise_percentage = rand(ad["marketing_info"]["raise_percentage"] / 2, ad["marketing_info"]["raise_percentage"], 3)
        diff = (ad["marketing_info"]["max_cpc"] - request.min_cpc)
        actual_raise = max(min(ad["marketing_info"]["max_cpc"] - request.min_cpc, request.min_cpc * raise_percentage), rand(diff * 0.2, diff * 0.3, 3))
        total_raise_amount += actual_raise
        final_ad_list.append([index, 0, actual_raise])

    for i in range(len(ad_list)):
        ad = ad_list[i]
        res = get_weight_user_info(request.user_info, ad)
        weight_gained = res[0]
        total_weight = res[1]
        
        if request.categories is not None:
            for cat in request.categories.categories_list:
                total_weight += cat_weight
                if cat in ad["categories"]:
                    weight_gained += cat_weight

        final_weight = 0
        if total_weight != 0:
            final_weight = weight_gained / total_weight
        if total_times_served != 0:
            final_weight -= (int(ad["marketing_info"]["impressions"]) / total_times_served) * times_served_weight

        final_weight += (final_ad_list[i][2] / total_raise_amount) * pay_weight
        

        final_ad_list[i] = [i, final_weight, final_ad_list[i][2] + request.min_cpc]

    final_ad_list.sort(key= lambda x : x[1], reverse= True)
    winner_ad = ad_list[final_ad_list[0][0]]
    return {"cpc": final_ad_list[0][2], "ad_id": winner_ad["id"]}
    



def request(ad_apply : ApplyAd):
    ad = gen.get_one(advertisement_collection, {"id" : ad_apply.ad_id})
    gen.update_one(advertisement_collection, {"id" : ad["id"]}, { "$inc": { "marketing_info.impressions": 1 } })
    served_ad = {"id": str(uuid4()), "agreed_cpc": ad_apply.cpc, "ad_id": ad["id"]}
    served_ad_collection.insert_one(dict(served_ad))
    data = {
        "url" : ad["ad_info"]["url"]
    }
    return data