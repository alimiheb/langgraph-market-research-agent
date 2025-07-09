"""
Main entry point for the Market Research Agent.
This script demonstrates the complete workflow of market research and reporting.
"""

import os
import sys
from agent import create_market_research_agent


def main():
    """Main function to run the market research agent."""
    print("🏢 Market Research Agent")
    print("=" * 50)
    
    # Sample business ideas from Challenge 1 or user input
    sample_business_ideas = [
        "AI-powered personal fitness coach app",
        "Sustainable food packaging for restaurants", 
        "Virtual reality training platform for medical students",
        "Smart home energy management system",
        "Subscription box for local artisan products"
    ]
    
    # Get Gemini API key from environment or user input
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("⚠️  Gemini API key not found in environment variables.")
        print("The agent will use a fallback report generation method.")
        print("To use Gemini AI, set the GEMINI_API_KEY environment variable.")
        print()
    
    # Create the market research agent
    try:
        agent = create_market_research_agent(api_key=api_key)
        print("✅ Market Research Agent initialized successfully!")
        print()
    except Exception as e:
        print(f"❌ Error initializing agent: {str(e)}")
        return
    
    # Get business idea from user or use sample
    print("Choose a business idea to research:")
    print("0. Enter your own business idea")
    for i, idea in enumerate(sample_business_ideas, 1):
        print(f"{i}. {idea}")
    
    try:
        choice = input("\nEnter your choice (0-5): ").strip()
        
        if choice == "0":
            business_idea = input("Enter your business idea: ").strip()
            if not business_idea:
                print("❌ No business idea provided. Exiting.")
                return
        elif choice in [str(i) for i in range(1, len(sample_business_ideas) + 1)]:
            business_idea = sample_business_ideas[int(choice) - 1]
        else:
            print("❌ Invalid choice. Using default business idea.")
            business_idea = sample_business_ideas[0]
    
    except KeyboardInterrupt:
        print("\n👋 Operation cancelled by user.")
        return
    except Exception as e:
        print(f"❌ Error getting user input: {str(e)}")
        business_idea = sample_business_ideas[0]
    
    print(f"\n🎯 Selected business idea: {business_idea}")
    print()
    
    # Run the market research workflow
    try:
        results = agent.research_business_idea(business_idea)
        
        # Display results
        print("\n" + "=" * 60)
        print("📋 MARKET RESEARCH RESULTS")
        print("=" * 60)
        
        # Show market analysis data
        if results.get("market_analysis") and not results["market_analysis"].get("error"):
            print("\n🔍 Market Analysis Data:")
            print("-" * 30)
            market_data = results["market_analysis"]
            for key, value in market_data.items():
                if key != "business_idea":
                    formatted_key = key.replace("_", " ").title()
                    print(f"• {formatted_key}: {value}")
        
        # Show final report
        if results.get("final_report"):
            print("\n📊 Executive Summary Report:")
            print("-" * 40)
            print(results["final_report"])
        
        # Show workflow messages
        if results.get("messages"):
            print("\n📝 Workflow Status:")
            print("-" * 20)
            for message in results["messages"]:
                print(f"• {message}")
        
        print("\n" + "=" * 60)
        print("✅ Market research completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during market research: {str(e)}")
        print("Please check your configuration and try again.")


def demo_mode():
    """Run a quick demo with predefined business idea."""
    print("🚀 Running Market Research Agent Demo")
    print("=" * 40)
    
    # Use a predefined business idea for demo
    demo_business_idea = "AI-powered personal fitness coach app"
    
    try:
        agent = create_market_research_agent()
        results = agent.research_business_idea(demo_business_idea)
        
        print(f"\n📊 Demo Results for: {demo_business_idea}")
        print("=" * 50)
        
        if results.get("final_report"):
            print(results["final_report"])
        
        return results
        
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")
        return None


if __name__ == "__main__":
    # Check if demo mode is requested
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_mode()
    else:
        main()