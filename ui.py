import streamlit as st
import requests
import json

def main():
    st.title("Product Requirement Document Generator")
    st.write("Fill in the details below to generate your PRD")
    
    with st.form("prd_form"):
        product_name = st.text_input("Product Name")
        product_objective = st.text_area("Product Objective")
        industry = st.text_input("Industry")
        target_audience = st.text_input("Target Audience")
        user_persona = st.text_input("User Persona")
        problem_statement = st.text_area("Problem Statement")
        competitor_analysis = st.text_area("Competitor Analysis")
        
        core_features = st.text_area("Core Features (comma separated)")
        unique_features = st.text_area("Unique Features (comma separated)")
        integrations = st.text_area("Integrations (comma separated)")
        
        tech_stack = st.text_input("Tech Stack")
        security_compliance = st.text_input("Security Compliance")
        scalability = st.text_input("Scalability")
        
        kpi = st.text_area("KPIs (comma separated)")
        business_goals = st.text_area("Business Goals")
        launch_date = st.text_input("Launch Date")
        roadmap = st.text_input("Roadmap")
        budget = st.text_input("Budget")
        
        submit = st.form_submit_button("Generate PRD")
    
    if submit:
        # Show loading spinner while processing
        with st.spinner('Generating PRD... This may take a few minutes...'):
            data = {
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
            
            try:
                # Send request to our FastAPI endpoint
                response = requests.post("http://localhost:8000/generate-prd", json=data)
                
                if response.status_code == 200:
                    response_data = response.json()
                    
                    # Create tabs for different views
                    tab1, tab2 = st.tabs(["Generated PRD", "Raw Data"])
                    
                    with tab1:
                        st.markdown(response_data["markdown"])
                        # Add download button for markdown
                        st.download_button(
                            label="Download PRD as Markdown",
                            data=response_data["markdown"],
                            file_name="PRD.md",
                            mime="text/markdown"
                        )
                    
                    with tab2:
                        st.json(response_data["raw_data"])
                        # Add download button for JSON
                        st.download_button(
                            label="Download Raw Data as JSON",
                            data=json.dumps(response_data["raw_data"], indent=2),
                            file_name="PRD_data.json",
                            mime="application/json"
                        )
                    
                    st.success("PRD generated successfully!")
                else:
                    st.error(f"Error: {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Failed to connect to the API. Please make sure the API server is running.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
