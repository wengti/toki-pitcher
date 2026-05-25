# Received from the frontend
from openai import BaseModel


class CustomerDataModel(BaseModel):
    id: str
    monthly_usage: float
    name: str
    plan: str
    tenure_end: str
    tenure_start: str
    pitch: str | None


# To be sent to the LLM chain for pitch generation
class PitcherPromptModel(BaseModel):
    customer_name: str
    tenure_start: str
    tenure_end: str
    monthly_usage: str
    cur_plan_name: str
    cur_plan_price: str
    cur_download_speed: str
    cur_upload_speed: str
    new_plan_name: str
    new_plan_price: str
    new_download_speed: str
    new_upload_speed: str
    new_plan_duration_months: str
    router: str
    mesh_price: str | None
    fttr_price: str | None
    promotion: str | None
