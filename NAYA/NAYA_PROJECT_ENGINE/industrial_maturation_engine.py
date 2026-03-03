"""
Industrial Project Maturation Engine

Specialized for large-scale industrial projects (€15M-€40M+)
Maturation from current state to 70-90% production readiness

Architecture:
- Scans existing portfolio for industrial-scale projects
- Analyzes maturity level (current → target)
- Creates staged deployment roadmap
- Manages complex dependencies & integrations
- Tracks capital allocation tier
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from datetime import datetime, timedelta
import json


class ProjectScale(Enum):
    """Project economic classification."""
    STARTUP = "startup"              # €0-100k
    SCALE_UP = "scale_up"            # €100k-1M
    VENTURE = "venture"              # €1M-15M
    INDUSTRIAL = "industrial"        # €15M-100M
    ENTERPRISE = "enterprise"        # €100M+


class MaturityLevel(Enum):
    """Project maturation stages."""
    CONCEPT = 10                     # Idea only
    VALIDATED = 25                   # Market validation
    PROTOTYPE = 40                   # Working prototype
    MVP = 50                         # Minimum viable product
    SCALING = 65                     # Early scaling
    PRODUCTION = 80                  # Production deployment
    OPTIMIZED = 90                   # Full optimization


@dataclass
class ProjectMaturityAnalysis:
    """Analysis of project current vs target maturity."""
    
    project_id: str
    project_name: str
    current_maturity: MaturityLevel
    target_maturity: MaturityLevel  # Usually 70-90% for industrial
    estimated_value: float
    project_scale: ProjectScale
    
    # Roadmap stages
    stages: List[Dict[str, Any]] = field(default_factory=list)
    
    # Dependencies
    critical_dependencies: List[str] = field(default_factory=list)
    tech_stack_maturity: Dict[str, float] = field(default_factory=dict)
    
    # Resources
    team_gaps: List[str] = field(default_factory=list)
    infrastructure_gaps: List[str] = field(default_factory=list)
    
    def get_maturity_gap(self) -> int:
        """Gap to close (in percentage points)."""
        return self.target_maturity.value - self.current_maturity.value
    
    def is_industrial_scale(self) -> bool:
        """Check if this is industrial scale project."""
        return self.project_scale == ProjectScale.INDUSTRIAL


@dataclass
class MaturityStage:
    """Single maturity stage in roadmap."""
    
    stage_name: str
    target_maturity: int  # percentage
    timeline_weeks: int
    key_deliverables: List[str] = field(default_factory=list)
    success_criteria: List[str] = field(default_factory=list)
    dependencies_resolved: List[str] = field(default_factory=list)
    resource_investment: float = 0.0  # in thousands
    risk_level: str = "medium"


class IndustrialProjectAnalyzer:
    """
    Analyzes projects for maturity status and path to Industrial scale.
    """
    
    def __init__(self):
        self.analyses = {}
    
    def analyze_project(
        self,
        project_id: str,
        project_name: str,
        current_maturity_pct: int,
        estimated_value: float,
        vertical: str,
        constraints: Dict[str, Any],
        naya_behavior: Dict[str, Any]
    ) -> ProjectMaturityAnalysis:
        """
        Analyze project for industrial maturation readiness.
        """
        
        # Classify scale
        project_scale = self._classify_scale(estimated_value)
        
        # Current maturity
        current_maturity = self._pct_to_level(current_maturity_pct)
        
        # Target maturity (70-90% for industrial push)
        target_pct = 80  # Default to 80%
        target_maturity = MaturityLevel(target_pct)
        
        analysis = ProjectMaturityAnalysis(
            project_id=project_id,
            project_name=project_name,
            current_maturity=current_maturity,
            target_maturity=target_maturity,
            estimated_value=estimated_value,
            project_scale=project_scale,
            critical_dependencies=self._extract_dependencies(
                vertical, constraints
            ),
            tech_stack_maturity=self._evaluate_tech_stack(
                vertical, naya_behavior
            )
        )
        
        # Generate stages
        analysis.stages = self._generate_maturity_stages(analysis)
        
        # Identify gaps
        analysis.team_gaps = self._identify_team_gaps(vertical)
        analysis.infrastructure_gaps = self._identify_infra_gaps(
            project_scale, vertical
        )
        
        self.analyses[project_id] = analysis
        return analysis
    
    def _classify_scale(self, value: float) -> ProjectScale:
        """Classify project by economic value."""
        if value < 100_000:
            return ProjectScale.STARTUP
        elif value < 1_000_000:
            return ProjectScale.SCALE_UP
        elif value < 15_000_000:
            return ProjectScale.VENTURE
        elif value < 100_000_000:
            return ProjectScale.INDUSTRIAL
        else:
            return ProjectScale.ENTERPRISE
    
    def _pct_to_level(self, pct: int) -> MaturityLevel:
        """Convert percentage to maturity level."""
        if pct <= 15:
            return MaturityLevel.CONCEPT
        elif pct <= 30:
            return MaturityLevel.VALIDATED
        elif pct <= 45:
            return MaturityLevel.PROTOTYPE
        elif pct <= 60:
            return MaturityLevel.MVP
        elif pct <= 75:
            return MaturityLevel.SCALING
        elif pct <= 85:
            return MaturityLevel.PRODUCTION
        else:
            return MaturityLevel.OPTIMIZED
    
    def _extract_dependencies(
        self,
        vertical: str,
        constraints: Dict[str, Any]
    ) -> List[str]:
        """Extract critical dependencies."""
        deps = []
        
        if constraints.get('certifications_required'):
            deps.append(f"Certifications for {vertical}")
        
        if constraints.get('eu_export'):
            deps.append("EU export compliance")
        
        if constraints.get('dangerous_goods'):
            deps.append("Dangerous goods certification")
        
        if constraints.get('energy_type'):
            deps.append("Energy certification")
        
        if constraints.get('insurance_required'):
            deps.append("Insurance & liability coverage")
        
        return deps
    
    def _evaluate_tech_stack(
        self,
        vertical: str,
        naya_behavior: Dict[str, Any]
    ) -> Dict[str, float]:
        """Evaluate maturity of tech stack."""
        
        return {
            'supplier_integration': 0.75 if naya_behavior.get('supplier_hunt') else 0.5,
            'market_validation': 0.8,
            'reuse_assets': 0.9 if naya_behavior.get('reuse_assets') else 0.5,
            'automation_level': 0.7
        }
    
    def _generate_maturity_stages(
        self,
        analysis: ProjectMaturityAnalysis
    ) -> List[MaturityStage]:
        """Generate stages to reach target maturity."""
        
        gap = analysis.get_maturity_gap()
        stages = []
        
        if gap <= 0:
            return stages
        
        # Stage 1: Validation completion (if needed)
        if analysis.current_maturity.value < 30:
            stages.append(MaturityStage(
                stage_name="Market Validation",
                target_maturity=30,
                timeline_weeks=8,
                key_deliverables=[
                    "Market study",
                    "Customer validation",
                    "Price discovery"
                ],
                success_criteria=[
                    "10+ customer interviews",
                    "Willingness-to-pay confirmed",
                    "Market size estimated"
                ]
            ))
        
        # Stage 2: Prototype (if needed)
        if analysis.current_maturity.value < 45:
            stages.append(MaturityStage(
                stage_name="Prototype Development",
                target_maturity=45,
                timeline_weeks=12,
                key_deliverables=[
                    "Working prototype",
                    "Technical documentation",
                    "Cost structure"
                ],
                success_criteria=[
                    "Prototype functional",
                    "3 test customers validated",
                    "Unit economics calculated"
                ],
                risk_level="high"
            ))
        
        # Stage 3: MVP (if needed)
        if analysis.current_maturity.value < 60:
            stages.append(MaturityStage(
                stage_name="MVP & Initial Traction",
                target_maturity=60,
                timeline_weeks=16,
                key_deliverables=[
                    "Production-ready MVP",
                    "Customer acquisition channel",
                    "Go-to-market plan"
                ],
                success_criteria=[
                    "5-10 paying customers",
                    "Revenue >€50k",
                    "Unit economics positive"
                ],
                resource_investment=250.0
            ))
        
        # Stage 4: Scaling (if needed)
        if analysis.current_maturity.value < 75:
            stages.append(MaturityStage(
                stage_name="Scaling & Expansion",
                target_maturity=75,
                timeline_weeks=20,
                key_deliverables=[
                    "Scaled production",
                    "Team expansion",
                    "Multi-channel distribution"
                ],
                success_criteria=[
                    "50+ customers",
                    "€1M+ ARR trajectory",
                    "Team >5 people"
                ],
                resource_investment=500.0,
                risk_level="high"
            ))
        
        # Stage 5: Production optimization (if needed to reach 80%+)
        if analysis.target_maturity.value >= 80:
            stages.append(MaturityStage(
                stage_name="Production Optimization",
                target_maturity=80,
                timeline_weeks=12,
                key_deliverables=[
                    "Optimized operations",
                    "Quality systems",
                    "Performance analytics"
                ],
                success_criteria=[
                    "Unit cost reduced 20%",
                    "Customer retention 90%+",
                    "NPS >50"
                ],
                resource_investment=200.0
            ))
        
        return stages
    
    def _identify_team_gaps(self, vertical: str) -> List[str]:
        """Identify team expertise gaps."""
        gaps = []
        
        if vertical in ['digital', 'ai', 'xr']:
            gaps.append("ML/AI specialist")
        
        if vertical in ['hardware', 'manufacturing']:
            gaps.append("Supply chain manager")
        
        if vertical in ['cosmetics', 'food']:
            gaps.append("Regulatory compliance officer")
        
        gaps.append("CFO/Finance lead")
        gaps.append("Growth/Marketing lead")
        
        return gaps
    
    def _identify_infra_gaps(
        self,
        scale: ProjectScale,
        vertical: str
    ) -> List[str]:
        """Identify infrastructure gaps."""
        gaps = []
        
        if scale in [ProjectScale.INDUSTRIAL, ProjectScale.ENTERPRISE]:
            gaps.append("Production facility")
            gaps.append("Quality control system")
            gaps.append("Distributed inventory")
        
        if vertical in ['cosmetics', 'food']:
            gaps.append("Manufacturing facility")
            gaps.append("Laboratory testing")
        
        gaps.append("24/7 customer support")
        gaps.append("Automated fulfillment")
        
        return gaps


class IndustrialMaturitationPlanner:
    """
    Plans the maturation journey for industrial projects.
    """
    
    def __init__(self, analyzer: IndustrialProjectAnalyzer):
        self.analyzer = analyzer
    
    def create_maturation_plan(
        self,
        analysis: ProjectMaturityAnalysis
    ) -> Dict[str, Any]:
        """
        Create complete maturation plan from current to target state.
        """
        
        plan = {
            'project_id': analysis.project_id,
            'project_name': analysis.project_name,
            'current_state': {
                'maturity': f"{analysis.current_maturity.value}%",
                'scale': analysis.project_scale.value,
                'estimated_value': f"€{analysis.estimated_value:,.0f}"
            },
            'target_state': {
                'maturity': f"{analysis.target_maturity.value}%",
                'scale': 'INDUSTRIAL',
                'estimated_value': f"€{analysis.estimated_value * 1.5:,.0f}"  # 50% growth expected
            },
            'journey': {
                'stages': []
            },
            'risks': []
        }
        
        # Add stages
        total_weeks = 0
        cumulative_investment = 0.0
        
        for stage in analysis.stages:
            stage_plan = {
                'stage': stage.stage_name,
                'target_maturity': f"{stage.target_maturity}%",
                'timeline_weeks': stage.timeline_weeks,
                'deliverables': stage.key_deliverables,
                'success_criteria': stage.success_criteria,
                'investment_k_eur': stage.resource_investment,
                'risk': stage.risk_level
            }
            
            plan['journey']['stages'].append(stage_plan)
            total_weeks += stage.timeline_weeks
            cumulative_investment += stage.resource_investment
        
        plan['total_journey'] = {
            'timeline_months': round(total_weeks / 4.3, 1),
            'total_investment_k_eur': cumulative_investment,
            'expected_argg_horizon': '18-24 months'
        }
        
        # Add team & infra requirements
        plan['requirements'] = {
            'team_additions': analysis.team_gaps,
            'infrastructure': analysis.infrastructure_gaps,
            'dependencies_to_resolve': analysis.critical_dependencies
        }
        
        return plan


# ─────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────

class IndustrialProjectEngine:
    """
    Master engine for industrial project maturation.
    
    Public API for NAYA system.
    """
    
    def __init__(self):
        self.analyzer = IndustrialProjectAnalyzer()
        self.planner = IndustrialMaturitationPlanner(self.analyzer)
        self.portfolio = {}
    
    def scan_project_portfolio(self, projects: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Scan portfolio and identify industrial-scale projects.
        Returns analysis + maturation plans for each.
        """
        
        industrial_projects = []
        venture_projects = []
        
        for project in projects:
            analysis = self.analyzer.analyze_project(
                project_id=project['project_id'],
                project_name=project.get('description', project['project_id']),
                current_maturity_pct=project.get('current_maturity', 40),
                estimated_value=project.get('estimated_value', 5_000_000),
                vertical=project.get('vertical', 'other'),
                constraints=project.get('constraints', {}),
                naya_behavior=project.get('naya_behavior', {})
            )
            
            # Create maturation plan
            plan = self.planner.create_maturation_plan(analysis)
            
            if analysis.is_industrial_scale():
                industrial_projects.append({
                    'analysis': analysis,
                    'maturation_plan': plan
                })
            else:
                venture_projects.append({
                    'analysis': analysis,
                    'maturation_plan': plan
                })
            
            self.portfolio[project['project_id']] = {
                'analysis': analysis,
                'plan': plan
            }
        
        return {
            'timestamp': datetime.utcnow().isoformat(),
            'total_projects_scanned': len(projects),
            'industrial_scale_projects': len(industrial_projects),
            'venture_scale_projects': len(venture_projects),
            'industrial_projects': [
                {
                    'id': p['analysis'].project_id,
                    'name': p['analysis'].project_name,
                    'scale': p['analysis'].project_scale.value,
                    'current_maturity': f"{p['analysis'].current_maturity.value}%",
                    'target_maturity': f"{p['analysis'].target_maturity.value}%",
                    'maturity_gap': f"{p['analysis'].get_maturity_gap()}%",
                    'journey_months': p['maturation_plan']['total_journey']['timeline_months'],
                    'investment_k_eur': p['maturation_plan']['total_journey']['total_investment_k_eur']
                }
                for p in industrial_projects
            ],
            'portfolio_summary': self._summarize_portfolio()
        }
    
    def get_industrial_projects(self) -> List[Dict[str, Any]]:
        """Get all industrial-scale projects with maturation status."""
        return [
            {
                'project_id': proj['analysis'].project_id,
                'name': proj['analysis'].project_name,
                'scale': proj['analysis'].project_scale.value,
                'maturity': {
                    'current': f"{proj['analysis'].current_maturity.value}%",
                    'target': f"{proj['analysis'].target_maturity.value}%"
                },
                'stages': len(proj['plan']['journey']['stages']),
                'total_timeline_months': proj['plan']['total_journey']['timeline_months']
            }
            for proj in self.portfolio.values()
            if proj['analysis'].is_industrial_scale()
        ]
    
    def _summarize_portfolio(self) -> Dict[str, Any]:
        """Get portfolio summary."""
        if not self.portfolio:
            return {}
        
        total_value = sum(
            p['analysis'].estimated_value
            for p in self.portfolio.values()
        )
        
        industrial_value = sum(
            p['analysis'].estimated_value
            for p in self.portfolio.values()
            if p['analysis'].is_industrial_scale()
        )
        
        return {
            'total_portfolio_value_eur': total_value,
            'industrial_value_eur': industrial_value,
            'portfolio_concentration': f"{(industrial_value/total_value*100):.1f}%"
        }


__all__ = [
    'IndustrialProjectEngine',
    'IndustrialProjectAnalyzer',
    'IndustrialMaturitationPlanner',
    'ProjectMaturityAnalysis',
    'ProjectScale',
    'MaturityLevel'
]
