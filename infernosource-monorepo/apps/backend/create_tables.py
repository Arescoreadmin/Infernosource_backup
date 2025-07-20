from database import Base, engine
import sites.models  # ensures your models are imported!

Base.metadata.create_all(bind=engine)
print("Tables created!")
