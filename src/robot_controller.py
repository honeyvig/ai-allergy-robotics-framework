import time

class ExternalAssistant:
    def deliver_antihistamine_patch(self, location='arm'):
        time.sleep(0.05)
        return {'status':'delivered','route':'topical','location':location}
    def provide_epipen(self):
        time.sleep(0.05)
        return {'status':'ready'}

class ImplantPump:
    def __init__(self):
        self.reserve_ml = 5.0
    def deliver_dose(self, mg=1.0):
        if self.reserve_ml <= 0:
            return {'status':'empty'}
        self.reserve_ml -= mg*0.01
        time.sleep(0.02)
        return {'status':'delivered','remaining_ml': round(self.reserve_ml,2)}
