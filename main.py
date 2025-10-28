from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is live!", "status": "OK"}

@app.get("/districts")
def get_districts():
    data = [
        {"district": "Ahmedabad", "performance": 85},
        {"district": "Surat", "performance": 90},
        {"district": "Rajkot", "performance": 75}
    ]
    return {"data": data}
