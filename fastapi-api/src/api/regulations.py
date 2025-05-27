from fastapi import APIRouter

router = APIRouter()

@router.get("/regulations/{regulation_id}/sections/{section_id}")
async def get_regulation_section(regulation_id: str, section_id: str):
    return {"regulation_id": regulation_id, "section_id": section_id}

@router.get("/regulations/search")
async def search_regulations(query: str, classification_level: str):
    return {"query": query, "classification_level": classification_level}