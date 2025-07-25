#!/usr/bin/env python3
from dotenv import load_dotenv
from ai_agent import create_agent_video

load_dotenv()

def test_agent():
    """Test AI Agent workflow"""
    print("Testing AI Agent workflow...")
    
    result = create_agent_video(
        description="Benefits of renewable energy",
        region="Europe", 
        language="English"
    )
    
    print("\n--- Agent Results ---")
    for key, value in result.items():
        print(f"{key.upper()}:")
        print(value[:200] + "..." if len(value) > 200 else value)
        print()

if __name__ == "__main__":
    test_agent()