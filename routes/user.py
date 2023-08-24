from fastapi import APIRouter


router = APIRouter()
@router.post('/login')
def login():
    return 1

@router.get('/logout')
def logout():
    return exit