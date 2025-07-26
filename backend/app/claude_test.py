import boto3
import json
import os
from dotenv import load_dotenv

# Load AWS credentials from .env (optional if already configured via AWS CLI)
load_dotenv()

# Set up Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

# Claude Messages API wrapper
def call_claude_messages_api(prompt_messages):
    model_id = "us.anthropic.claude-sonnet-4-20250514-v1:0"

    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": prompt_messages,
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_k": 250,
        "top_p": 0.9
    }

    response = bedrock.invoke_model(
        modelId=model_id,
        body=json.dumps(payload),
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response['body'].read().decode())
    return response_body['content'][0]['text']


# Main function for testing
if __name__ == "__main__":
    user_input = "Explain what a large language model is in 2 sentences."
    messages = [
        {"role": "user", "content": user_input}
    ]
    
    try:
        output = call_claude_messages_api(messages)
        print("\n🧠 Claude says:\n")
        print(output)
    except Exception as e:
        print(f"❌ Error calling Claude: {e}")

