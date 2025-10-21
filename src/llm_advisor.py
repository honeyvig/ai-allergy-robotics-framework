def advise(patient_info, prediction):
    p = prediction.get('risk_probability',0)
    if p > 0.6:
        level='high'
        advice=['Refer to paediatric allergist','Consider supervised early-introduction protocols','Environmental control measures']
    elif p > 0.3:
        level='moderate'
        advice=['Monitor symptoms','Avoid obvious triggers','Keep a symptom diary']
    else:
        level='low'
        advice=['Routine care','Introduce diverse foods per guidelines']
    return {'patient_id': patient_info.get('id','unknown'),'risk_level': level,'advice': advice,'note':'Mock LLM - validate clinically'}
