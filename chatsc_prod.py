# chatsc_prod.py
from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import json
import psycopg2
from datetime import datetime

# =======================
# Config
# =======================
DB_CONFIG = {
    "host": "db",
    "port": 5432,
    "database": "chatsc_prod",
    "user": "chatsc",
    "password": "chatsc123"
}

VECTOR_DB_CONFIG = {
    "host": "vector_db",
    "port": 19530
}

# =======================
# DB Helpers
# =======================
def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def insert_document(title, source, metadata={}):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO documents (title, source, created_at, updated_at, metadata) VALUES (%s,%s,%s,%s,%s) RETURNING id",
        (title, source, datetime.utcnow(), datetime.utcnow(), json.dumps(metadata))
    )
    doc_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return doc_id

# =======================
# FastAPI App
# =======================
app = FastAPI(title="ChatSC Production API")

class SearchRequest(BaseModel):
    query: str
    sources: list = []

@app.post("/v1/search")
async def search(req: SearchRequest):
    results = [{"title": "Demo Result", "source": "SC"}]
    return {"query": req.query, "results": results}

@app.post("/v1/chat")
async def chat(message: dict):
    text = message.get("text", "")
    return {"response": f"Received message: {text}"}

@app.post("/v1/bots")
async def create_bot(bot: dict):
    bot_id = str(uuid.uuid4())
    return {"bot_id": bot_id, "status": "created"}

# =======================
# ETL Pipeline
# =======================
def extract_documents():
    print("Extracting documents from SC/TGN/STW...")

def transform_documents():
    print("Cleaning and transforming documents...")

def embed_and_index():
    print("Generating embeddings and indexing to Vector DB...")

def run_etl():
    extract_documents()
    transform_documents()
    embed_and_index()

# =======================
# Ingestion Worker
# =======================
def ingestion_worker():
    print("Ingestion worker running...")

# =======================
# Embeddings Pipeline
# =======================
def embeddings_pipeline():
    print("Embeddings pipeline running...")

# =======================
# Bot Factory
# =======================
def bot_factory():
    print("Bot factory: creating new bots...")

# =======================
# Demo Execution
# =======================
if __name__ == "__main__":
    print("Starting ChatSC Production Simulation...")
    run_etl()
    ingestion_worker()
    embeddings_pipeline()
    bot_factory()
    print("FastAPI ready. Run: uvicorn chatsc_prod:app --reload --host 0.0.0.0 --port 8000")
