# AI Allergy Robotics Framework

Conceptual starter repo for allergy prediction and robotics/implant simulation.
What's included

README.md, LICENSE, requirements.txt, .env.example

data/ — allergies_list.csv, maternal_factors.csv, ai_research_sources.csv (sample)

docs/ — architecture and ethical guidelines

src/ — core modules:

allergy_predictor.py — toy ML predictor (scikit-learn) for child allergy risk

llm_advisor.py — mock LLM advisor returning triage/advice

sensor_interface.py — simulated wearable and environmental sensors

immunology_model.py — toy immune-response simulator (IgE/histamine)

robot_controller.py — simulated external assistant & implant pump

orchestrator.py — demo pipeline tying everything together

app/ — FastAPI demo (app.py) and a minimal HTML UI

notebooks/ — allergy_risk_demo.ipynb, robotics_simulation.ipynb showing how to run the prototypes

How to run locally

Unzip the file.

Create & activate Python venv (3.10+):
