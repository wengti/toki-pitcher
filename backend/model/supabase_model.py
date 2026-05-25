from __future__ import annotations

import datetime
import uuid
from typing import (
    Annotated,
    Any,
    List,
    Literal,
    NotRequired,
    Optional,
    TypeAlias,
    TypedDict,
)

from pydantic import BaseModel, Field, Json

AuthFactorType: TypeAlias = Literal["totp", "webauthn", "phone"]

AuthFactorStatus: TypeAlias = Literal["unverified", "verified"]

AuthAalLevel: TypeAlias = Literal["aal1", "aal2", "aal3"]

AuthCodeChallengeMethod: TypeAlias = Literal["s256", "plain"]

AuthOneTimeTokenType: TypeAlias = Literal["confirmation_token", "reauthentication_token", "recovery_token", "email_change_token_new", "email_change_token_current", "phone_change_token"]

AuthOauthRegistrationType: TypeAlias = Literal["dynamic", "manual"]

AuthOauthAuthorizationStatus: TypeAlias = Literal["pending", "approved", "denied", "expired"]

AuthOauthResponseType: TypeAlias = Literal["code"]

AuthOauthClientType: TypeAlias = Literal["public", "confidential"]

RealtimeEqualityOp: TypeAlias = Literal["eq", "neq", "lt", "lte", "gt", "gte", "in"]

RealtimeAction: TypeAlias = Literal["INSERT", "UPDATE", "DELETE", "TRUNCATE", "ERROR"]

StorageBuckettype: TypeAlias = Literal["STANDARD", "ANALYTICS", "VECTOR"]

class PublicCustomers(BaseModel):
    id: uuid.UUID = Field(alias="id")
    monthly_usage: float = Field(alias="monthly_usage")
    name: str = Field(alias="name")
    pitch: Optional[str] = Field(alias="pitch")
    plan: str = Field(alias="plan")
    tenure_end: datetime.date = Field(alias="tenure_end")
    tenure_start: datetime.date = Field(alias="tenure_start")

class PublicCustomersInsert(TypedDict):
    id: NotRequired[Annotated[uuid.UUID, Field(alias="id")]]
    monthly_usage: Annotated[float, Field(alias="monthly_usage")]
    name: Annotated[str, Field(alias="name")]
    pitch: NotRequired[Annotated[Optional[str], Field(alias="pitch")]]
    plan: Annotated[str, Field(alias="plan")]
    tenure_end: Annotated[datetime.date, Field(alias="tenure_end")]
    tenure_start: Annotated[datetime.date, Field(alias="tenure_start")]

class PublicCustomersUpdate(TypedDict):
    id: NotRequired[Annotated[uuid.UUID, Field(alias="id")]]
    monthly_usage: NotRequired[Annotated[float, Field(alias="monthly_usage")]]
    name: NotRequired[Annotated[str, Field(alias="name")]]
    pitch: NotRequired[Annotated[Optional[str], Field(alias="pitch")]]
    plan: NotRequired[Annotated[str, Field(alias="plan")]]
    tenure_end: NotRequired[Annotated[datetime.date, Field(alias="tenure_end")]]
    tenure_start: NotRequired[Annotated[datetime.date, Field(alias="tenure_start")]]

class PublicPlans(BaseModel):
    download_speed: float = Field(alias="download_speed")
    fttr_price: Optional[float] = Field(alias="fttr_price")
    id: uuid.UUID = Field(alias="id")
    mesh_price: float = Field(alias="mesh_price")
    name: str = Field(alias="name")
    plan_duration_months: Optional[int] = Field(alias="plan_duration_months")
    plan_price: float = Field(alias="plan_price")
    plan_price_promo: Optional[float] = Field(alias="plan_price_promo")
    router: str = Field(alias="router")
    upload_speed: float = Field(alias="upload_speed")

class PublicPlansInsert(TypedDict):
    download_speed: Annotated[float, Field(alias="download_speed")]
    fttr_price: NotRequired[Annotated[Optional[float], Field(alias="fttr_price")]]
    id: NotRequired[Annotated[uuid.UUID, Field(alias="id")]]
    mesh_price: NotRequired[Annotated[float, Field(alias="mesh_price")]]
    name: Annotated[str, Field(alias="name")]
    plan_duration_months: NotRequired[Annotated[Optional[int], Field(alias="plan_duration_months")]]
    plan_price: Annotated[float, Field(alias="plan_price")]
    plan_price_promo: NotRequired[Annotated[Optional[float], Field(alias="plan_price_promo")]]
    router: Annotated[str, Field(alias="router")]
    upload_speed: Annotated[float, Field(alias="upload_speed")]

class PublicPlansUpdate(TypedDict):
    download_speed: NotRequired[Annotated[float, Field(alias="download_speed")]]
    fttr_price: NotRequired[Annotated[Optional[float], Field(alias="fttr_price")]]
    id: NotRequired[Annotated[uuid.UUID, Field(alias="id")]]
    mesh_price: NotRequired[Annotated[float, Field(alias="mesh_price")]]
    name: NotRequired[Annotated[str, Field(alias="name")]]
    plan_duration_months: NotRequired[Annotated[Optional[int], Field(alias="plan_duration_months")]]
    plan_price: NotRequired[Annotated[float, Field(alias="plan_price")]]
    plan_price_promo: NotRequired[Annotated[Optional[float], Field(alias="plan_price_promo")]]
    router: NotRequired[Annotated[str, Field(alias="router")]]
    upload_speed: NotRequired[Annotated[float, Field(alias="upload_speed")]]
