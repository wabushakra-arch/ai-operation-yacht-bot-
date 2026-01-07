# Deploying to Streamlit Cloud

## Quick Deploy

### Step 1: Connect GitHub Repository
1. Go to https://streamlit.io/cloud
2. Click **"New App"**
3. Select your GitHub repo: `wabushakra-arch/ai-operation-yacht-bot-`
4. Select the branch: `main`
5. Select the main file: `streamlit_app.py`

### Step 2: Add API Key to Streamlit Secrets
1. After deployment, click on the app menu (⋮) → **Settings**
2. Click **"Secrets"** in the left panel
3. Add your OpenAI API key in TOML format:

```toml
openai_api_key = "sk-proj-your-actual-api-key-here"
```

**Format is critical!** It must be:
- `openai_api_key = "your-key"`  ✅ Correct
- NOT: `openai_api_key='sk-proj-...'` ❌ Wrong format

### Step 3: Deploy
Click **"Deploy"** and wait for your app to go live.

## Live URL
Once deployed, your app will be available at:
```
https://share.streamlit.io/?utm_source=streamlit&utm_medium=referral&utm_campaign=main&utm_content=yacht-operations-bot
```

## Usage
1. Select an operation (A-G) from the sidebar
2. Enter your request details
3. Click **"Generate Response"**
4. Copy the AI-generated content

## Tips
- Keep your API key secure - never commit it to GitHub
- Use Streamlit Secrets for production deployments
- Test locally first with `streamlit run streamlit_app.py`

## Troubleshooting
- **"API Key not found"**: Ensure you added it correctly to Streamlit Secrets in TOML format
- **Module errors**: Make sure all dependencies are in `requirements.txt`
- **Slow responses**: OpenAI API calls can take 5-10 seconds
