"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Logo } from "@/components/ui/logo"
import { GenerationForm } from "@/components/generation-form"
import { Globe, Sparkles, Zap, Video } from "lucide-react"
import type { GenerationRequest } from "@/lib/types"
import { generateVideo } from "@/lib/api"

export default function Dashboard() {
  const [isGenerating, setIsGenerating] = useState(false)
  const router = useRouter()

  const handleGenerate = async (request: GenerationRequest) => {
    setIsGenerating(true)

    try {
      const result = await generateVideo(request)

      // Store result in sessionStorage for the results page
      sessionStorage.setItem("generationResult", JSON.stringify(result))

      router.push("/results")
    } catch (error) {
      console.error("Generation failed:", error)
      // Handle error (show toast, etc.)
    } finally {
      setIsGenerating(false)
    }
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-muted/20 bg-background/80 backdrop-blur-sm">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-center">
            <Logo />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-6 py-16">
        <div className="mx-auto max-w-4xl text-center">
          {/* Hero Section */}
          <div className="mb-16">
            <h2 className="mb-6 text-5xl font-bold leading-tight">
              <span className="bg-gradient-to-r from-foreground to-muted-foreground bg-clip-text text-transparent">
                Generate AI-Powered
              </span>
              <span className="block bg-gradient-primary bg-clip-text text-transparent">Marketing Videos</span>
            </h2>
            <p className="mx-auto max-w-2xl text-xl text-muted-foreground">
              Create compelling video ads with AI research and cultural insights. Our AI analyzes local trends, consumer
              behavior, and cultural nuances to generate videos that resonate with your target audience.
            </p>
          </div>

          {/* Generation Form */}
          <GenerationForm onGenerate={handleGenerate} isGenerating={isGenerating} />

          {/* Features */}
          <div className="mt-20 grid gap-8 md:grid-cols-4">
            <div className="text-center">
              <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-primary/20 to-accent/20">
                <Globe className="h-6 w-6 text-primary" />
              </div>
              <h3 className="mb-2 text-lg font-semibold text-foreground">Cultural Research</h3>
              <p className="text-sm text-muted-foreground">Deep analysis of local markets and cultural preferences</p>
            </div>
            <div className="text-center">
              <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-primary/20 to-accent/20">
                <Sparkles className="h-6 w-6 text-primary" />
              </div>
              <h3 className="mb-2 text-lg font-semibold text-foreground">AI-Powered</h3>
              <p className="text-sm text-muted-foreground">Advanced AI models trained on marketing best practices</p>
            </div>
            <div className="text-center">
              <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-primary/20 to-accent/20">
                <Video className="h-6 w-6 text-primary" />
              </div>
              <h3 className="mb-2 text-lg font-semibold text-foreground">Video Generation</h3>
              <p className="text-sm text-muted-foreground">Professional-quality videos with voiceover and scripts</p>
            </div>
            <div className="text-center">
              <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-primary/20 to-accent/20">
                <Zap className="h-6 w-6 text-primary" />
              </div>
              <h3 className="mb-2 text-lg font-semibold text-foreground">Lightning Fast</h3>
              <p className="text-sm text-muted-foreground">Generate compelling videos in minutes, not days</p>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
