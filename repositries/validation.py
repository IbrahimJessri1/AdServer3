
from models.advertisement import AdvertisementInput



class Validator:
    def validate(ad_input : AdvertisementInput):
        mx_cpc = ad_input.max_cpc
        if mx_cpc <= 0:
            return False
        return True