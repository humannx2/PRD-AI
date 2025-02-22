from fastapi import FastAPI, HTTPException
import json

# Import from main.py
from main import execute_crews, generate_markdown
# Import models
from models import ProductInput, PRDResponse

app = FastAPI(
    title="PRD Generator API",
    description="Generating Product Requirements Documents using AI",
    version="1.0.0"
)

@app.post("/generate-prd", response_model=PRDResponse)
async def generate_prd(product_input: ProductInput):
    try:
        # Execute crews and get PRD output
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 