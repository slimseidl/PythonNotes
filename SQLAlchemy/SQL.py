from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///testDB.db")

conn = engine.connect()

conn.execute(text("""
             Create table if not exists users(
             id Integer Primary KEy autoincrement,
             name Text,
             age Integer)"""))


conn.execute(text("Insert into users (name, age) Values ('John', 29)"))
conn.execute(text("INSERT INTO users (name, age) VALUES ('Alice', 25)"))

conn.commit()

result = conn.execute(text("SELECT * From users"))
for row in result:
    print(row)