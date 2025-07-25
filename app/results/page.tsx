"use client"

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Logo } from "@/components/ui/logo"
import { ResearchCard } from "@/components/ui/research-card"
import { VideoPlayer } from "@/components/ui/video-player"
import { ArrowLeft, Clock, CheckCircle, Search } from "lucide-react"
import type { GenerationResult } from "@/lib/types"
import { exportVideo } from "@/lib/api"

export default function ResultsPage() {
  const [result, setResult] = useState<GenerationResult | null>(null)
  const [isExporting, setIsExporting] = useState(false)
  const router = useRouter()

  useEffect(() => {
    const storedResult = sessionStorage.getItem("generationResult")
    if (storedResult) {
      setResult(JSON.parse(storedResult))
    } else {
      router.push("/")
    }
  }, [router])

  const handleExport = async (format: "mp4" | "mov" | "gif") => {
    if (!result) return

    setIsExporting(true)
    try {
      const exportResult = await exportVideo(result.generatedVideo.id, format)
      // In a real app, you'd trigger the download here
      console.log("Export URL:", exportResult.downloadUrl)
      // You could show a success toast here
    } catch (error) {
      console.error("Export failed:", error)
    } finally {
      setIsExporting(false)
    }
  }

  if (!result) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-2 border-primary border-t-transparent" />
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-muted/20 bg-background/80 backdrop-blur-sm">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <Button
              variant="ghost"
              onClick={() => router.push("/")}
              className="text-muted-foreground hover:text-foreground"
            >
              <ArrowLeft className="mr-2 h-4 w-4" />
              New Generation
            </Button>
            <Logo />
            <div className="w-32" /> {/* Spacer for centering */}
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-6 py-8">
        {/* Generation Summary */}
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-3xl font-bold text-foreground">Generated Video</h2>
            <div className="flex items-center space-x-4">
              <Badge className="bg-success/10 text-success border-success/20">
                <CheckCircle className="h-3 w-3 mr-1" />
                Completed
              </Badge>
              <Badge variant="outline" className="border-primary/30 text-primary">
                <Clock className="h-3 w-3 mr-1" />
                {result.processingTime}s
              </Badge>
            </div>
          </div>

          <Card className="border border-muted/20 bg-gradient-card backdrop-blur-sm">
            <CardContent className="p-6">
              <div className="flex items-start space-x-4">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10">
                  <Search className="h-5 w-5 text-primary" />
                </div>
                <div className="flex-1">
                  <h3 className="mb-2 font-semibold text-foreground">Campaign Brief</h3>
                  <p className="text-muted-foreground mb-3">{result.request.description}</p>
                  <div className="flex space-x-2">
                    <Badge className="bg-primary/10 text-primary border-primary/20">
                      {result.request.region.charAt(0).toUpperCase() + result.request.region.slice(1)}
                    </Badge>
                    <Badge className="bg-accent/10 text-accent border-accent/20">
                      {result.request.language.toUpperCase()}
                    </Badge>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <div className="grid gap-8 lg:grid-cols-2">
          {/* Research Context */}
          <div className="space-y-6">
            <div>
              <h3 className="text-2xl font-semibold text-foreground mb-2">Research Context</h3>
              <p className="text-muted-foreground mb-6">
                Our AI analyzed these key areas to generate culturally relevant and effective marketing content.
              </p>
            </div>

            <div className="space-y-4">
              {result.researchContext.map((research) => (
                <ResearchCard key={research.id} research={research} />
              ))}
            </div>
          </div>

          {/* Generated Video */}
          <div className="space-y-6">
            <div>
              <h3 className="text-2xl font-semibold text-foreground mb-2">Generated Video</h3>
              <p className="text-muted-foreground mb-6">
                Your AI-generated marketing video based on the research insights and cultural analysis.
              </p>
            </div>

            <VideoPlayer video={result.generatedVideo} onExport={handleExport} />
          </div>
        </div>

        {/* Generate Another Button */}
        <div className="mt-12 text-center">
          <Button
            onClick={() => router.push("/")}
            className="bg-gradient-primary text-primary-foreground hover:opacity-90"
            size="lg"
          >
            Generate Another Video
          </Button>
        </div>
      </main>
    </div>
  )
}
