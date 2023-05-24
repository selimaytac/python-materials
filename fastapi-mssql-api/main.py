from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import pyodbc

app = FastAPI()

# Veritabanı bağlantısı için gerekli bilgiler
# server = "server_adı"
# database = "veritabanı_adı"
# username = "kullanıcı_adı"
# password = "şifre"

# # Veritabanı bağlantısını oluşturma
# conn = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}")

# Veritabanı bağlantısı için gerekli bilgiler
server = "localhost"
database = "NewDatabase"
trusted_connection = "no"

# Veritabanı bağlantısını oluşturma
conn = pyodbc.connect(f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection={trusted_connection};")


cursor = conn.cursor()

# CRUD operasyonları için kullanılacak modeller
class Item(BaseModel):
    id: int
    name: str
    description: str

# Veri ekleme
@app.post("/items/")
def create_item(item: Item):
    try:
        cursor.execute("INSERT INTO items (id, name, description) VALUES (?, ?, ?)",
                       item.id, item.name, item.description)
        conn.commit()
        return {"message": "Item created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Tüm verileri getirme
@app.get("/items/")
def get_all_items():
    try:
        cursor.execute("SELECT * FROM items")
        rows = cursor.fetchall()
        items = []
        for row in rows:
            item = {
                "id": row.id,
                "name": row.name,
                "description": row.description
            }
            items.append(item)
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Veri getirme
@app.get("/items/{item_id}")
def get_item(item_id: int):
    try:
        cursor.execute("SELECT * FROM items WHERE id = ?", item_id)
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Item not found.")
        item = {
            "id": row.id,
            "name": row.name,
            "description": row.description
        }
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Veri güncelleme
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    try:
        cursor.execute("UPDATE items SET name = ?, description = ? WHERE id = ?",
                       item.name, item.description, item_id)
        conn.commit()
        return {"message": "Item updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Veri silme
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    try:
        cursor.execute("DELETE FROM items WHERE id = ?", item_id)
        conn.commit()
        return {"message": "Item deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
