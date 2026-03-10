from backend.app.schemas.register import UserDetails,LoginDetails
from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.models.user import User
from backend.app.events.user_events import UserRegistered
from backend.app.events.bus import EventBus
router=APIRouter()
@router.post('/register')
def RegisterUser(user:UserDetails,db:Session=Depends(get_db)):
    new_user = User(**user.model_dump())        
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    EventBus.publish(EventBus,UserRegistered(new_user.id))
    return new_user

@router.post('/login')
def LoginUser(user:LoginDetails,db:Session=Depends(get_db)):
    return db.query(User).filter(User.email==user.email ,User.password_hash==user.password).one_or_none()
