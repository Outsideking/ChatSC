---

## **2️⃣ ความสามารถของ ChatSC**

- **Chat API** – `/v1/chat`  
  รับข้อความจากผู้ใช้ และตอบกลับข้อความ
- **Search API** – `/v1/search`  
  ค้นหาเอกสาร/ข้อมูล SC, TGN, STW (รองรับ vector search)
- **Bot Factory API** – `/v1/bots`  
  สร้าง bot แชทใหม่
- **ETL Pipeline** – Extract → Transform → Embed & Index  
- **Ingestion Worker** – รับเอกสาร/ข้อความใหม่จากระบบ
- **Embeddings Pipeline** – แปลงเอกสารเป็น vector สำหรับ semantic search
- **Database Integration** – PostgreSQL สำหรับจัดเก็บ documents, bots, history
- **Vector DB Integration** – Milvus สำหรับเก็บ embeddings
- **Feedback Loop** – พัฒนาตัวเองจากข้อความ/เอกสารที่เก็บ

---

## **3️⃣ การติดตั้งและรัน**

### **ความต้องการระบบ**
- Docker >= 24.0
- docker-compose >= 2.0
- Python >= 3.11 (สำหรับรันไฟล์เดียว `chatsc_prod.py`)

### **1. Clone Repo**
```bash
git clone <YOUR_REPO_URL>
cd chatsc_prod
