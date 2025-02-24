from crewai import Task
from agents import (tech_spec_agent, success_metrics_agent, final_compiler_agent, 
                   user_requirements_agent, feature_definition_agent, 
                   prd_analyzer_agent, prd_modifier_agent)
from models import PRDOutput


#User Requirements Task
user_requirements_task = Task(
    description="""Based on this data, and make a comprehensive list for other agents to work on.
      - Product Name: {PRODUCT_NAME}
      - Objective: {PRODUCT_OBJECTIVE}
      - Industry/Niche: {INDUSTRY}
      - Target Audience: {TARGET_AUDIENCE}
      - User Persona: {USER_PERSONA}
      - Problem Statement: {PROBLEM_STATEMENT}
      - Competitor Analysis:{COMPETITOR_ANALYSIS}
      - Core Features: {CORE_FEATURES}
      - Unique Selling Points (USPs): {UNIQUE_FEATURES}
      - Integrations: {INTEGRATIONS}
      - Tech Stack: {TECH_STACK}
      - Security & Compliance: {SECURITY_COMPLIANCE}
      - Scalability Considerations: {SCALABILITY}
      - Success Metrics & KPIs: {KPI}
      - Business Goals: {BUSINESS_GOALS}
      - Launch Date: {LAUNCH_DATE}
      - Development Roadmap: {ROADMAP}
      - Budget Allocation: {BUDGET}""",
    agent=user_requirements_agent, 
    expected_output="A comprehensive list of all the user requirements compiled to help other agents"
)

#Feature Definition Task
feature_definition_task = Task(
    description="""
    Define and structure the product's core features.  
    Using the provided requirements:
      - Identify MVP features and their importance.
      - Highlight full-scale features beyond MVP.
      - Explain how the features solve the problem statement.
      - Map out the user journey based on the user persona.
      - Define competitive advantages over existing solutions.
    Ensure the feature list aligns with business objectives.
    """,
    agent=feature_definition_agent,
    expected_output="A detailed list of all the objectives defined in the description"
)

# Technical Specifications Task
tech_spec_task = Task(
    description="""
    Provide detailed technical specifications.  
    Define:
      -Frontend & Backend Technologies: {{TECH_STACK}}
      -APIs & Integrations: {{INTEGRATIONS}}
      -Security & Compliance Standards: {{SECURITY_COMPLIANCE}}
      -Scalability Strategies: {{SCALABILITY}}
      -Infrastructure & Hosting Recommendations  
    Ensure the technical decisions align with the product's goals.
    """,
    agent=tech_spec_agent,
    expected_output="A detailed list of all the objectives defined in the description"
)

#Success Metrics Task
success_metrics_task = Task(
    description="""
    Define measurable success criteria for the product.  
    Establish:
      -Key Performance Indicators (KPIs)
      -User Retention & Growth Metrics 
      -Monetization & ROI Expectations
      -Market Adoption Strategy
    
    Use the following information to define the metrics:
    User Requirements: {USER_REQUIREMENTS}
    Feature Definition: {FEATURE_DEFINITION}
    Technical Specifications: {TECH_SPECS}
    
    Ensure all success metrics are realistic and aligned with industry standards.
    """,
    agent=success_metrics_agent,
    expected_output="A detailed list of all the objectives defined in the description"
)

# Final PRD Compilation Task
final_compiler_task = Task(
    description="""
    Compile all sections into a structured PRD.  
    Merge outputs from:
      - User Requirements: {USER_REQUIREMENTS}
      - Feature Definitions: {FEATURE_DEFINITION}
      - Technical Specifications: {TECH_SPECS}
      - Success Metrics: {SUCCESS_METRICS}    
    
    Create a well-structured Markdown document with the following format:
    
    # [Product Name] - Product Requirements Document
    
    ## Executive Summary
    [Brief overview of the product and its main objectives]
    
    ## Problem Statement & Objectives
    [Detail the problem being solved and key objectives]
    
    ## Target Market & User Personas
    [Describe the target audience and user personas]
    
    ## Product Features
    ### Core Features
    [List and describe core features]
    
    ### Unique Selling Points
    [Highlight unique features and competitive advantages]
    
    ## Technical Specifications
    [Detail the technical implementation requirements]
    
    ## Success Metrics & KPIs
    [List measurable success criteria]
    
    ## Timeline & Milestones
    [Outline development phases and key dates]
    
    ## Risks & Mitigation Strategies
    [Identify potential risks and mitigation plans]
    
    Ensure the final PRD meets industry standards and is ready for stakeholders.
    """,
    agent=final_compiler_agent,
    expected_output="A complete, well-structured PRD document in Markdown format",
    # output_file="PRD.md",
    output_json=PRDOutput,
    # output_format="markdown"
)

# PRD Analysis Task
prd_analysis_task = Task(
    description="""
    Analyze the existing PRD and user modification request.
    
    PRD Content:
    {prd_content}
    
    User Request:
    {user_request}
    
    Identify:
    1. Which sections need to be modified
    2. How the modifications affect other sections
    3. What content should remain unchanged
    """,
    agent=prd_analyzer_agent,
    expected_output="Analysis of required modifications and affected sections"
)

# PRD Modification Task
prd_modification_task = Task(
    description="""
    Modify the PRD based on the analysis and user request.
    
    Original PRD:
    {prd_content}
    
    User Request:
    {user_request}
    
    Analysis Results:
    {analysis_result}
    
    Requirements:
    1. Only modify identified sections
    2. Maintain consistency with unchanged sections
    3. Ensure modifications align with overall PRD objectives
    """,
    agent=prd_modifier_agent,
    expected_output="Modified PRD with requested changes",
    output_json=PRDOutput
)

