"use client"

import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import type { GeneratedVideo } from "@/lib/types"
import { Play, Download, Share, Clock, Mic } from "lucide-react"

interface VideoPlayerProps {
  video: GeneratedVideo
  onExport: (format: "mp4" | "mov" | "gif") => void
}

export function VideoPlayer({ video, onExport }: VideoPlayerProps) {
  return (
    <Card className="border border-muted/20 bg-gradient-card backdrop-blur-sm">
      <CardContent className="p-6">
        <div className="space-y-6">
          {/* Video Preview */}
          <div className="relative aspect-video rounded-lg overflow-hidden bg-muted/20">
            <img
              src={video.thumbnailUrl || "/placeholder.svg"}
              alt={video.title}
              className="w-full h-full object-cover"
            />
            <div className="absolute inset-0 flex items-center justify-center bg-black/20">
              <Button size="lg" className="rounded-full bg-primary/90 hover:bg-primary">
                <Play className="h-6 w-6 ml-1" />
              </Button>
            </div>
            <div className="absolute bottom-4 right-4">
              <Badge className="bg-black/50 text-white">
                <Clock className="h-3 w-3 mr-1" />
                {video.duration}s
              </Badge>
            </div>
          </div>

          {/* Video Info */}
          <div className="space-y-4">
            <div>
              <h3 className="text-xl font-semibold text-foreground mb-2">{video.title}</h3>
              <p className="text-muted-foreground">{video.description}</p>
            </div>

            {/* Voice Over Info */}
            <div className="flex items-center space-x-4 p-3 rounded-lg bg-muted/20">
              <Mic className="h-4 w-4 text-primary" />
              <div className="flex-1">
                <span className="text-sm font-medium text-foreground">Voice Over: </span>
                <span className="text-sm text-muted-foreground">
                  {video.voiceOver.gender} • {video.voiceOver.language} ({video.voiceOver.accent})
                </span>
              </div>
            </div>

            {/* Script Preview */}
            <div className="space-y-2">
              <h4 className="text-sm font-medium text-foreground">Script Preview</h4>
              <div className="p-4 rounded-lg bg-background/50 border border-muted/20">
                <p className="text-sm text-muted-foreground leading-relaxed">{video.script}</p>
              </div>
            </div>

            {/* Export Options */}
            <div className="flex flex-wrap gap-3 pt-4 border-t border-muted/20">
              <Button onClick={() => onExport("mp4")} className="bg-primary hover:bg-primary/90">
                <Download className="h-4 w-4 mr-2" />
                Export MP4
              </Button>
              <Button
                variant="outline"
                onClick={() => onExport("mov")}
                className="border-muted/30 hover:border-primary"
              >
                Export MOV
              </Button>
              <Button
                variant="outline"
                onClick={() => onExport("gif")}
                className="border-muted/30 hover:border-primary"
              >
                Export GIF
              </Button>
              <Button variant="outline" className="border-muted/30 hover:border-primary bg-transparent">
                <Share className="h-4 w-4 mr-2" />
                Share
              </Button>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
