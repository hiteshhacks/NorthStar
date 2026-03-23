from fastapi import FastAPI
from app.api.routes import upload, analysis, explain

app = FastAPI(title="NorthStar AI", version="1.0.0")

app.include_router(upload.router,prefix="/upload")
app.include_router(analysis.router,prefix="/analysis")
app.include_router(explain.router,prefix="/explain")
app.include_router(core_processor.router,prefix="/core_processor")

@app.get("/")
def root():
    return {"message":"NorthStar is running"}