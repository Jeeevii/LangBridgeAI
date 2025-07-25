#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from aws_bedrock import BedrockService

# Load environment variables
load_dotenv()

def test_bedrock():
    """Test Bedrock connection and generate content"""
    try:
        # Initialize Bedrock service
        bedrock = BedrockService(region_name=os.getenv("AWS_REGION", "us-east-1"))
        
        # Test prompt
        prompt = "Write a short story about AI helping humans in 100 words."
        
        print("Calling Bedrock...")
        response = bedrock.generate_content(prompt)
        
        print("\n--- Bedrock Response ---")
        print(response)
        print("\n--- Test Complete ---")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_bedrock()