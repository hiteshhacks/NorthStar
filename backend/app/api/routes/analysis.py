from fastapi import FastAPI,APIRouter
from app.schemas.analysis import AnalysisRequest
import pandas as pd
from app.services.fairness import demographic_parity, disparate_impact

router = APIRouter()


@router.post("/")
def analyze(data: AnalysisRequest):
    file_path = data.file_path
    sensitive = data.sensitive
    target = data.target

    df = pd.read_csv(file_path)

    dp = demographic_parity(df, sensitive, target)
    di = disparate_impact(df, sensitive, target)

    return {
        "demographic_parity": dp,
        "disparate_impact": di
    }