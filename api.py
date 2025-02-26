from fastapi import FastAPI, HTTPException
import json

# Import from main.py
from main import execute_crews, generate_markdown
# Import models
from models import ProductInput, PRDResponse, ModificationRequest
from prd_modifier import modify_prd

app = FastAPI(
    title="PRD Generator API",
    description="Generating Product Requirements Documents using AI",
    version="1.0.0"
)

@app.post("/generate-prd", response_model=PRDResponse)
async def generate_prd(product_input: ProductInput):
    try:
        # Execute crews and get PRD output
        if product_input is None:
            raise HTTPException(
                status_code=400,
                detail="Product input is required"
            )
        prd_output = execute_crews(dict(product_input))
        prd_data = json.loads(prd_output.raw)

        # Generate markdown
        markdown_output = generate_markdown(prd_data)

        return PRDResponse(
            markdown=markdown_output,
            raw_data=prd_data
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating PRD: {str(e)}"
        )

@app.post("/modify-prd", response_model=PRDResponse)
async def modify_prd_endpoint(modification_request: ModificationRequest):
    try:
        if modification_request is None:
            raise HTTPException(
                status_code=400,
                detail="Modification request is required"
            )
        
        if not modification_request.raw_data:
            raise HTTPException(
                status_code=400,
                detail="PRD data is required. Please first generate a PRD using the /generate-prd endpoint"
            )
        
        # Get the modified PRD data
        # in json
        modified_prd = modify_prd(
            modification_request.raw_data,
            modification_request.user_request
        )
        
        # Generate markdown for the modified PRD
        markdown_output = generate_markdown(modified_prd)
        
        # Return the response in the correct format
        return {
            "markdown": markdown_output,
            "raw_data": modified_prd
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error modifying PRD: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 