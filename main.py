from fastapi import FastAPI
import psycopg2, os, json

app = FastAPI()

@app.get("/district/{district}")
def get_district(district: str):
    # In real version, query Postgres; for demo, return static data
    data = {"district": district, "month": "2025-09",
            "jobs_provided": 1234, "wages_paid": 9876543,
            "pending_payments": 12}
    return data
