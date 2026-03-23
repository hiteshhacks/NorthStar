from fastapi import APIRouter,HTTPException
from app.schemas.explain import ExplainRequest
from app.services.llm import Client, MODEL, prompt_builder

 

client  = Client

router = APIRouter()

 
@router.post("/")
def explain_bias(data: ExplainRequest):
    try:
        dp = data.demographic_parity
        di = data.disparate_impact

        prompt = prompt_builder(dp,di)

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role":"system", "content":"You are a AI Ethics Expert"},
                {"role":"user", "content":prompt}
            ],
            temperature=0.3
        )

        llm_output = response.choices[0].message.content


        return {
            "analysis":llm_output,
            "input_metrics":{
                "demographic_parity":dp,
                "disparate_impact":di
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





    

     