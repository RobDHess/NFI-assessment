from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json

from .api_utils import run_main

app = FastAPI()


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.post("/process")
async def process_file(file: UploadFile):
    """Process the uploaded JSON file and return the results."""
    try:
        # Load the JSON content
        content = await file.read()
        data = json.loads(content)

        # Validate input structure
        if "spoor" not in data or "profielen" not in data:
            raise HTTPException(
                status_code=400,
                detail="Invalid JSON structure. Requires 'spoor' and 'profielen'.",
            )

        # Extract data
        spoor = data["spoor"]
        profielen = data["profielen"]

        # Validate input types
        if not isinstance(spoor, str):
            raise HTTPException(status_code=400, detail="'spoor' must be a string.")

        if not isinstance(profielen, list) or not all(
            isinstance(p, str) for p in profielen
        ):
            raise HTTPException(
                status_code=400, detail="'profielen' must be a list of strings."
            )

        # Process each profiel
        results = run_main(spoor, profielen)

        # Return the result as JSON
        return JSONResponse(content=results)

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
