from crewai import Crew
from agents import tech_spec_agent, success_metrics_agent, final_compiler_agent, user_requirements_agent, feature_definition_agent
from tasks import user_requirements_task, feature_definition_task, tech_spec_task, success_metrics_task, final_compiler_task
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

# prd_crew = Crew(
#     agents=[
#         user_requirements_agent,
#         feature_definition_agent,
#         tech_spec_agent,
#         success_metrics_agent,
#         final_compiler_agent
#     ],
#     tasks=[
#         user_requirements_task,
#         feature_definition_task,
#         tech_spec_task,
#         success_metrics_task,
#         final_compiler_task
#     ],
#     verbose=True  # Enable detailed logging
# )

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

# Crew 1: Extracts user requirements, feature definitions, and technical specs
crew_1 = Crew(
    agents=[
        user_requirements_agent,
        feature_definition_agent,
        tech_spec_agent
    ],
    tasks=[
        user_requirements_task,
        feature_definition_task,
        tech_spec_task
    ],
    verbose=True
)

# Execute Crew 1 and extract outputs
crew_1_results = crew_1.kickoff(inputs=sample_data)
user_requirements_output = crew_1_results[user_requirements_agent].raw
feature_definition_output = crew_1_results[feature_definition_agent].raw
tech_spec_output = crew_1_results[tech_spec_agent].raw

# Prepare inputs for Crew 2
compiled_inputs = {
    "USER_REQUIREMENTS": user_requirements_output,
    "FEATURE_DEFINITION": feature_definition_output,
    "TECH_SPECS": tech_spec_output
}

# Crew 2: Generates success metrics
crew_2 = Crew(
    agents=[success_metrics_agent],
    tasks=[success_metrics_task],
    verbose=True
)

# Execute Crew 2 and extract output
success_metrics_output = crew_2.kickoff(inputs=compiled_inputs)[success_metrics_agent].raw

# Update inputs for final compilation
compiled_inputs["SUCCESS_METRICS"] = success_metrics_output

# Crew 3: Generates the final PRD
crew_3 = Crew(
    agents=[final_compiler_agent],
    tasks=[final_compiler_task],
    verbose=True
)

# Execute Crew 3 and get the final PRD output
prd_output = crew_3.kickoff(inputs=compiled_inputs)

print("Final PRD Output:\n", prd_output)



# # Kickoff the PRD Generation with sample data
# print("Running PRD AI Crew with Sample Input...\n")
# final_prd = prd_crew.kickoff(inputs=sample_data)

# # Display final PRD in terminal
# print("\n PRD Generated Successfully!\n")
# print(final_prd)