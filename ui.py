import streamlit as st
import requests
import json

def main():
    st.title("Product Requirement Data Collection")
    
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
        
        kpis = st.text_area("KPIs (comma separated)")
        business_goals = st.text_area("Business Goals")
        launch_date = st.text_input("Launch Date")
        roadmap = st.text_input("Roadmap")
        budget = st.text_input("Budget")
        
        submit = st.form_submit_button("Submit")
    
    if submit:
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
            "KPIs": [x.strip() for x in kpis.split(",") if x.strip()],
            "BUSINESS_GOALS": business_goals,
            "LAUNCH_DATE": launch_date,
            "ROADMAP": roadmap,
            "BUDGET": budget
        }
        
        st.json(data)
        
        # Send data to backend (Replace 'http://backend-url' with actual API endpoint)
        try:
            response = requests.post("http://backend-url", json=data)
            if response.status_code == 200:
                st.success("Data submitted successfully!")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")

if __name__ == "__main__":
    main()
