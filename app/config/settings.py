from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    GROQ_API_KEY: str

    LLM_MODEL: str = "openai/gpt-oss-20b"

    EMBEDDING_MODEL: str = (
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    CHUNK_SIZE: int = 800

    CHUNK_OVERLAP: int = 100

    VECTOR_DB_PATH: str = "vectorstore/faiss_index"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()