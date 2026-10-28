import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",

"postgresql://learnity_user:learnity_secret_pass@localhost:5432/learnity_db"
)