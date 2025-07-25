import { Sparkles } from "lucide-react"

export function Logo({ className = "" }: { className?: string }) {
  return (
    <div className={`flex items-center space-x-3 ${className}`}>
      <div className="relative">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-primary">
          <Sparkles className="h-6 w-6 text-primary-foreground" />
        </div>
        <div className="absolute inset-0 rounded-xl bg-gradient-primary opacity-50 blur-lg animate-pulse-glow"></div>
      </div>
      <h1 className="text-2xl font-bold bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
        LangBridge AI
      </h1>
    </div>
  )
}
