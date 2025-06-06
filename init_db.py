from app import db
from models import User  # 必要なモデルを import

db.create_all()
print("✅ Database initialized.")