export interface GenerationRequest {
  description: string
  region: string
  language: string
  targetAudience?: string
}

export interface ResearchContext {
  id: string
  category: string
  title: string
  summary: string
  sources: string[]
  confidence: number
}

export interface GeneratedVideo {
  id: string
  title: string
  description: string
  duration: number
  thumbnailUrl: string
  videoUrl: string
  script: string
  voiceOver: {
    language: string
    accent: string
    gender: string
  }
  createdAt: string
}

export interface GenerationResult {
  id: string
  request: GenerationRequest
  researchContext: ResearchContext[]
  generatedVideo: GeneratedVideo
  processingTime: number
  status: "completed" | "processing" | "failed"
}
