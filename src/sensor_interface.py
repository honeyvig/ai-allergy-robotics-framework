import random

def read_wearable():
    return {'hr': random.randint(60,120),'skin_temp_c': round(32+random.random()*4,2),'scratch_events': random.randint(0,5)}

def read_env():
    return {'pollen_index': random.randint(0,200),'pm2_5': round(random.random()*150,2)}
