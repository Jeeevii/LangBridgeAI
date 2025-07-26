import boto3
import json
from typing import Dict, Any, Optional
from botocore.exceptions import ClientError

class BedrockService:
    def __init__(self, region_name: str = "us-east-1"):
        self.bedrock = boto3.client(
            service_name="bedrock-runtime",
            region_name=region_name
        )
    
    def generate_content(self, prompt: str, model_id: str = "us.anthropic.claude-sonnet-4-20250514-v1:0") -> str:
        """Generate content using Amazon Bedrock with Claude Sonnet 3"""

        try:
            body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 4000,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
            
            response = self.bedrock.invoke_model(
                modelId=model_id,
                body=json.dumps(body)
            )
            
            response_body = json.loads(response["body"].read())
            return response_body["content"][0]["text"]
            
        except ClientError as e:
            raise Exception(f"Bedrock API error: {e}")
    
    def generate_video_script(self, description: str, region: str, language: str, target_audience: Optional[str] = None) -> str:
        """Generate video script based on requirements"""
        audience_text = f" for {target_audience}" if target_audience else ""
        
        prompt = f"""Create a compelling video script in {language} about "{description}" 
        targeted for the {region} region{audience_text}.
        
        The script should be:
        - Engaging and informative
        - Culturally appropriate for {region}
        - 2-3 minutes long when spoken
        - Include clear introduction, main content, and conclusion
        
        Format the response as a clean script without additional formatting."""
        
        return self.generate_content(prompt)
    
    def generate_research_context(self, description: str, region: str) -> Dict[str, Any]:
        """Generate research context for the video topic"""
        prompt = f"""Provide research context for a video about "{description}" in {region}.
        
        Return information about:
        - Key facts and statistics
        - Cultural considerations for {region}
        - Relevant trends and insights
        - Credible sources
        
        Format as informative bullet points."""
        
        research_content = self.generate_content(prompt)
        
        return {
            "category": "AI Generated Research",
            "title": f"Research: {description}",
            "summary": research_content,
            "sources": ["Amazon Bedrock AI Analysis"],
            "confidence": 85
        }
    def find_trend_websites(self, marketing_prompt: str, region: str = "japan", product_category: Optional[str] = None) -> Dict[str, Any]:
        """Find trending websites and reviews based on a marketing message"""
        
        category_text = f" in the category of {product_category}" if product_category else ""
        
        prompt = f"""
        Based on the following marketing message:

        \"{marketing_prompt}\"

        Do the following:
        1. Identify current consumer trends{category_text}.
        2. List 5 active websites that:
        - Sell relevant products
        - Feature popular or trending items
        - Include customer reviews
        3. For each website, summarize what type of products they offer and any interesting review trends.
        4. Focus on sources relevant to the {region} region.

        Format your response as a list of websites with:
        - Website Name & URL
        - Summary of Products
        - Review or Trend Insight
        """
            
        result = self.generate_content(prompt)
        
        return {
            "category": "Web Trend Discovery",
            "title": f"Trend Sites for: {marketing_prompt[:40]}...",
            "results": result,
            "source": "Amazon Bedrock AI (Claude Sonnet)",
            "confidence": 80
        }
