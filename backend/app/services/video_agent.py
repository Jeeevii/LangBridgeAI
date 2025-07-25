import os
import time
import requests
import json
from typing import Optional

class MiniMaxVideoAgent:
    def __init__(self, api_key: str, model: str = "MiniMax-Hailuo-02"):
        self.api_key = api_key
        self.model = model
        self.api_base = "https://api.minimax.io/v1"

    def generate_video(self, prompt: str, duration: int = 6, resolution: str = "1080P") -> Optional[str]:
        url = f"{self.api_base}/video_generation"
        payload = {
            "prompt": prompt,
            "model": self.model,
            "duration": duration,
            "resolution": resolution,
        }
        headers = {
            'authorization': f'Bearer {self.api_key}',
            'content-type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get("task_id")

    def poll_status(self, task_id: str, timeout: int = 300, interval: int = 10) -> Optional[str]:
        url = f"{self.api_base}/query/video_generation?task_id={task_id}"
        headers = {'authorization': f'Bearer {self.api_key}'}
        elapsed = 0

        while elapsed < timeout:
            res = requests.get(url, headers=headers).json()
            status = res.get("status")

            if status == "Success":
                return res["file_id"]
            elif status in {"Fail", "Unknown"}:
                return None

            time.sleep(interval)
            elapsed += interval

        return None

    def download_video(self, file_id: str, output_path: str) -> str:
        url = f"{self.api_base}/files/retrieve?file_id={file_id}"
        headers = {'authorization': f'Bearer {self.api_key}'}
        res = requests.get(url, headers=headers).json()
        download_url = res["file"]["download_url"]

        content = requests.get(download_url).content
        with open(output_path, "wb") as f:
            f.write(content)

        return output_path
