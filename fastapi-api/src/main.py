from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()

# Importing routers from different modules
from api.regulations import router as regulations_router
from api.rule_engine import router as rule_engine_router
from api.compliance import router as compliance_router

# Including the routers
app.include_router(regulations_router, prefix="/regulations", tags=["Regulations"])
app.include_router(rule_engine_router, prefix="/evaluate", tags=["Rule Engine"])
app.include_router(compliance_router, prefix="/check", tags=["Compliance"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}