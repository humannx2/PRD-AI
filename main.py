from crewai import Crew
from agents.py import tech_spec_agent, success_metrics_agent, final_compiler_agent, user_requirements_agent, feature_definition_agent
from tasks import user_requirements_task, feature_definition_task, tech_spec_task, success_metrics_task, final_compiler_task

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