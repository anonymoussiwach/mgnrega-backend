from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (Vercel) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later you can restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is live!", "status": "OK"}

@app.get("/districts")
def get_districts():
    # dummy example endpoint — replace later with your real logic
    data = [
        {"district": "Ahmedabad", "performance": 85},
        {"district": "Surat", "performance": 90},
        {"district": "Rajkot", "performance": 75}
    ]
    return {"data": data}
