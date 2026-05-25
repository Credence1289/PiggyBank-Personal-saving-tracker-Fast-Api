from app.db.dbengine import engine
from app.models.models import Base

print("Creating Table......")
Base.metadata.create_all(bind = engine)
print("Table Created")