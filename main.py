# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/submit", response_model=schemas.FormData)
def create_form_data(form_data: schemas.FormDataCreate, db: Session = Depends(get_db)):
    # Validate form data
    if not form_data:
        raise HTTPException(status_code=400, detail="Invalid form data")
    
    # Save form data to the database
    try:
        db_form_data = models.FormData(**form_data.dict())
        db.add(db_form_data)
        db.commit()
        db.refresh(db_form_data)
        return db_form_data
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to save form data")

# Handle OPTIONS requests for the /submit endpoint
@app.options("/submit")
async def options_submit():
    return {"allow": "POST"}

