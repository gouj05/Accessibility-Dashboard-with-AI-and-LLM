from fastapi import FastAPI
from database import Base, engine
from routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from routes import extension
from translator import translate_text
from modelsT import TranslateRequest
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(extension.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return {"status": "Translator API running"}


@app.post("/translate")
def translate(req: TranslateRequest):

    translated = translate_text(req.text, req.target_lang)

    return {
        "translated": translated
    }