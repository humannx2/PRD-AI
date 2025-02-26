import streamlit as st
import requests
import json
from typing import Dict, Any
from models import PRDResponse
# Constants
API_BASE_URL = "http://localhost:8000"
GENERATE_ENDPOINT = f"{API_BASE_URL}/generate-prd"
MODIFY_ENDPOINT = f"{API_BASE_URL}/modify-prd"

def init_session_state():
    """Initialize session state variables"""
    if 'generated_prd' not in st.session_state:
        st.session_state.generated_prd = None

def create_input_form() -> Dict[str, Any]:
    """Create and return the input form for PRD generation"""
    with st.form("prd_form"):
        # Basic Information
        st.subheader("Basic Information")
        product_name = st.text_input("Product Name")
        product_objective = st.text_area("Product Objective")
        industry = st.text_input("Industry")
        
        # Target Market
        st.subheader("Target Market")
        target_audience = st.text_input("Target Audience")
        user_persona = st.text_input("User Persona")
        problem_statement = st.text_area("Problem Statement")
        competitor_analysis = st.text_area("Competitor Analysis")
        
        # Features
        st.subheader("Features")
        core_features = st.text_area("Core Features (comma separated)")
        unique_features = st.text_area("Unique Features (comma separated)")
        integrations = st.text_area("Integrations (comma separated)")
        
        # Technical Details
        st.subheader("Technical Details")
        tech_stack = st.text_input("Tech Stack")
        security_compliance = st.text_input("Security Compliance")
        scalability = st.text_input("Scalability")
        
        # Business Details
        st.subheader("Business Details")
        kpi = st.text_area("KPIs (comma separated)")
        business_goals = st.text_area("Business Goals")
        launch_date = st.text_input("Launch Date")
        roadmap = st.text_input("Roadmap")
        budget = st.text_input("Budget")
        
        submit = st.form_submit_button("Generate PRD")
        
        if submit:
            return {
                "PRODUCT_NAME": product_name,
                "PRODUCT_OBJECTIVE": product_objective,
                "INDUSTRY": industry,
                "TARGET_AUDIENCE": target_audience,
                "USER_PERSONA": user_persona,
                "PROBLEM_STATEMENT": problem_statement,
                "COMPETITOR_ANALYSIS": competitor_analysis,
                "CORE_FEATURES": [x.strip() for x in core_features.split(",") if x.strip()],
                "UNIQUE_FEATURES": [x.strip() for x in unique_features.split(",") if x.strip()],
                "INTEGRATIONS": [x.strip() for x in integrations.split(",") if x.strip()],
                "TECH_STACK": tech_stack,
                "SECURITY_COMPLIANCE": security_compliance,
                "SCALABILITY": scalability,
                "KPI": [x.strip() for x in kpi.split(",") if x.strip()],
                "BUSINESS_GOALS": business_goals,
                "LAUNCH_DATE": launch_date,
                "ROADMAP": roadmap,
                "BUDGET": budget
            }
    return None

def generate_prd(data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate PRD using the API"""
    response = requests.post(GENERATE_ENDPOINT, json=data)
    if response.status_code != 200:
        raise Exception(f"Error: {response.text}")
    return response.json()

def modify_prd(raw_data: Dict[str, Any], modification_request: str):
    """Modify PRD using the API"""
    modification_data = {
        "raw_data": raw_data,
        "user_request": modification_request
    }
    try:
        response = requests.post(MODIFY_ENDPOINT, json=modification_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        # response_json = response.json()
        return response
        # return PRDResponse(
        #     markdown=response_json["markdown"],
        #     raw_data=response_json["raw_data"]
        # )
    except requests.exceptions.RequestException as e:
        if response.status_code == 500:
            error_detail = response.json().get('detail', str(e))
            raise Exception(f"Server error: {error_detail}")
        raise Exception(f"Error communicating with server: {str(e)}")

def display_prd(prd_data: Dict[str, Any]):
    """Display PRD in tabs with markdown and raw data views"""
    tabs = st.tabs(["Generated PRD", "Raw Data", "Modify PRD"])
    
    # Generated PRD Tab
    with tabs[0]:
        st.markdown(prd_data["markdown"])
        st.download_button(
            label="Download PRD as Markdown",
            data=prd_data["markdown"],
            file_name="PRD.md",
            mime="text/markdown"
        )
    
    # Raw Data Tab
    with tabs[1]:
        st.json(prd_data["raw_data"])
        st.download_button(
            label="Download Raw Data as JSON",
            data=json.dumps(prd_data["raw_data"], indent=2),
            file_name="PRD_data.json",
            mime="application/json"
        )
    
    # Modify PRD Tab
    with tabs[2]:
        st.write("Modify your PRD by describing the changes you want to make:")
        modification_request = st.text_area(
            "Describe your modifications",
            placeholder="Example: Add a section about security requirements"
        )
        
        if st.button("Apply Modifications"):
            try:
                with st.spinner('Modifying PRD...'):
                    modified_prd = modify_prd(prd_data["raw_data"], modification_request)
                    st.session_state.generated_prd = modified_prd
                    st.success("PRD modified successfully!")
                    st.experimental_rerun()
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

def main():
    st.title("Product Requirement Document Generator")
    st.write("Fill in the details below to generate your PRD")
    
    # Initialize session state
    init_session_state()
    
    # If no PRD has been generated, show the input form
    if st.session_state.generated_prd is None:
        form_data = create_input_form()
        if form_data:
            try:
                with st.spinner('Generating PRD... This may take a few minutes...'):
                    prd_data = generate_prd(form_data)
                    st.session_state.generated_prd = prd_data
                    st.success("PRD generated successfully!")
                    display_prd(prd_data)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        # If PRD exists, show it and modification options
        display_prd(st.session_state.generated_prd)
        
        # Add option to start over
        if st.button("Start Over"):
            st.session_state.generated_prd = None
            st.experimental_rerun()

if __name__ == "__main__":
    main()