from fastapi import APIRouter

router = APIRouter()

from .regulations import router as regulations_router
from .rule_engine import router as rule_engine_router
from .compliance import router as compliance_router

router.include_router(regulations_router, prefix="/regulations", tags=["regulations"])
router.include_router(rule_engine_router, prefix="/evaluate", tags=["rule_engine"])
router.include_router(compliance_router, prefix="/check", tags=["compliance"])