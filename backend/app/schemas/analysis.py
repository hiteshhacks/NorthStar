from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    file_path: str
    sensitive:str
    target: str