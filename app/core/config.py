from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    HOST: str
    PORT: int

    VERIFY_TOKEN: str

    META_ACCESS_TOKEN: str
    PHONE_NUMBER_ID: str
    GRAPH_API_VERSION: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()        