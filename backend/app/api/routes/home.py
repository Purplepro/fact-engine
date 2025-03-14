from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Results, FunFactList

router = APIRouter(tags=["home"])


router.get("/", response_model=Results)

