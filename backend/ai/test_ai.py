import pytest

from ai.pitcher_chain import create_pitcher_chain
from model.model import PitcherPromptModel


def test_pitcher_chain():
    pitcher_chain = create_pitcher_chain()

    pitcher_template_dict = PitcherPromptModel(
        customer_name="Ryan Walker",
        tenure_start="2010-12-28",
        tenure_end="2025-05-28",
        monthly_usage=str(30.46),
        cur_plan_name="Tier 4",
        cur_plan_price=str(99),
        cur_download_speed=str(200),
        cur_upload_speed=str(200),
        new_plan_name="Tier 4",
        new_plan_price=str(99),
        new_download_speed=str(200),
        new_upload_speed=str(200),
        new_plan_duration_months=str(24),
        router="WiFi 6",
        mesh_price="RM 15 per month",
        fttr_price=None,
        promotion=None,
    ).model_dump()

    response = pitcher_chain.invoke(pitcher_template_dict)
    assert type(response.content) == str
