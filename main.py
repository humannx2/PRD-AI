from crewai import Crew
from agents import tech_spec_agent, success_metrics_agent, final_compiler_agent, user_requirements_agent, feature_definition_agent
from tasks import user_requirements_task, feature_definition_task, tech_spec_task, success_metrics_task, final_compiler_task
from dotenv import load_dotenv
import warnings
import json
from datetime import datetime
from json import JSONEncoder

warnings.filterwarnings('ignore')

load_dotenv()


class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Testing Data
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

# Data dictionary to use the custom encoder when needed
data = {
    "USER_REQUIREMENTS": sample_data,
    "FEATURE_DEFINITION": None,
    "TECH_SPECS": None,
    "SUCCESS_METRICS": None,
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

# Execute Crew 1 & 2 and extract outputs
crew_1_results = crew_1.kickoff(inputs=sample_data)
# print(crew_1_results)
crew_2_results = crew_2.kickoff(inputs=sample_data)
# print(crew_2_results)

data["FEATURE_DEFINITION"] = crew_1_results.raw
data["TECH_SPECS"] = crew_2_results.raw

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

# Convert data to JSON-serializable format
data = json.loads(json.dumps(data, cls=DateTimeEncoder))

# Execute Crew 4 and get the final PRD output
prd_output = crew_4.kickoff(inputs=data)

# Convert JSON to Python dictionary
prd_data = json.loads(prd_output.raw)

# Function to generate Markdown from JSON
def generate_markdown(prd_data):
    md = f"# {prd_data['title']}\n\n"
    md += f"**Version:** {prd_data['metadata']['version']}\n"
    md += f"**Author:** {prd_data['metadata']['author']}\n"
    md += f"**Date:** {prd_data['metadata']['date']}\n\n"

    md += "## Executive Summary\n"
    md += f"{prd_data['executive_summary']}\n\n"

    md += "## Purpose and Objectives\n"
    md += f"### Problem Statement\n{prd_data['purpose_and_objectives']['problem_statement']}\n\n"
    md += f"### Product Goals\n{prd_data['purpose_and_objectives']['product_goals']}\n\n"

    md += "## Scope\n"
    md += "### In Scope:\n" + "\n".join([f"- {item}" for item in prd_data["scope"]["in_scope"]]) + "\n\n"
    md += "### Out of Scope:\n" + "\n".join([f"- {item}" for item in prd_data["scope"]["out_of_scope"]]) + "\n\n"

    md += "## Stakeholders\n"
    for stakeholder in prd_data["stakeholders"]:
        md += f"- **{stakeholder['name']}**: {stakeholder['role']}\n"

    md += "\n## Market and User Research\n"
    md += f"**Target Market:** {prd_data['market_and_user_research']['target_market']}\n"
    md += "### User Personas:\n" + "\n".join([f"- {persona}" for persona in prd_data["market_and_user_research"]["user_personas"]]) + "\n\n"

    md += "## Requirements\n"
    md += "### Functional Requirements:\n" + "\n".join([f"- {req}" for req in prd_data["requirements"]["functional"]]) + "\n\n"
    md += "### Non-Functional Requirements:\n"
    for key, value in prd_data["requirements"]["non_functional"].items():
        md += f"- **{key.capitalize()}**: {value}\n"

    md += "\n## Assumptions, Constraints, and Dependencies\n"
    md += "### Assumptions:\n" + "\n".join([f"- {assumption}" for assumption in prd_data["assumptions_constraints_dependencies"]["assumptions"]]) + "\n\n"
    md += "### Constraints:\n" + "\n".join([f"- {constraint}" for constraint in prd_data["assumptions_constraints_dependencies"]["constraints"]]) + "\n\n"
    md += "### Dependencies:\n" + "\n".join([f"- {dependency}" for dependency in prd_data["assumptions_constraints_dependencies"]["dependencies"]]) + "\n\n"

    md += "## Timeline and Milestones\n"
    for phase, date in zip(prd_data["timeline_and_milestones"]["phases"], prd_data["timeline_and_milestones"]["estimated_release_dates"]):
        md += f"- **{phase}**: {date}\n"

    md += "\n## Success Metrics and Acceptance Criteria\n"
    md += "### KPIs:\n" + "\n".join([f"- {kpi}" for kpi in prd_data["success_metrics_and_acceptance_criteria"]["KPIs"]]) + "\n\n"
    md += "### Acceptance Criteria:\n" + "\n".join([f"- {criteria}" for criteria in prd_data["success_metrics_and_acceptance_criteria"]["acceptance_criteria"]]) + "\n\n"

    md += "## Risks and Mitigation Strategies\n"
    md += "\n".join([f"- {risk}" for risk in prd_data["risks_and_mitigation_strategies"]]) + "\n\n"

    md += "## Open Issues and Questions\n"
    md += "\n".join([f"- {issue}" for issue in prd_data["open_issues_and_questions"]]) + "\n\n"

    md += "## Appendices\n"
    md += "\n".join([f"- {appendix}" for appendix in prd_data["appendices"]]) + "\n"

    return md

# Generate Markdown
markdown_output = generate_markdown(prd_data)

# Save to a file
with open("PRD.md", "w", encoding="utf-8") as file:
    file.write(markdown_output)

print("Markdown file generated: PRD.md")

