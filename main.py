
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Import your existing routers and DB logic
from routes.user_routes import router as user_router
from routes.email_routes import router as email_router
from db import get_db, DATABASE_URL
from models import Base

# 1. Load Environment Variables
load_dotenv()

app = FastAPI()

# 3. CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Include your existing routers
app.include_router(user_router)
app.include_router(email_router)

# 5. Database Setup
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000, reload=True)
