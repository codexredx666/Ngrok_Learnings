from fastapi import APIRouter

router = APIRouter()

@router.get("/email")
def send_email():
    return {"message": "Email routes working"}
