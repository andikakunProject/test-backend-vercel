
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "Flask berjalan di Vercel!"}

@app.get("/api/hello")
def hello():
    return {
        "message": "Halo dari Python!",
        "status": "success"
    }

