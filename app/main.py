from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.llm_client import generate_from_local_llm
from app.prompt_builder import build_prompt
from app.rule_engine import normalize_output
from app.storage import init_db, save_prescript, get_recent_prescripts

app = FastAPI(title="Prescript Pager")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 开发阶段先这样，后面再收紧
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PrescriptRequest(BaseModel):
    mode: str = "ritual"

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "Prescript engine is running"}

@app.post("/generate")
def generate_prescript(req: PrescriptRequest):
    history = get_recent_prescripts(limit=10)
    prompt = build_prompt(req.mode, history)
    raw = generate_from_local_llm(prompt)
    text = normalize_output(raw)

    save_prescript(text, req.mode)
    return {
        "prescript": text,
        "mode": req.mode
    }