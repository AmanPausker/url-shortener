from fastapi import FastAPI, Depends, HTTPException

from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import models
import schemas

from database import engine, SessionLocal
from utils import generate_short_code

#Create database Tables

models.Base.metadata.create_all(bind = engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Home route
@app.get("/")
def home():
    return {"message":"URL shortener backend"}

#Shortend URl Route
@app.post("/shorten")
def shorten_url(request:schemas.URLRequest, db:Session = Depends(get_db)):
    short_code = generate_short_code()

    new_url = models.url(
        short_code = short_code,
        original_url = request.url
    )
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {"short_url": f"http://localhost:8000/{short_code}"}
@app.get("/{short_code}")
def redirect_url(short_code:str, db:Session = Depends(get_db)):

    url_entry = db.query(models.url).filter(models.url.short_code == short_code).first()
    if not url_entry:
        raise HTTPSException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url = url_entry.original_url)