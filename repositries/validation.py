
from models.advertisement import AdvertisementInput



class Validator:
    def validate(ad_input : AdvertisementInput):
        mx_cpc = ad_input.marketing_info.max_cpc
        mn_cpc = ad_input.marketing_info.min_cpc
        if mx_cpc <= 0 or mn_cpc <= 0 or mn_cpc > mx_cpc:
            return False
        return True