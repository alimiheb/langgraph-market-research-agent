# Market Research Agent

This project implements a market research agent using LangGraph for stateful workflow management and an external market analysis tool that simulates MCP (Model Context Protocol) functionality.

## Project Structure

```
market_research_agent/
├── main.py              # Entry point and user interface
├── agent.py             # LangGraph-based stateful agent
├── tools/
│   └── market_analyst.py # External market analysis tool (MCP-style)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Features

- **Stateful Workflow**: Uses LangGraph to manage a two-state workflow (research → report)
- **External Tool Integration**: Simulates MCP-discoverable market analysis tool
- **AI-Powered Reports**: Uses Google Gemini API for intelligent report generation
- **Fallback Support**: Works without API keys using structured reports
- **Interactive Interface**: User-friendly command-line interface

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Gemini API key (optional):**
   ```bash
   # Windows PowerShell
   $env:GEMINI_API_KEY = "your-api-key-here"
   
   # Windows Command Prompt
   set GEMINI_API_KEY=your-api-key-here
   
   # Linux/macOS
   export GEMINI_API_KEY="your-api-key-here"
   ```

## Usage

### Interactive Mode
```bash
python main.py
```

### Demo Mode
```bash
python main.py --demo
```

## How It Works

### 1. Market Analyst Tool (`tools/market_analyst.py`)
- Simulates an external MCP-discoverable tool
- Provides comprehensive market analysis including:
  - Market size estimation
  - Competition analysis
  - Growth potential assessment
  - Target demographics identification
  - Risk and opportunity analysis

### 2. LangGraph Agent (`agent.py`)
- **Research State**: Calls the market analyst tool to gather data
- **Report State**: Uses Gemini AI to generate executive summaries
- Maintains state throughout the workflow
- Handles errors gracefully with fallback options

### 3. Main Application (`main.py`)
- Provides user interface for business idea input
- Orchestrates the complete workflow
- Displays formatted results
- Supports both interactive and demo modes

## Example Output

```
🔍 Starting market research...
✅ Market research completed for: AI-powered personal fitness coach app
📊 Generating market research report...
✅ Market research report generated successfully!

📋 MARKET RESEARCH RESULTS
Market Size: $1B - $10B (Large market)
Competition Level: High - Saturated market with established players
Growth Potential: High (15-30% annually) - Fast-growing market
...
```

## Technical Details

- **State Management**: TypedDict with annotations for proper state flow
- **Error Handling**: Comprehensive try-catch blocks with user-friendly messages
- **Modular Design**: Clear separation between tool, agent, and interface layers
- **Extensibility**: Easy to add new states or modify the workflow

## Dependencies

- `langgraph`: For stateful workflow management
- `google-generativeai`: For AI-powered report generation
- `python-dotenv`: For environment variable management
- `typing-extensions`: For enhanced type hints
