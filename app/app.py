from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from src.orchestrator import run_demo
import uvicorn
app = FastAPI(title='AI Allergy Robotics Demo')
class Patient(BaseModel):
    id: str
    maternal_allergy: int = 0
    paternal_allergy: int = 0
    early_eczema: int = 0
    urban_residence: int = 1
    sibling_allergy: int = 0

@app.get('/', response_class=HTMLResponse)
def home():
    return open('app/templates/index.html','r').read()

@app.post('/api/run')
def run(p: Patient):
    return run_demo(p.dict())

if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
