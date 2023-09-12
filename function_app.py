import azure.functions as func
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from WrapperFunction import app as fastapi_app


class RecommendationModel(BaseModel):
    text: str
    type: str 



app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)


@app.post('/send_recommendations')
async def send_data(recommendations: List[RecommendationModel]):
    
    response_data = []

    for rec in recommendations:
        text_to_print = rec.text
        text_type =rec.type

        if text_type == "person":
            recommendation = f"test passed!"
        else:
            recommendation = f"test also passed, but not a person"

        response_data.append({"text": text_to_print, "recommendation": recommendation})

    return {"status": 200, "recommendations": response_data}
    # return print("test passed!")
