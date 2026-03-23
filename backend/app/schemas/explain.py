from fastapi import FastAPI
from pydantic import BaseModel

class ExplainRequest(BaseModel):
    demographic_parity:dict
    disparate_impact:float