from fastapi import FastAPI

app = FastAPI(
    title="law Contracts API",
    description="AI-powered Contract Analysis using Gemini",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "app": "Law Contracts API",
        "version": "1.0.0",
        "endpoint": {
            "POST /contract/upload": "Upload a PDF or TXT contract for analysis",
            "GET /contracts/": "Retrive details of specific contract by ID",
            "POST /anlysis/analyse/{contract_id}": "Analyze a contract using AI and return insights",
            "GET /anlysis/{contract_id}": "Retrieve a contract using AI and return insights",
            "GET /anlysis/contract/{contract_id}": "Retrieve a list of all analysis performed for a specific contract",
        }
    }