"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Card, CardContent } from "@/components/ui/card"
import { Globe, Zap, Languages } from "lucide-react"
import type { GenerationRequest } from "@/lib/types"

const regions = [
  { value: "japan", label: "Japan" },
  { value: "south-korea", label: "South Korea" },
  { value: "france", label: "France" },
  { value: "germany", label: "Germany" },
  { value: "united-states", label: "United States" },
  { value: "brazil", label: "Brazil" },
]

const languages = [
  { value: "ja", label: "Japanese" },
  { value: "ko", label: "Korean" },
  { value: "fr", label: "French" },
  { value: "de", label: "German" },
  { value: "en", label: "English" },
  { value: "pt", label: "Portuguese" },
]

interface GenerationFormProps {
  onGenerate: (request: GenerationRequest) => void
  isGenerating: boolean
}

export function GenerationForm({ onGenerate, isGenerating }: GenerationFormProps) {
  const [description, setDescription] = useState("")
  const [selectedRegion, setSelectedRegion] = useState("")
  const [selectedLanguage, setSelectedLanguage] = useState("")

  const handleSubmit = () => {
    if (!description.trim() || !selectedRegion || !selectedLanguage) return

    onGenerate({
      description: description.trim(),
      region: selectedRegion,
      language: selectedLanguage,
    })
  }

  const isValid = description.trim() && selectedRegion && selectedLanguage

  return (
    <Card className="border border-muted/20 bg-gradient-card backdrop-blur-sm">
      <CardContent className="p-8">
        <div className="space-y-8">
          {/* Description Input */}
          <div className="space-y-3">
            <label className="block text-sm font-medium text-foreground">Describe your product or campaign</label>
            <Textarea
              placeholder="e.g., Eco-friendly running shoes for urban millennials who care about sustainability and performance. Target audience values quality, innovation, and environmental responsibility..."
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="min-h-[120px] resize-none border-muted/30 bg-background/50 text-base placeholder:text-muted-foreground focus:border-primary focus:ring-primary"
            />
          </div>

          {/* Region and Language Selectors */}
          <div className="grid gap-6 md:grid-cols-2">
            <div className="space-y-3">
              <label className="block text-sm font-medium text-foreground">Target Region</label>
              <Select value={selectedRegion} onValueChange={setSelectedRegion}>
                <SelectTrigger className="border-muted/30 bg-background/50 focus:border-primary focus:ring-primary">
                  <Globe className="mr-2 h-4 w-4 text-muted-foreground" />
                  <SelectValue placeholder="Select region" />
                </SelectTrigger>
                <SelectContent className="border-muted/30 bg-card">
                  {regions.map((region) => (
                    <SelectItem key={region.value} value={region.value}>
                      {region.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-3">
              <label className="block text-sm font-medium text-foreground">Primary Language</label>
              <Select value={selectedLanguage} onValueChange={setSelectedLanguage}>
                <SelectTrigger className="border-muted/30 bg-background/50 focus:border-primary focus:ring-primary">
                  <Languages className="mr-2 h-4 w-4 text-muted-foreground" />
                  <SelectValue placeholder="Select language" />
                </SelectTrigger>
                <SelectContent className="border-muted/30 bg-card">
                  {languages.map((language) => (
                    <SelectItem key={language.value} value={language.value}>
                      {language.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
          </div>

          {/* Generate Button */}
          <Button
            onClick={handleSubmit}
            disabled={!isValid || isGenerating}
            className="h-14 w-full bg-gradient-primary text-lg font-semibold text-primary-foreground hover:opacity-90 disabled:opacity-50 relative overflow-hidden"
          >
            {isGenerating && <div className="absolute inset-0 bg-shimmer animate-shimmer"></div>}
            {isGenerating ? (
              <div className="flex items-center space-x-2">
                <div className="h-5 w-5 animate-spin rounded-full border-2 border-white border-t-transparent" />
                <span>Generating Video...</span>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <Zap className="h-5 w-5" />
                <span>Generate AI Video</span>
              </div>
            )}
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}
