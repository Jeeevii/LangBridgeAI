import type { Config } from "tailwindcss"

const config: Config = {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
    "*.{js,ts,jsx,tsx,mdx}",
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "#0A0F1C",
        foreground: "#F8FAFC",
        primary: {
          DEFAULT: "#00D4FF",
          foreground: "#0A0F1C",
          50: "#E6FDFF",
          100: "#B3F9FF",
          500: "#00D4FF",
          600: "#00B8E6",
          700: "#0099CC",
        },
        secondary: {
          DEFAULT: "#1E293B",
          foreground: "#F1F5F9",
        },
        accent: {
          DEFAULT: "#6366F1",
          foreground: "#F8FAFC",
          50: "#EEF2FF",
          500: "#6366F1",
        },
        muted: {
          DEFAULT: "#1E2A3A",
          foreground: "#94A3B8",
        },
        card: {
          DEFAULT: "#0F1629",
          foreground: "#F8FAFC",
        },
        success: "#10B981",
        warning: "#F59E0B",
        destructive: "#EF4444",
      },
      backgroundImage: {
        "gradient-primary": "linear-gradient(135deg, #00D4FF 0%, #6366F1 100%)",
        "gradient-card": "linear-gradient(135deg, rgba(15, 22, 41, 0.8) 0%, rgba(30, 42, 58, 0.4) 100%)",
        shimmer: "linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.1), transparent)",
      },
      animation: {
        shimmer: "shimmer 2s infinite",
        "pulse-glow": "pulse-glow 2s ease-in-out infinite alternate",
      },
      keyframes: {
        shimmer: {
          "0%": { transform: "translateX(-100%)" },
          "100%": { transform: "translateX(100%)" },
        },
        "pulse-glow": {
          "0%": { boxShadow: "0 0 20px rgba(0, 212, 255, 0.3)" },
          "100%": { boxShadow: "0 0 40px rgba(0, 212, 255, 0.6)" },
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config

export default config
