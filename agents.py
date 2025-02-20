from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")
# llm = LLM(model="groq/llama3-8b-8192", temperature=0.7, api_key=api_key)
llm = LLM(model="openai/gpt-4", temperature=0.7, api_key=api_key)
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
    Establish KPIs, user engagement metrics, and business goals to track the product’s success, based on the data provided by the User Requirement Agent.
    """,
    backstory="An expert in data-driven decision-making and growth metrics, ",
    llm=llm,
    verbose=True
)

#Final Compiler Agent
final_compiler_agent = Agent(
    role="Final Compiler Agent",
    goal="""
    Merge all Output provided by User Requirements Agent, Technical Specifications Agent, Feature Definition Agent, Success Metrics Agent into a structured PRD following industry standards.
     Ensure:
      - **Completeness** → No missing sections
      - **Clarity** → Well-structured content
      - **Formatting** → Uses Markdown syntax for easy readability.
    """,
    backstory="A veteran product strategist with extensive experience in PRD development.",
    llm=llm,
    verbose=True
)


