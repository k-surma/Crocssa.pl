import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://crocssa:crocssa@localhost:5432/crocssa"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    CORS_HEADERS = "Content-Type"
