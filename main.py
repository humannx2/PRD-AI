from crewai import Crew
from agents import tech_spec_agent, success_metrics_agent, final_compiler_agent, user_requirements_agent, feature_definition_agent
from tasks import user_requirements_task, feature_definition_task, tech_spec_task, success_metrics_task, final_compiler_task
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')

load_dotenv()


sample_data = {
    "PRODUCT_NAME": "TaskFlow",
    "PRODUCT_OBJECTIVE": "An AI-powered task management tool for remote teams.",
    "INDUSTRY": "SaaS / Productivity",
    "TARGET_AUDIENCE": "Startup founders, project managers, and remote teams.",
    "USER_PERSONA": "Tech-savvy professionals who manage distributed teams.",
    "PROBLEM_STATEMENT": "Managing tasks efficiently across different time zones is challenging.",
    "COMPETITOR_ANALYSIS": "Competes with Trello and Asana but offers AI-powered automation.",
    "CORE_FEATURES": ["Task assignment", "AI-prioritized tasks", "Progress tracking"],
    "UNIQUE_FEATURES": ["AI-driven task automation", "Smart deadline predictions"],
    "INTEGRATIONS": ["Slack", "Google Calendar", "Notion"],
    "TECH_STACK": "React (Frontend), Django (Backend), PostgreSQL (Database)",
    "SECURITY_COMPLIANCE": "GDPR & SOC2 compliant",
    "SCALABILITY": "Built on AWS with auto-scaling support",
    "KPI": ["Monthly Active Users (MAU): 50,000", "Retention Rate: 85%"],
    "BUSINESS_GOALS": "Achieve $1M ARR within 12 months",
    "LAUNCH_DATE": "Q3 2025",
    "ROADMAP": "MVP → Beta → Full Launch",
    "BUDGET": "$200,000 for initial development"
}

crew_1 = Crew(
    agents=[
        user_requirements_agent,
        feature_definition_agent,
    ],
    tasks=[
        user_requirements_task,
        feature_definition_task,
    ],
    verbose=True
)
crew_2 = Crew(
    agents=[
        user_requirements_agent,
        tech_spec_agent,
    ],
    tasks=[
        user_requirements_task,
        tech_spec_task,
    ],
    verbose=True
)

# Execute Crew 1 and extract outputs
crew_1_results = crew_1.kickoff(inputs=sample_data)
print(crew_1_results)
crew_2_results = crew_2.kickoff(inputs=sample_data)
print(crew_2_results)

# Prepare inputs for Crew 2
data = {
    "USER_REQUIREMENTS": sample_data,
    "FEATURE_DEFINITION": crew_1_results.raw,
    "TECH_SPECS": crew_2_results.raw
}

# Crew 3: Generates success metrics
crew_3 = Crew(
    agents=[success_metrics_agent],
    tasks=[success_metrics_task],
    verbose=True
)

# Execute Crew 3 and extract output
success_metrics_output = crew_3.kickoff(inputs=data)

# Update inputs for final compilation
data["SUCCESS_METRICS"] = success_metrics_output.raw

# Crew 4: Generates the final PRD
crew_4 = Crew(
    agents=[final_compiler_agent],
    tasks=[final_compiler_task],
    verbose=True
)

# Execute Crew 4 and get the final PRD output
prd_output = crew_4.kickoff(inputs=data)

print("Final PRD Output:\n", prd_output)

