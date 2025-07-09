"""
Market Analyst Tool - Simulates an external MCP-discoverable tool for market research.
This tool provides mock market analysis reports for business ideas.
"""

import random
from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class MarketAnalysisReport:
    """Data class to structure market analysis reports."""
    business_idea: str
    market_size: str
    competition_level: str
    growth_potential: str
    target_demographics: str
    key_challenges: str
    opportunities: str
    risk_level: str


class MarketAnalystTool:
    """
    A simulated external market analysis tool that provides comprehensive
    market research reports for business ideas.
    """
    
    def __init__(self):
        self.market_sizes = [
            "$10M - $50M (Niche market)",
            "$50M - $200M (Small market)",
            "$200M - $1B (Medium market)", 
            "$1B - $10B (Large market)",
            "$10B+ (Massive market)"
        ]
        
        self.competition_levels = [
            "Low - Few competitors, blue ocean opportunity",
            "Medium - Moderate competition with room for differentiation",
            "High - Saturated market with established players",
            "Very High - Dominated by tech giants and major corporations"
        ]
        
        self.growth_potentials = [
            "Low (0-5% annually) - Mature/declining market",
            "Moderate (5-15% annually) - Steady growth market",
            "High (15-30% annually) - Fast-growing market",
            "Very High (30%+ annually) - Explosive growth market"
        ]
        
        self.demographics = [
            "Millennials and Gen Z (18-40 years)",
            "Working professionals (25-55 years)",
            "Small to medium businesses",
            "Enterprise clients",
            "Tech-savvy consumers",
            "Budget-conscious consumers",
            "Premium market segment"
        ]
    
    def analyze_market(self, business_idea: str) -> MarketAnalysisReport:
        """
        Perform market analysis for a given business idea.
        
        Args:
            business_idea (str): The business idea to analyze
            
        Returns:
            MarketAnalysisReport: Comprehensive market analysis report
        """
        # Simulate analysis processing time and complexity
        import time
        time.sleep(0.5)  # Simulate external API call delay
        
        # Generate mock but realistic market analysis
        report = MarketAnalysisReport(
            business_idea=business_idea,
            market_size=random.choice(self.market_sizes),
            competition_level=random.choice(self.competition_levels),
            growth_potential=random.choice(self.growth_potentials),
            target_demographics=random.choice(self.demographics),
            key_challenges=self._generate_challenges(business_idea),
            opportunities=self._generate_opportunities(business_idea),
            risk_level=self._assess_risk_level()
        )
        
        return report
    
    def _generate_challenges(self, business_idea: str) -> str:
        """Generate relevant challenges based on business idea keywords."""
        challenges = []
        idea_lower = business_idea.lower()
        
        if any(word in idea_lower for word in ['tech', 'app', 'software', 'digital']):
            challenges.extend([
                "High development costs",
                "User acquisition and retention",
                "Technology scalability"
            ])
        
        if any(word in idea_lower for word in ['food', 'restaurant', 'delivery']):
            challenges.extend([
                "Supply chain management",
                "Food safety regulations",
                "Seasonal demand fluctuations"
            ])
        
        if any(word in idea_lower for word in ['e-commerce', 'online', 'marketplace']):
            challenges.extend([
                "Customer trust and security",
                "Logistics and fulfillment",
                "Marketing and brand awareness"
            ])
        
        # Default challenges
        if not challenges:
            challenges = [
                "Market penetration",
                "Customer acquisition costs",
                "Regulatory compliance"
            ]
        
        return "; ".join(random.sample(challenges, min(2, len(challenges))))
    
    def _generate_opportunities(self, business_idea: str) -> str:
        """Generate relevant opportunities based on business idea keywords."""
        opportunities = []
        idea_lower = business_idea.lower()
        
        if any(word in idea_lower for word in ['sustainable', 'eco', 'green']):
            opportunities.append("Growing environmental consciousness")
        
        if any(word in idea_lower for word in ['ai', 'machine learning', 'automation']):
            opportunities.append("AI adoption across industries")
        
        if any(word in idea_lower for word in ['health', 'fitness', 'wellness']):
            opportunities.append("Increasing health awareness post-pandemic")
        
        # Default opportunities
        base_opportunities = [
            "Digital transformation trends",
            "Remote work culture shift",
            "Changing consumer preferences",
            "Emerging market expansion"
        ]
        
        opportunities.extend(random.sample(base_opportunities, 2))
        return "; ".join(opportunities[:3])
    
    def _assess_risk_level(self) -> str:
        """Assess overall risk level for the business idea."""
        risk_levels = [
            "Low - Stable market with predictable returns",
            "Medium - Moderate risks with good potential",
            "High - Significant risks but high reward potential",
            "Very High - Venture-level risks with uncertain outcomes"
        ]
        return random.choice(risk_levels)


# Factory function to create the tool instance (MCP-style interface)
def create_market_analyst_tool() -> MarketAnalystTool:
    """Factory function to create a market analyst tool instance."""
    return MarketAnalystTool()


# Direct function interface for simple usage
def analyze_business_idea(business_idea: str) -> Dict[str, Any]:
    """
    Simple function interface for market analysis.
    
    Args:
        business_idea (str): The business idea to analyze
        
    Returns:
        Dict[str, Any]: Market analysis report as dictionary
    """
    tool = create_market_analyst_tool()
    report = tool.analyze_market(business_idea)
    
    return {
        "business_idea": report.business_idea,
        "market_size": report.market_size,
        "competition_level": report.competition_level,
        "growth_potential": report.growth_potential,
        "target_demographics": report.target_demographics,
        "key_challenges": report.key_challenges,
        "opportunities": report.opportunities,
        "risk_level": report.risk_level
    }