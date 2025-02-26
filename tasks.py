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
    Compile all sections into a highly detailed and structured Product Requirements Document (PRD). 
    Merge outputs from:
      - User Requirements: {USER_REQUIREMENTS}
      - Feature Definitions: {FEATURE_DEFINITION}
      - Technical Specifications: {TECH_SPECS}
      - Success Metrics: {SUCCESS_METRICS}

    Create a thorough, cohesive, and well-structured Markdown document with the following detailed format:

    # [Product Name] - Product Requirements Document

    ## Executive Summary
    Provide a clear, concise yet **comprehensive overview** of the product, its main objectives, and **expected market impact**. 
    - Explain what makes the product unique, highlighting the main problem it addresses and why this solution is vital. 
    - Include a **vision statement** for the product and its place in the market.
    - Specify any **major milestones** or timelines for expected product success and growth.

    ## Problem Statement & Objectives
    Describe in **detail the problem** the product is solving:
    - Identify **user pain points** and **market challenges** in a thorough way (supported by data or research if possible).
    - Link these pain points to specific features or outcomes from the product.
    - Articulate clear **product objectives** and how they align with the business's broader goals, ensuring they are **measurable** and **impactful**.
    - Explain how the product's success will be defined. Include both **short-term goals** and **long-term vision**.
    
    ## Target Market & User Personas
    Provide a **detailed breakdown** of the target market:
    - Define **demographics**, **psychographics**, and **behavioral data** of the target audience.
    - Describe each **user persona** in detail. Each persona should include:
      - **Background information**: Age, profession, location, etc.
      - **Goals and motivations**: What are they looking for in this product?
      - **Challenges and pain points**: What obstacles are they facing that the product solves?
      - **User journey**: Describe how each persona interacts with the product, from discovery to regular use.
    - Identify **user needs** and explain how these needs map directly to the product features.

    ## Product Features
    ### Core Features
    List and describe each **core feature** in detail, ensuring each is aligned with the product’s objectives:
    - Break down each feature into actionable items, including user stories or use cases to make them relatable.
    - Explain **why** each feature is necessary for solving the user’s problems or fulfilling their needs.
    - Prioritize the features, clearly distinguishing **MVP features** from **future enhancements**.
    - Provide **wireframes or mockups** (if available), or detailed descriptions of how users will interact with each feature.

    ### Unique Selling Points (USPs)
    Identify and highlight the **unique features** that set this product apart from competitors:
    - Compare these features directly with competitors’ products, explaining why your product is superior.
    - Include a **competitive analysis** that shows why your product fills gaps in the current market.
    - Describe **competitive advantages** (e.g., faster, more intuitive, cheaper, more secure, etc.) in clear, comparative terms.
    - Emphasize features that target **early adopters** and niche audiences for initial traction.

    ## Technical Specifications
    Detail the **technical requirements** for implementing the product:
    - Address the **scalability** of the product, describing how it can handle a growing user base.
    - Define **performance requirements** for responsiveness and system speed.
    - Highlight **security requirements** (encryption, authentication, data privacy) and compliance with standards like GDPR, SOC2.
    - Provide a technical breakdown of **integration points** (third-party services, APIs), including details of the data exchange, authentication protocols, and any other technical dependencies.
    - Discuss **technical challenges** or potential risks, and outline the **mitigation strategies**.
    - Explain the **platform** (e.g., cloud-based, on-premise) and the **tech stack** (languages, frameworks, databases, etc.).

    ## Success Metrics & KPIs
    Define **measurable success metrics** to evaluate product performance:
    - List **leading KPIs** (e.g., user adoption rate, NPS score, feature engagement) and **lagging KPIs** (e.g., revenue, retention rate, customer lifetime value).
    - For each metric, define a **target value** and the **timeframe** for achieving it.
    - Explain how each metric ties back to the **business goals** and **user objectives**.
    - Provide a **measurement plan** that outlines how success will be tracked over time, including tools, platforms, and teams responsible for monitoring.

    ## Timeline & Milestones
    Provide a **detailed timeline** for product development:
    - Break down the development process into clear **phases**, including planning, MVP development, testing, and full-scale release.
    - Include specific **milestones** with target dates (e.g., MVP completion, Beta testing, Full product launch).
    - Add **dependencies** (e.g., tech stack finalization, hiring needs, third-party integrations) and any **critical path** items that may delay the product.
    - Outline the **resources** required for each phase, including team members and budgets.

    ## Risks & Mitigation Strategies
    Identify all **risks** that could affect product success:
    - Include **market risks**, such as competition, shifting customer preferences, or changing regulations.
    - Identify **technical risks**, like unforeseen integration challenges, scalability concerns, or bugs.
    - List **user adoption risks** (e.g., low engagement, poor UX).
    - For each identified risk, describe a **mitigation plan** to reduce the likelihood of it impacting the product. Provide **contingency plans** in case risks materialize.

    Ensure that the final PRD is:
    - **Actionable**, with clear next steps and priorities.
    - **Comprehensive**, addressing all necessary aspects of the product lifecycle.
    - **Aligned with business and user goals**, ensuring it’s ready for development teams, stakeholders, and executives to make informed decisions.""",
    agent=final_compiler_agent,
    expected_output="A complete, well-structured PRD document in Markdown format",
    # output_file="PRD.md",
    output_json=PRDOutput,
    # output_format="markdown"
)
# final_compiler_task = Task(
#     description="""
#     Compile all sections into a structured PRD.  
#     Merge outputs from:
#       - User Requirements: {USER_REQUIREMENTS}
#       - Feature Definitions: {FEATURE_DEFINITION}
#       - Technical Specifications: {TECH_SPECS}
#       - Success Metrics: {SUCCESS_METRICS}    
    
#     Create a well-structured Markdown document with the following format:
    
#     # [Product Name] - Product Requirements Document
    
#     ## Executive Summary
#     [Brief overview of the product and its main objectives]
    
#     ## Problem Statement & Objectives
#     [Detail the problem being solved and key objectives]
    
#     ## Target Market & User Personas
#     [Describe the target audience and user personas]
    
#     ## Product Features
#     ### Core Features
#     [List and describe core features]
    
#     ### Unique Selling Points
#     [Highlight unique features and competitive advantages]
    
#     ## Technical Specifications
#     [Detail the technical implementation requirements]
    
#     ## Success Metrics & KPIs
#     [List measurable success criteria]
    
#     ## Timeline & Milestones
#     [Outline development phases and key dates]
    
#     ## Risks & Mitigation Strategies
#     [Identify potential risks and mitigation plans]
    
#     Ensure the final PRD meets industry standards and is ready for stakeholders.
#     """,
#     agent=final_compiler_agent,
#     expected_output="A complete, well-structured PRD document in Markdown format",
#     # output_file="PRD.md",
#     output_json=PRDOutput,
#     # output_format="markdown"
# )

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

