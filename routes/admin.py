from fastapi import APIRouter




router = APIRouter()


@router.get('/admin_info')
def admin_info():
    return 1

@router.post('/change_pwd')
def change_pwd():
    return 1