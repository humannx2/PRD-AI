from crewai import Task
from agents import tech_spec_agent, success_metrics_agent, final_compiler_agent, user_requirements_agent, feature_definition_agent


# 🟢 User Requirements Task
user_requirements_task = Task(
    description="""Based on this data, and make a comprehensive list for other agents to work on.
      - **Product Name:** {PRODUCT_NAME}
      - **Objective:** {PRODUCT_OBJECTIVE}
      - **Industry/Niche:** {INDUSTRY}
      - **Target Audience:** {TARGET_AUDIENCE}
      - **User Persona:** {USER_PERSONA}
      - **Problem Statement:** {PROBLEM_STATEMENT}
      - **Competitor Analysis:**{COMPETITOR_ANALYSIS}
      - **Core Features:** {CORE_FEATURES}
      - **Unique Selling Points (USPs):** {UNIQUE_FEATURES}
      - **Integrations:** {INTEGRATIONS}
      - **Tech Stack:** {TECH_STACK}
      - **Security & Compliance:** {SECURITY_COMPLIANCE}
      - **Scalability Considerations:** {SCALABILITY}
      - **Success Metrics & KPIs:** {KPI}
      - **Business Goals:** {BUSINESS_GOALS}
      - **Launch Date:** {LAUNCH_DATE}
      - **Development Roadmap:** {ROADMAP}
      - **Budget Allocation:** {BUDGET}""",
    agent=user_requirements_agent, 
    expected_output="A comprehensive list of all the user requirements compiled to help other agents"
)

# 🟢 Feature Definition Task
feature_definition_task = Task(
    description="""
    Define and structure the product’s core features.  
    Using the provided requirements:
      - Identify **MVP features** and their importance.
      - Highlight **full-scale features** beyond MVP.
      - Explain **how the features solve the problem statement**.
      - Map out the **user journey** based on the user persona.
      - Define **competitive advantages** over existing solutions.
    Ensure the feature list aligns with business objectives.
    """,
    agent=feature_definition_agent,
    expected_output="A detailed list of all the objectives defined in the description"
)

# 🟢 Technical Specifications Task
tech_spec_task = Task(
    description="""
    Provide detailed technical specifications.  
    Define:
      -**Frontend & Backend Technologies:** {{TECH_STACK}}
      -**APIs & Integrations:** {{INTEGRATIONS}}
      -**Security & Compliance Standards:** {{SECURITY_COMPLIANCE}}
      -**Scalability Strategies:** {{SCALABILITY}}
      -**Infrastructure & Hosting Recommendations**  
    Ensure the technical decisions align with the product's goals.
    """,
    agent=tech_spec_agent,
    expected_output="A detailed list of all the objectives defined in the description"
)

# 🟢 Success Metrics Task
success_metrics_task = Task(
    description="""
    Define measurable success criteria for the product.  
    Establish:
      -**Key Performance Indicators (KPIs):** {{KPIs}}
      -**User Retention & Growth Metrics**  
      -**Monetization & ROI Expectations:** {{BUSINESS_GOALS}}
      -**Market Adoption Strategy**
    Ensure all success metrics are realistic and aligned with industry standards.
    """,
    agent=success_metrics_agent,
    expected_output="A detailed list of all the objectives defined in the description"

)

# 🟢 Final PRD Compilation Task
final_compiler_task = Task(
    description="""
    Compile all sections into a structured PRD.  
    Merge outputs from:
      -**User Requirements Agent**
      -**Feature Definitions Agent**
      -**Technical Specifications Agent**
      -**Success Metrics Agent**
    Format the PRD as a **Markdown document** with:
      - Proper headers (`#`, `##`, `###`)
      - Bullet points & lists
      - Consistent structure for readability
    Ensure the final PRD meets industry standards and is ready for stakeholders.
    """,
    agent=final_compiler_agent,
    expected_output="A detailed list of all the objectives defined in the description",
    output_file="PRD.md"

)
