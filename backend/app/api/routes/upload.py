from fastapi import FastAPI, APIRouter, UploadFile, File
import pandas as pd
import os

router = APIRouter()

UPLOAD_DIR="uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)

@router.post("/")
async def upload_file(file:UploadFile=File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"


    with open(file_path,"wb") as f:
        f.write(await file.read())


    df = pd.read_csv(file_path)

    return {
        "filename":file.filename,
        "columns":list(df.columns),
        "rows":df.shape[0],
        "file_path":file_path
    }