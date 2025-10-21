from src.allergy_predictor import AllergyPredictor
from src.llm_advisor import advise
from src.sensor_interface import read_wearable, read_env
from src.immunology_model import simulate_exposure
from src.robot_controller import ExternalAssistant

def run_demo(patient_info):
    ap = AllergyPredictor()
    pred = ap.predict(patient_info)
    advice = advise(patient_info,pred)
    wearable = read_wearable()
    env = read_env()
    exposure = env['pollen_index']/100.0
    immune = simulate_exposure(exposure, baseline_sensitivity=0.5 + 0.3*patient_info.get('maternal_allergy',0))
    actions = []
    if immune['histamine_index'] > 30:
        assist = ExternalAssistant()
        actions.append(assist.deliver_antihistamine_patch())
    return {'prediction': pred, 'advice': advice, 'wearable': wearable, 'env': env, 'immune': immune, 'actions': actions}

if __name__=='__main__':
    demo = {'id':'p1','maternal_allergy':1,'paternal_allergy':0,'early_eczema':1,'urban_residence':1,'sibling_allergy':0}
    print(run_demo(demo))
