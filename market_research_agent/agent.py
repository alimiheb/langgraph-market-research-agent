"""
Market Research Agent using LangGraph for stateful workflow management.
This agent performs market research and generates comprehensive reports.
"""

import os
from typing import TypedDict, Annotated, Dict, Any
import operator
from langgraph.graph import StateGraph, END
import google.generativeai as genai
from tools.market_analyst import analyze_business_idea


class AgentState(TypedDict):
    """State object that flows through the LangGraph workflow."""
    business_idea: str
    market_analysis: Dict[str, Any]
    research_complete: bool
    final_report: str
    messages: Annotated[list, operator.add]


class MarketResearchAgent:
    """
    A stateful market research agent built with LangGraph.
    
    The agent has two main states:
    1. Research - Calls the market analyst tool
    2. Report - Uses Gemini API to generate a summary report
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the market research agent.
        
        Args:
            api_key (str): Google Gemini API key
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            print("Warning: No Gemini API key provided. Report generation will use fallback method.")
            self.model = None
        
        # Build the LangGraph workflow
        self.workflow = self._build_workflow()
        self.app = self.workflow.compile()
    
    def _build_workflow(self) -> StateGraph:
        """Build the LangGraph workflow with research and report states."""
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("research", self._research_node)
        workflow.add_node("report", self._report_node)
        
        # Define the workflow flow
        workflow.set_entry_point("research")
        workflow.add_edge("research", "report")
        workflow.add_edge("report", END)
        
        return workflow
    
    def _research_node(self, state: AgentState) -> Dict[str, Any]:
        """
        Research node that calls the market analyst tool.
        
        Args:
            state (AgentState): Current state of the agent
            
        Returns:
            Dict[str, Any]: Updated state with market analysis
        """
        print("🔍 Starting market research...")
        
        try:
            # Call the external market analyst tool
            market_analysis = analyze_business_idea(state["business_idea"])
            
            print(f"✅ Market research completed for: {state['business_idea']}")
            
            return {
                "market_analysis": market_analysis,
                "research_complete": True,
                "messages": [f"Market research completed for: {state['business_idea']}"]
            }
            
        except Exception as e:
            print(f"❌ Error during market research: {str(e)}")
            return {
                "market_analysis": {"error": f"Research failed: {str(e)}"},
                "research_complete": False,
                "messages": [f"Market research failed: {str(e)}"]
            }
    
    def _report_node(self, state: AgentState) -> Dict[str, Any]:
        """
        Report node that generates a summary using Gemini API.
        
        Args:
            state (AgentState): Current state with market analysis
            
        Returns:
            Dict[str, Any]: Updated state with final report
        """
        print("📊 Generating market research report...")
        
        if not state.get("research_complete", False):
            error_report = "Cannot generate report: Market research was not completed successfully."
            return {
                "final_report": error_report,
                "messages": [error_report]
            }
        
        try:
            if self.model:
                # Use Gemini API for report generation
                final_report = self._generate_gemini_report(state)
            else:
                # Fallback to structured report without AI
                final_report = self._generate_fallback_report(state)
            
            print("✅ Market research report generated successfully!")
            
            return {
                "final_report": final_report,
                "messages": ["Market research report generated successfully"]
            }
            
        except Exception as e:
            error_msg = f"Error generating report: {str(e)}"
            print(f"❌ {error_msg}")
            return {
                "final_report": self._generate_fallback_report(state),
                "messages": [error_msg]
            }
    
    def _generate_gemini_report(self, state: AgentState) -> str:
        """Generate report using Gemini AI."""
        market_data = state["market_analysis"]
        
        prompt = f"""
        As a senior business analyst, create a comprehensive market research report for the following business idea:

        Business Idea: {state['business_idea']}

        Market Analysis Data:
        - Market Size: {market_data.get('market_size', 'N/A')}
        - Competition Level: {market_data.get('competition_level', 'N/A')}
        - Growth Potential: {market_data.get('growth_potential', 'N/A')}
        - Target Demographics: {market_data.get('target_demographics', 'N/A')}
        - Key Challenges: {market_data.get('key_challenges', 'N/A')}
        - Opportunities: {market_data.get('opportunities', 'N/A')}
        - Risk Level: {market_data.get('risk_level', 'N/A')}

        Please provide a concise but comprehensive executive summary that includes:
        1. Market Overview
        2. Competitive Landscape
        3. Growth Opportunities
        4. Risk Assessment
        5. Strategic Recommendations

        Keep the tone professional and actionable for business decision-making.
        """
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def _generate_fallback_report(self, state: AgentState) -> str:
        """Generate a structured report without AI as fallback."""
        market_data = state["market_analysis"]
        
        return f"""
# Market Research Report: {state['business_idea']}

## Executive Summary
This report provides a comprehensive analysis of the market opportunity for {state['business_idea']}.

## Market Overview
- **Market Size**: {market_data.get('market_size', 'Data not available')}
- **Target Demographics**: {market_data.get('target_demographics', 'Data not available')}

## Competitive Landscape
- **Competition Level**: {market_data.get('competition_level', 'Data not available')}

## Growth Analysis
- **Growth Potential**: {market_data.get('growth_potential', 'Data not available')}
- **Key Opportunities**: {market_data.get('opportunities', 'Data not available')}

## Risk Assessment
- **Risk Level**: {market_data.get('risk_level', 'Data not available')}
- **Key Challenges**: {market_data.get('key_challenges', 'Data not available')}

## Strategic Recommendations
Based on the analysis, this business idea shows potential in the current market environment. 
Consider the identified challenges and opportunities when developing your business strategy.

---
*Report generated by Market Research Agent*
        """
    
    def research_business_idea(self, business_idea: str) -> Dict[str, Any]:
        """
        Run the complete market research workflow for a business idea.
        
        Args:
            business_idea (str): The business idea to research
            
        Returns:
            Dict[str, Any]: Complete workflow results
        """
        print(f"🚀 Starting market research for: {business_idea}")
        print("=" * 60)
        
        # Initialize state
        initial_state = {
            "business_idea": business_idea,
            "market_analysis": {},
            "research_complete": False,
            "final_report": "",
            "messages": []
        }
        
        # Run the workflow
        final_state = self.app.invoke(initial_state)
        
        print("=" * 60)
        print("🎯 Market research workflow completed!")
        
        return final_state


def create_market_research_agent(api_key: str = None) -> MarketResearchAgent:
    """
    Factory function to create a market research agent.
    
    Args:
        api_key (str): Google Gemini API key (optional)
        
    Returns:
        MarketResearchAgent: Configured agent instance
    """
    return MarketResearchAgent(api_key=api_key)