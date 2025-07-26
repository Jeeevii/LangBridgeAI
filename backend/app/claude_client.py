# claude_client.py

import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

def call_claude_messages_api(prompt_messages, system_prompt="You are a helpful assistant."):
    model_id = "anthropic.claude-3-sonnet-20240229"

    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "system": system_prompt,
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

    full_response = ""
    for event in response['body']:
        chunk = json.loads(event['chunk']['bytes'].decode())
        if "delta" in chunk:
            full_response += chunk["delta"].get("text", "")
    
    return full_response
