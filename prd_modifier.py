from crewai import Crew
from models import PRDOutput, PRDResponse
from agents import prd_analyzer_agent, prd_modifier_agent
from typing import Dict
import json
from tasks import prd_analysis_task, prd_modification_task

# def modify_prd(prd_data: Dict, user_request: str) -> PRDResponse:
def modify_prd(prd_data: Dict, user_request: str):
    data={
        "prd_content": json.dumps(prd_data, indent=2),
        "user_request": user_request,
        "analysis_result": None
    }

    modification_analysis_crew = Crew(
        agents=[prd_analyzer_agent],
        tasks=[prd_analysis_task],
        verbose=True
    )

    modification_crew = Crew(
        agents=[prd_modifier_agent],
        tasks=[prd_modification_task],
        verbose=True
    )

    # Execute modification process
    modified_analysis_prd = modification_analysis_crew.kickoff(inputs=data)
    data["analysis_result"] = modified_analysis_prd.raw
    modified_prd = modification_crew.kickoff(inputs=data)
    modified_prd_data = json.loads(modified_prd.raw)
    print (modified_prd_data)
    return modified_prd_data

    # # Generate updated markdown
    # from main import generate_markdown
    # markdown_output = generate_markdown(modified_prd_data)

    # return PRDResponse(
    #     markdown=markdown_output,
    #     raw_data=modified_prd_data
    # )

# Sample usage
if __name__ == "__main__":
    # Sample PRD data
    sample_prd = {
        "title": "Product Requirements Document for TaskFlow",
        "metadata": {
            "version": "1.0",
            "revision_history": [
                "Initial Draft - March 2024"
            ],
            "author": "Final Compiler Agent",
            "date": "2024-03-20T00:00:00Z"
        },
        "executive_summary": "TaskFlow is an AI-powered task management tool designed specifically for remote teams, addressing the challenges of managing tasks efficiently across different time zones.",
        "purpose_and_objectives": {
            "problem_statement": "Managing tasks efficiently across different time zones is challenging for remote teams.",
            "product_goals": "To develop an intuitive task management solution that simplifies task assignment and tracking."
        },
        "scope": {
            "in_scope": [
                "Core task management features",
                "Basic AI prioritization"
            ],
            "out_of_scope": [
                "Mobile application",
                "Advanced analytics"
            ]
        },
        "stakeholders": [
            {
                "name": "Product Manager",
                "role": "Oversees product development"
            },
            {
                "name": "Tech Lead",
                "role": "Technical architecture"
            }
        ],
        "market_and_user_research": {
            "target_market": "Remote tech companies",
            "user_personas": [
                "Remote team managers",
                "Distributed team members"
            ]
        },
        "requirements": {
            "functional": [
                "Task creation and assignment",
                "Progress tracking",
                "Basic AI prioritization"
            ],
            "non_functional": {
                "usability": "Intuitive interface",
                "performance": "< 2s response time",
                "reliability": "99.9% uptime",
                "security": "SOC2 compliance",
                "scalability": "Support 10k users",
                "environmental": "Cloud-based deployment"
            }
        },
        "assumptions_constraints_dependencies": {
            "assumptions": [
                "Users have stable internet",
                "Basic tech literacy"
            ],
            "constraints": [
                "6-month development timeline",
                "$150k budget"
            ],
            "dependencies": [
                "Cloud infrastructure",
                "AI services"
            ]
        },
        "timeline_and_milestones": {
            "phases": [
                "Design",
                "Development",
                "Testing",
                "Launch"
            ],
            "estimated_release_dates": [
                "2024-04-01T00:00:00Z",
                "2024-06-01T00:00:00Z",
                "2024-08-01T00:00:00Z",
                "2024-09-01T00:00:00Z"
            ]
        },
        "success_metrics_and_acceptance_criteria": {
            "KPIs": [
                "10,000 users in 6 months",
                "90% user satisfaction"
            ],
            "acceptance_criteria": [
                "All core features working",
                "Performance targets met"
            ]
        },
        "risks_and_mitigation_strategies": [
            "Technical risk: Regular code reviews",
            "Market risk: Early beta testing"
        ],
    }

    # Sample user modification request
    sample_request = """
    Please update the executive summary to emphasize our new machine learning 
    capabilities and add a new KPI for AI task automation accuracy rate of 95%.
    Also, update the functional requirements to include advanced AI features.
    """

    # Modify PRD
    try:
        modified_prd = modify_prd(sample_prd, sample_request)
        print("\nModification successful!")
        print("\nModified Executive Summary:")
        print(modified_prd.raw_data["executive_summary"])
        print("\nModified KPIs:")
        print(modified_prd.raw_data["success_metrics_and_acceptance_criteria"]["KPIs"])
        print("\nModified Functional Requirements:")
        print(modified_prd.raw_data["requirements"]["functional"])
    except Exception as e:
        print(f"Error occurred: {str(e)}") 