from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# STEP 2: LOAD MODEL
model = joblib.load('models/tennis_model.joblib')
encoders = joblib.load('models/encoders.joblib')

class TennisInput(BaseModel):
    outlook: str
    temperature: str
    humidity: str
    wind: str

# STEP 3: THE ROUTE 
@app.get('/')
def home():
    return {'Message':"Backend worked."}

@app.post("/predict")
async def predict_tennis(data: TennisInput):
    # Encoding the text data into numbers
    input_features = [
        encoders['Outlook'].transform([data.outlook])[0],
        encoders['Temperature'].transform([data.temperature])[0],
        encoders['Humidity'].transform([data.humidity])[0],
        encoders['Wind'].transform([data.wind])[0]
    ]
    
    prediction = model.predict([input_features])[0]
    result = encoders['PlayTennis'].inverse_transform([prediction])[0]
    
    return {"play_tennis": result}

