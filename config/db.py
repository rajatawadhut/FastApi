from sqlalchemy import create_engine, MetaData
engine = create_engine("mysql+pymysql://root@localhost:3306/lopa")
meta = MetaData()
meta.create_all(bind=engine)
conn = engine.connect()