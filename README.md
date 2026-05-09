# NutriMind AI

Minimal, hackathon-ready AI nutrition tracker.

## Features
- Track calories and protein
- Suggest allergy-safe meals
- Generate simple recipes
- Provide daily health tips
- Powered by Claude 3 Haiku for high-speed, cost-effective inference.

## Tech Stack
- **Backend:** Python / FastAPI
- **Frontend:** Single `index.html` with vanilla JS/CSS
- **Intelligence:** Anthropic Claude API

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your API Key:
   ```bash
   # Linux/macOS
   export ANTHROPIC_API_KEY="your-api-key"
   
   # Windows PowerShell
   $env:ANTHROPIC_API_KEY="your-api-key"
   ```
3. Run the app:
   ```bash
   uvicorn app:app --reload --port 8080
   ```
4. Visit `http://localhost:8080`

## Deployment (Google Cloud Run)
Requirements: Google Cloud SDK installed and authenticated.

```bash
gcloud run deploy nutrimind-ai \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars ANTHROPIC_API_KEY=your-api-key
```

## Repository Information
- **Size:** < 1 MB
- **Branches:** Setup uses a single `main` branch.
- **GitHub Link:** *[Insert Link Here]*
