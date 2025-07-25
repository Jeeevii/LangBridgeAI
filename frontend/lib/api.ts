import type { GenerationRequest, GenerationResult } from "./types"

const BASE_URL = "http://localhost:8000" // change if deploying

export async function generateVideo(request: GenerationRequest): Promise<GenerationResult> {
  const res = await fetch(`${BASE_URL}/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
  })

  if (!res.ok) {
    throw new Error(`Generation failed: ${res.statusText}`)
  }

  const result = await res.json()
  return result as GenerationResult
}

export async function exportVideo(videoId: string, format: "mp4" | "mov" | "gif"): Promise<{ downloadUrl: string }> {
  const res = await fetch(`${BASE_URL}/export/${videoId}?format=${format}`)

  if (!res.ok) {
    throw new Error(`Export failed: ${res.statusText}`)
  }

  return await res.json()
}
