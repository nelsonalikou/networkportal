# app/routers/ports.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils.deps import get_current_user

router = APIRouter(prefix="/ports", tags=["Ports"])

@router.post("/", response_model=schemas.PortResponse)
def create_port(port: schemas.PortCreate, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    db_port = models.Port(**port.dict(), owner_id=user.id)
    db.add(db_port)
    db.commit()
    db.refresh(db_port)
    return db_port

@router.get("/", response_model=list[schemas.PortResponse])
def list_ports(db: Session = Depends(get_db)):
    return db.query(models.Port).all()

@router.get("/{port_id}", response_model=schemas.PortResponse)
def get_port(port_id: int, db: Session = Depends(get_db)):
    port = db.query(models.Port).filter(models.Port.id == port_id).first()
    if not port:
        raise HTTPException(status_code=404, detail="Port not found")
    return port

@router.delete("/{port_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_port(
    port_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    port = db.query(models.Port).filter(models.Port.id == port_id).first()
    if not port:
        raise HTTPException(status_code=404, detail="Port not found")

    # Optional: check if the current user owns the port
    if port.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this port")

    db.delete(port)
    db.commit()
    return