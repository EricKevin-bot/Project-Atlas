import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    AI_PROVIDER = os.getenv("AI_PROVIDER", "mock")
    MODEL = os.getenv("MODEL", "claude-sonnet-5")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


config = Config()