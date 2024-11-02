from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str

    class Config:
        env_file = ".env"

    @classmethod
    def __post_root_validators__(cls):
        cls.access_token_expire_minutes = int(cls.access_token_expire_minutes)



settings = Settings()
