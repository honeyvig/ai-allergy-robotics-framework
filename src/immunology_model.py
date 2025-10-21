import random

def simulate_exposure(allergen_conc, baseline_sensitivity=0.5):
    response = allergen_conc * baseline_sensitivity * (1+random.random()*0.5)
    IgE = min(100, 10 + response*20)
    hist = min(100, response*30)
    return {'IgE_u_ml': round(IgE,2),'histamine_index': round(hist,2)}
