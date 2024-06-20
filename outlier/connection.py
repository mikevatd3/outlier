from sqlalchemy import create_engine

tns_engine = create_engine("postgresql+psycopg2://michael@localhost:5432/investors")
