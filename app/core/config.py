from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL:AnyUrl = Field(..., env="DB_URL")
    SECRET_KEY:str = Field(..., env="SECRET_KEY")
    ALGORITHM:str = Field("HS356", env="ALGORITHM")
    LOG_TOKEN: str = Field(..., env="LOG_TOKEN")
    ACCESS_TOKEN_EXPIRY_MIN: int = Field(30, env="ACCESS_TOKEN_EXPIRY_MIN")
    class Config:
        env_file=".env"
        case_sensitive = True

settings = Settings()