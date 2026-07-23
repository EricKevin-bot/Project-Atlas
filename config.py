from dataclasses import dataclass


@dataclass
class Config:
    PROJECT_NAME = "Project Atlas"

    OUTPUT_FOLDER = "output"

    AI_PROVIDER = "mock"

    MODEL = "claude-sonnet"

    DEBUG = True


config = Config()