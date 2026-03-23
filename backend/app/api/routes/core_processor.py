from fastapi import FastAPI, APIRouter, File, UploadFile,HTTPException
import pandas as pd 
import os 
from app.services.fairness import demographic_parity, disparate_impact
from app.services.llm import prompt_builder,Client,MODEL
from app.schemas.analysis import AnalysisRequest

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

client = Client

@router.post("/")
async def full_analysis(data: AnalysisRequest):
    file_path = data.file_path
    sensitive = data.sensitive
    target = data.target

    try:
        file_path = f"{UploadFile}/{file.filename}"
        with open(file_path,"wb")as f:

            f.write(await file.read())
        df = pd.read_csv(file_path)

        if sensitive not in df.colums or target not in df.columns:

            raise HTTPException(status_code=400,details="invalid column")

            dp = demographic_parity(df,sensitive,target)
            di = disparate_impact(df,sensitive,target)

            prompt = prompt_builder(dp,di)

            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role":"system","content":prompt}
                ],
                temperature=0.3
            )

            llm_output = response.choices[0].message.content

            return {
                "demographic_parity":dp,
                "disparate_impact":di,
                "explanation":llm_output
            }

    except Exception as e:
        raise HTTPException(status_code=500,details=str(e))