from pydantic import BaseModel


class NebulaUserAPIAuthorizationTokenResponseModel(BaseModel):
    token: str
