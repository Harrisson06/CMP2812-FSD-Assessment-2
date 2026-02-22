from itertools import product
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional

from app.Routers.Corrections_notice import router as Corrections_router 
Corrections_router.include_router(Corrections_router, prefix="/api", tags=["Corrections"])

app = FastAPI()

# Pydantic model to define the schema of the data for PUT, POST, & DELETE
class Products(BaseModel):
    ProductID: int
    Name: str


@app.get("/")
def root():
    return {"message": "CMP2812 Full Stack Development Assessment 2"}