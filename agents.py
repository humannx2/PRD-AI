from crewai import Agent, LLM
import os

api_key=os.environ("GROQ_API_KEY")
llm=LLM(model="groq/llama3-8b-8192", temperature=0.6, api_key=api_key)

# User Requirements Agent
user_requirements_agent = Agent(
    name="User Requirements Agent",
    role="A consultant who gathers detailed requirements from the user.",
    goal="""
    Collect comprehensive details about the product by interacting with the user.
    Ensure all necessary information is gathered before passing data to other agents.
    """,
    backstory="""
    An experienced product manager who knows how to ask the right questions to extract 
    essential product details.
    """,
    llm=llm
)

#Feature Definition Agent
feature_definition_agent = Agent(
    name="Feature Definition Agent",
    role="A product strategist who defines the core features and functionalities.",
    goal="""
    Analyze user requirements and generate a structured list of product features, 
    prioritizing them based on MVP and full-scale versions.
    """,
    backstory="An expert in designing intuitive product features with a focus on usability.",
    llm=llm
)

#Technical Specifications Agent
tech_spec_agent = Agent(
    name="Technical Specifications Agent",
    role="A technical architect who outlines the required tech stack and integrations.",
    goal="""
    Define the frontend, backend, database technologies, security, and scalability strategies.
    Ensure all technical aspects align with product goals.
    """,
    backstory="A senior software architect specializing in scalable and secure systems.",
    llm=llm
)

#Success Metrics Agent
success_metrics_agent = Agent(
    name="Success Metrics Agent",
    role="A business analyst who defines key performance indicators and success metrics.",
    goal="""
    Establish KPIs, user engagement metrics, and business goals to track the product’s success.
    """,
    backstory="An expert in data-driven decision-making and growth metrics.",
    llm=llm
)

#Final Compiler Agent
final_compiler_agent = Agent(
    name="Final Compiler Agent",
    role="A senior product manager who compiles and refines the final PRD.",
    goal="""
    Merge all sections into a structured PRD following industry standards.
    Ensure clarity, consistency, and completeness before finalizing the document.
    """,
    backstory="A veteran product strategist with extensive experience in PRD development.",
    llm=llm
)


