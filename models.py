from pydantic import BaseModel
from typing import List, Optional
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
    open_issues_and_questions: List[str]
    appendices: List[str] 