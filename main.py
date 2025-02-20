from crewai import Crew
from agents import tech_spec_agent, success_metrics_agent, final_compiler_agent, user_requirements_agent, feature_definition_agent
from tasks import user_requirements_task, feature_definition_task, tech_spec_task, success_metrics_task, final_compiler_task
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

prd_crew = Crew(
    agents=[
        user_requirements_agent,
        feature_definition_agent,
        tech_spec_agent,
        success_metrics_agent,
        final_compiler_agent
    ],
    tasks=[
        user_requirements_task,
        feature_definition_task,
        tech_spec_task,
        success_metrics_task,
        final_compiler_task
    ],
    verbose=True  # Enable detailed logging
)

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


# Kickoff the PRD Generation with sample data
print("Running PRD AI Crew with Sample Input...\n")
final_prd = prd_crew.kickoff(inputs=sample_data)

# Display final PRD in terminal
print("\n PRD Generated Successfully!\n")
print(final_prd)