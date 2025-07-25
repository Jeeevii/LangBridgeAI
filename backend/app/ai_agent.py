import json
from typing import List, Dict, Any
from aws_bedrock import BedrockService

class VideoGenerationAgent:
    def __init__(self):
        self.bedrock = BedrockService()
        self.memory = []
        self.tools = {
            "research": self._research_tool,
            "script": self._script_tool,
            "validate": self._validate_tool
        }
    
    def _research_tool(self, topic: str, region: str) -> str:
        """Research tool for gathering information"""
        prompt = f"Research {topic} for {region}. Provide key facts and cultural insights."
        return self.bedrock.generate_content(prompt)
    
    def _script_tool(self, topic: str, research: str, language: str) -> str:
        """Script generation tool"""
        prompt = f"Create video script for '{topic}' in {language}. Use this research: {research}"
        return self.bedrock.generate_content(prompt)
    
    def _validate_tool(self, script: str, requirements: str) -> str:
        """Validation tool"""
        prompt = f"Validate this script meets requirements: {requirements}\n\nScript: {script}"
        return self.bedrock.generate_content(prompt)
    
    def plan_task(self, request: Dict[str, Any]) -> List[str]:
        """Agent planning - decides what steps to take"""
        planning_prompt = f"""
        Task: Generate video for "{request['description']}" in {request['language']} for {request['region']}
        
        Plan the steps needed. Choose from: research, script, validate
        Return JSON array of steps: ["step1", "step2", "step3"]
        """
        
        plan = self.bedrock.generate_content(planning_prompt)
        try:
            return json.loads(plan.strip())
        except:
            return ["research", "script", "validate"]
    
    def execute_workflow(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Main agent workflow"""
        # Step 1: Plan
        steps = self.plan_task(request)
        results = {}
        
        # Step 2: Execute each step
        for step in steps:
            if step == "research":
                results["research"] = self._research_tool(request["description"], request["region"])
            elif step == "script":
                research = results.get("research", "")
                results["script"] = self._script_tool(request["description"], research, request["language"])
            elif step == "validate":
                script = results.get("script", "")
                results["validation"] = self._validate_tool(script, f"Language: {request['language']}, Region: {request['region']}")
        
        # Step 3: Store in memory
        self.memory.append({
            "request": request,
            "steps": steps,
            "results": results
        })
        
        return results

# Simple usage
def create_agent_video(description: str, region: str, language: str) -> Dict[str, Any]:
    agent = VideoGenerationAgent()
    request = {
        "description": description,
        "region": region, 
        "language": language
    }
    return agent.execute_workflow(request)