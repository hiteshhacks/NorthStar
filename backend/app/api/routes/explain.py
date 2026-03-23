from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def explain_bias(data: dict):
    metrics = data["metrics"]

    # Later connect Grok / LLaMA
    explanation = f"""
    The model shows bias based on the given metrics.
    Demographic Parity varies across groups.
    Disparate Impact indicates potential unfairness.
    """

    return {
        "explanation": explanation,
        "suggestions": [
            "Rebalance dataset",
            "Use fairness-aware algorithms",
            "Remove sensitive attribute influence"
        ]
    }