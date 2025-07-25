import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import type { ResearchContext } from "@/lib/types"
import { Brain, TrendingUp, Users, Target } from "lucide-react"

const categoryIcons = {
  "Cultural Analysis": Users,
  "Product Research": Target,
  "Trend Analysis": TrendingUp,
  "Competitive Analysis": Brain,
}

interface ResearchCardProps {
  research: ResearchContext
}

export function ResearchCard({ research }: ResearchCardProps) {
  const Icon = categoryIcons[research.category as keyof typeof categoryIcons] || Brain

  return (
    <Card className="border border-muted/20 bg-gradient-card backdrop-blur-sm hover:border-primary/30 transition-all duration-300">
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center space-x-2 text-lg">
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary/10">
              <Icon className="h-4 w-4 text-primary" />
            </div>
            <span className="text-foreground">{research.title}</span>
          </CardTitle>
          <Badge variant="outline" className="border-primary/30 text-primary bg-primary/5">
            {research.category}
          </Badge>
        </div>
      </CardHeader>
      <CardContent className="space-y-4">
        <p className="text-sm text-muted-foreground leading-relaxed">{research.summary}</p>

        <div className="space-y-2">
          <div className="flex items-center justify-between text-xs">
            <span className="text-muted-foreground">Confidence Score</span>
            <span className="text-primary font-medium">{research.confidence}%</span>
          </div>
          <Progress value={research.confidence} className="h-2" />
        </div>

        <div className="space-y-1">
          <span className="text-xs font-medium text-muted-foreground">Sources:</span>
          <div className="flex flex-wrap gap-1">
            {research.sources.map((source, index) => (
              <Badge key={index} variant="secondary" className="text-xs bg-muted/50">
                {source}
              </Badge>
            ))}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
