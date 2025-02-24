from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")
# llm = LLM(model="groq/llama3-8b-8192", temperature=0.7, api_key=api_key)
llm = LLM(model="openai/gpt-4o-mini", temperature=0.7, api_key=api_key)
# User Requirements Agent
user_requirements_agent = Agent(
    role="User Requirements Agent",
    goal="""
    Analyze the following details about the product and ensure all necessary information is gathered before passing data to other agents.
    """,
    backstory="""
    An experienced product manager who compiles essential information and product details.
    """,
    llm=llm,
    verbose=True
)

#Feature Definition Agent
feature_definition_agent = Agent(
    role="Feature Definition Agent",
    goal="""
    Analyze user requirements and generate a structured list of product features, 
    prioritizing them based on MVP and full-scale versions, based on the data provided by the User Requirement Agent.
    """,
    backstory="An expert in designing intuitive product features with a focus on usability.",
    llm=llm,
    verbose=True
)

#Technical Specifications Agent
tech_spec_agent = Agent(
    role="Technical Specifications Agent",
    goal="""
    Define the frontend, backend, database technologies, security, and scalability strategies.
    Ensure all technical aspects align with product goals, based on the data provided by the User Requirement Agent.
    """,
    backstory="A senior software architect specializing in scalable and secure systems.",
    llm=llm,
    verbose=True
)

#Success Metrics Agent
success_metrics_agent = Agent(
    role="Success Metrics Agent",
    goal="""
    Establish KPIs, user engagement metrics, and business goals to track the product's success, based on the data provided by the User Requirement Agent.
    """,
    backstory="An expert in data-driven decision-making and growth metrics, ",
    llm=llm,
    verbose=True
)

# Final Compiler Agent
final_compiler_agent = Agent(
    role="Final Compiler Agent",
    goal="""
    Your task is to compile a comprehensive, industry-standard Product Requirements Document (PRD) by merging outputs from:
      - User Requirements Agent
      - Technical Specifications Agent
      - Feature Definition Agent
      - Success Metrics Agent
    
    Deliverables:
      - A structured, detailed PRD with clearly defined sections.
      - Well-articulated requirements that are specific, measurable, and actionable.
      - Markdown-formatted output for easy readability and stakeholder review.
    
    Key Considerations:
      - Ensure completeness → Every essential section must be covered with no gaps.
      - Maintain clarity → Use concise, professional language.
      - Guarantee consistency → Align with company and industry best practices.
      - Establish traceability → Clearly link requirements to their respective sources.
      - Validate feasibility → Ensure all specifications are practical and implementable.
    
    Use industry best practices to enhance structure, readability, and effectiveness.
    """,
    backstory="A seasoned product strategist with deep expertise in PRD development, ensuring high-quality documentation that meets stakeholder needs and industry standards.",
    llm=llm,
    verbose=True
)

# PRD Modification Agents
prd_analyzer_agent = Agent(
    role="PRD Analysis Expert",
    goal="Analyze PRD modification requests and identify required changes",
    backstory="""You are an experienced Product Requirements Document (PRD) analyst 
    with expertise in understanding how changes in one section affect the entire document.""",
    verbose=True,
    memory=True
)

prd_modifier_agent = Agent(
    role="PRD Modification Expert",
    goal="Modify PRDs based on analysis provided by the PRD Analysis Expert and user requests while maintaining document consistency",
    backstory="""You are a skilled PRD writer with experience in making precise modifications 
    while ensuring the document remains coherent and consistent.""",
    verbose=True,
    memory=True
)


