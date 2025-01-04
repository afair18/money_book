from dotenv import load_dotenv
import os

# .env 파일 로드 (한 번만 수행)
load_dotenv()

# 환경 변수
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"
SERPERAPI_SECRET = os.getenv("SERPERAPI_SECRET")

# 유효성 검사 (옵션)
if not all([DATABASE_URL, SECRET_KEY, SERPERAPI_SECRET]):
    raise ValueError("Some essential environment variables are missing.")