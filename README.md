# Agentic AI Research Agent 🤖

An autonomous research agent that makes strategic decisions about research strategy, evaluates source credibility, detects contradictions, and generates evidence-based reports.

## Quick Start

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Setup API Key
Create a `.env` file in the project root:
```
GROQ_API_KEY=gsk_your_api_key_here
```

Get your free API key from: https://console.groq.com

### 4. Run the Application

**Option A: Web Interface (Recommended)**
```bash
streamlit run agentic_app.py
```
Opens at `http://localhost:8501`

**Option B: Command Line**
```bash
python agentic_agent.py
```

---

## How It Works: 6 Steps

The agent autonomously researches a topic by making decisions at each step:

### Step 1: Plan Strategy 🧠
Agent receives a topic and DECIDES what research angles are needed.
```
Example: "AI in Healthcare"
Agent decides: "I need mainstream sources, academic research, and recent news"
```

### Step 2: Execute Searches 🔍
Agent executes 4 targeted searches based on the strategy it created.
```
Search 1: "AI in healthcare 2025"
Search 2: "AI diagnosis accuracy research"
Search 3: "AI healthcare safety concerns"
Search 4: "AI regulation medicine"
```

### Step 3: Evaluate Sources ⭐
Agent ranks each source by credibility (1-10) and extracts key claims.
```
Source A: Credibility 9, claims: [AI improving efficiency, safety concerns]
Source B: Credibility 7, claims: [AI replacing jobs, regulatory gaps]
```

### Step 4: Analyze Consensus 🔄
Agent finds what sources AGREE on vs what they DISAGREE about.
```
Consensus: 85% agree AI is being deployed
Contradiction: 50% say it's ready for widespread adoption, 50% say it needs more testing
```

### Step 5: Decide to Iterate 🔁
Agent checks: "Did I find contradictions?"
- YES → Researches contradictions deeper (loops back to Step 2)
- NO → Proceeds to Step 6

```
Agent finds: "2 contradictions detected"
Agent decides: "I should research these deeper"
Agent iterates: performs additional targeted searches
```

### Step 6: Create Report 📊
Agent creates a professional report showing:
- What we know (high confidence)
- What's debated (with evidence for each side)
- Confidence levels
- What we still need to know

---

## What Makes It Different From Other LLMs

### LLM Approach (ChatGPT, Claude)
```
Input: "Research AI in healthcare"
  ↓
LLM generates report
  ↓
Output: Generic answer
```
**Problem:** Black box - you don't know what it actually researched or how it decided to iterate.

### Agentic Approach (This Project)
```
Input: "Research AI in healthcare"
  ↓
Agent PLANS what to search (autonomous decision)
  ↓
Agent SEARCHES strategically (4 different queries)
  ↓
Agent EVALUATES sources (ranks by credibility)
  ↓
Agent ANALYZES consensus (finds contradictions)
  ↓
Agent DECIDES: "Iterate or report?" (branching logic)
  ↓
Agent CREATES report (based on findings)
  ↓
Output: Report + Metadata (proves what agent did)
```

### Key Differences

| Feature | LLM | This Agent |
|---------|-----|-----------|
| **Decision Making** | No (just generates) | Yes (decides at each step) |
| **Multiple Searches** | No (one response) | Yes (4 targeted searches) |
| **Source Evaluation** | No | Yes (credibility scores) |
| **Contradiction Detection** | Maybe (buried in text) | Yes (explicit) |
| **Iteration** | No | Yes (if contradictions found) |
| **Transparency** | No (black box) | Yes (metadata shows decisions) |
| **Branching Logic** | No (linear) | Yes (if/else decisions) |

**In Short:** An LLM generates text. This agent makes decisions and shows its reasoning.

---

## Example Output

### What the Agent Decides
```json
{
  "searches_performed": 5,
  "sources_evaluated": 5,
  "contradictions_found": 2,
  "iterations_performed": 1,
  "source_agreement_score": 75%
}
```

This metadata PROVES the agent made autonomous decisions.

### What the Report Shows
```markdown
# AI in Healthcare 2025

## What We Know (High Confidence - 85% agreement)
- AI is being deployed in diagnostic imaging
- AI improves efficiency in clinical workflows

## What's Debated (Contradictions)
### Position A: Rapid widespread adoption
- Evidence: Company announcements, pilot programs
- Sources: 40% of evaluated sources

### Position B: Slower adoption due to barriers
- Evidence: Regulatory concerns, safety testing gaps
- Sources: 35% of evaluated sources

## Confidence Level
Medium-High: Strong agreement on benefits, disagreement on timeline
```

---

## File Structure

```
project/
├── agentic_agent.py          # Core agent logic
├── agentic_app.py            # Streamlit web interface
├── requirements.txt          # Python dependencies
├── .env                      # Your API key (don't push!)
├── README.md                 # This file
```

---

## Troubleshooting

**"GROQ_API_KEY not found"**
- Check .env file exists in project root
- Verify format: `GROQ_API_KEY=gsk_...` (no quotes)
- Restart Python after creating .env

**Research takes 2-3 minutes**
- This is normal - the agent makes 4-5 LLM calls
- Shows "Agent is researching..." in web UI

**Report looks the same every time**
- This is expected - underlying facts don't change
- But the agent's decisions and metadata might differ based on mode

---

## Cost

- **Free tier:** 100 requests/day (Groq)
- **Per research:** ~4-5 requests (20 researches/day free)
- **Cost if paying:** ~$0.05-0.10 per research

---

## Next Steps

1. Get free Groq API key: https://console.groq.com
2. Create .env file with your key
3. Run: `streamlit run agentic_app.py`
4. Try different topics and debate modes
5. Deploy to Streamlit Cloud for live demo

---

## Interview Explanation

**Short version (2 min):**
> "I built an autonomous research agent. It doesn't just generate text - it makes decisions at 6 steps: planning what to research, executing searches, evaluating sources, finding contradictions, deciding whether to iterate, and creating reports. The metadata proves what decisions it made."

**Key point:**
> "Unlike ChatGPT, this agent shows its reasoning and branches based on what it discovers. If it finds contradictions, it iterates. It's not a black box - you can see everything it decided to do."

---

For detailed explanations, see the code comments in `agentic_agent.py`.
