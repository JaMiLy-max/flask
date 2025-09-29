# Flask 설정 파일
import os

# 현재 파일의 절대 경로를 기준으로 루트 디렉토리를 계산
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
# instance 폴더가 없으면 생성
os.makedirs(INSTANCE_DIR, exist_ok=True) 

class Config:
    # 절대 경로를 사용하여 데이터베이스 URI를 명확하게 지정
    DB_PATH = os.path.join(INSTANCE_DIR, "reviews.db")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")


# # instance 폴더 경로
# INSTANCE_DIR = os.path.join(os.path.dirname(__file__), "..", "instance")

# # 폴더가 없으면 생성 (해당 디렉토리가 기존에 존재하면 에러발생 없이 넘어가고, 없을 경우에만 생성)
# # False (default) -> exist_ok를 True로 설정하지 않았을 때 이미 해당 디렉토리가 존재하는 경우에는 exception에러
# os.makedirs(INSTANCE_DIR, exist_ok=True)

# class Config:
#     """환경 설정 (로컬 SQLite 기본값)"""
#     # 민감한 데이터 숨김에 사용 -> env
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/reviews.db")
