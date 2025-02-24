from pydantic import BaseModel
from typing import Dict, List, Optional, Any
from datetime import datetime

class Stakeholder(BaseModel):
    name: str
    role: str

class NonFunctionalRequirements(BaseModel):
    usability: str
    performance: str
    reliability: str
    security: str
    scalability: str
    environmental: str

class Metadata(BaseModel):
    version: str
    revision_history: List[str]
    author: str
    date: datetime

class PurposeAndObjectives(BaseModel):
    problem_statement: str
    product_goals: str

class Scope(BaseModel):
    in_scope: List[str]
    out_of_scope: List[str]

class MarketAndUserResearch(BaseModel):
    target_market: str
    user_personas: List[str]

class Requirements(BaseModel):
    functional: List[str]
    non_functional: NonFunctionalRequirements

class AssumptionsConstraintsDependencies(BaseModel):
    assumptions: List[str]
    constraints: List[str]
    dependencies: List[str]

class TimelineAndMilestones(BaseModel):
    phases: List[str]
    estimated_release_dates: List[datetime]

class SuccessMetricsAndAcceptanceCriteria(BaseModel):
    KPIs: List[str]
    acceptance_criteria: List[str]

class PRDOutput(BaseModel):
    title: str
    metadata: Metadata
    executive_summary: str
    purpose_and_objectives: PurposeAndObjectives
    scope: Scope
    stakeholders: List[Stakeholder]
    market_and_user_research: MarketAndUserResearch
    requirements: Requirements
    assumptions_constraints_dependencies: AssumptionsConstraintsDependencies
    timeline_and_milestones: TimelineAndMilestones
    success_metrics_and_acceptance_criteria: SuccessMetricsAndAcceptanceCriteria
    risks_and_mitigation_strategies: List[str]

class ProductInput(BaseModel):
    PRODUCT_NAME: str
    PRODUCT_OBJECTIVE: str
    INDUSTRY: str
    TARGET_AUDIENCE: str
    USER_PERSONA: str
    PROBLEM_STATEMENT: str
    COMPETITOR_ANALYSIS: str
    CORE_FEATURES: List[str]
    UNIQUE_FEATURES: List[str]
    INTEGRATIONS: List[str]
    TECH_STACK: str
    SECURITY_COMPLIANCE: str
    SCALABILITY: str
    KPI: List[str]
    BUSINESS_GOALS: str
    LAUNCH_DATE: str
    ROADMAP: str
    BUDGET: str

class PRDResponse(BaseModel):
    markdown: str
    raw_data: Dict 

class ModificationRequest(BaseModel):
    raw_data: Dict[str, Any]
    user_request: str

    class Config:
        schema_extra = {
            "example": {
                "raw_data": "Output from /generate-prd endpoint",
                "user_request": "Add a section about security requirements"
            }
        } 