"""
Streamlit UI for Agentic Research Agent
Clean, professional interface showing agent decision-making
"""

import streamlit as st
import os
from dotenv import load_dotenv
from agentic_agent import AgenticResearchAgent
import json
from datetime import datetime

load_dotenv()

# Page config
st.set_page_config(
    page_title="Agentic AI Research Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
        font-size: 16px;
    }
    .agent-metadata {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
        border-left: 4px solid #1f77b4;
    }
    .report-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .decision-box {
        background-color: #fff3cd;
        padding: 12px;
        border-radius: 6px;
        margin-top: 10px;
        border-left: 4px solid #ff9800;
    }
    .metric-card {
        background-color: #f0f7ff;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🤖 Agentic AI Research Agent</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Autonomous research with decision-making, fact-checking, and iterative refinement</p>', unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    debate_mode = st.selectbox(
        "Research Mode",
        ["balanced", "skeptical", "comprehensive"],
        help="How the agent approaches the research"
    )
    
    show_metadata = st.checkbox(
        "Show Agent Metadata",
        value=True,
        help="Display agent's decision-making process"
    )
    
    st.divider()
    st.markdown("**What Makes This Agentic:**")
    st.markdown("""
    - 🧠 Plans research strategy (not predetermined)
    - 🔍 Searches multiple angles
    - ⭐ Evaluates source credibility
    - 🔄 Detects contradictions
    - 🔁 Iterates when needed
    - ✓ Verifies claims
    - 📊 Evidence-based reporting
    """)
    
    st.divider()
    st.markdown("**Example Topics:**")
    st.markdown("""
    - AI in healthcare
    - Climate change solutions
    - Remote work effectiveness
    - Cryptocurrency regulation
    - Mental health interventions
    """)

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    research_topic = st.text_input(
        "Enter research topic:",
        placeholder="e.g., AI ethics in 2025",
        label_visibility="collapsed"
    )

with col2:
    research_button = st.button("🔬 Research", use_container_width=True, type="primary")

# Session state
if "research_result" not in st.session_state:
    st.session_state.research_result = None
    st.session_state.research_complete = False

# Research execution
if research_button:
    if not research_topic.strip():
        st.error("❌ Please enter a research topic")
    else:
        try:
            with st.spinner("🤖 Agent is researching... This may take 2-3 minutes"):
                agent = AgenticResearchAgent()
                result = agent.research(research_topic, debate_mode=debate_mode)
                st.session_state.research_result = result
                st.session_state.research_complete = True
            
            st.success("✅ Research complete!")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Make sure you have:")
            st.info("1. Groq API key in .env file (GROQ_API_KEY=gsk_...)")
            st.info("2. Internet connection")
            st.info("3. Valid Groq API key from console.groq.com")

# Display results
if st.session_state.research_complete and st.session_state.research_result:
    result = st.session_state.research_result
    
    # Report header
    st.divider()
    st.markdown(f"## 📋 Research Report: {result['topic']}")
    
    # Agent decision overview
    metadata = result['agent_metadata']
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Searches", metadata['searches_performed'])
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Sources Evaluated", metadata['sources_evaluated'])
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Agreement Score", f"{metadata['source_agreement_score']}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Iterations", metadata['iterations_performed'])
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Agent decisions explanation
    if show_metadata:
        with st.expander("🤖 Agent Decision-Making", expanded=True):
            st.markdown("### Research Strategy")
            strategy = metadata['strategy']
            st.markdown(f"**Angles Researched:** {', '.join(strategy.get('research_angles', []))}")
            st.markdown(f"**Why:** {strategy.get('why_this_strategy', 'Multi-angle research')}")
            
            st.markdown("### What Agent Searched For")
            for i, query in enumerate(metadata['all_searches_made'][:4], 1):
                st.markdown(f"{i}. {query}")
            
            if metadata['contradictions_found'] > 0:
                st.markdown("### Contradictions Discovered")
                st.warning(f"Agent found {metadata['contradictions_found']} contradiction(s):")
                for contradiction in metadata['contradictions_discovered']:
                    st.markdown(f"- {contradiction}")
                
                st.info(f"Agent iterated {metadata['iterations_performed']} time(s) to research deeper")
            
            st.markdown("### Confidence Assessment")
            st.markdown(f"**Overall Confidence:** {metadata['confidence_level']}")
            st.markdown(f"**Source Agreement:** {metadata['source_agreement_score']}%")
    
    # Report content
    st.markdown('<div class="report-container">', unsafe_allow_html=True)
    st.markdown(result['report'])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Export options
    st.divider()
    st.subheader("📥 Export")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button(
            label="📄 Report (Markdown)",
            data=result['report'],
            file_name=f"report_{result['topic'][:20].replace(' ', '_')}.md",
            mime="text/markdown"
        )
    
    with col2:
        st.download_button(
            label="📊 Full Data (JSON)",
            data=json.dumps(result, indent=2),
            file_name=f"report_{result['topic'][:20].replace(' ', '_')}.json",
            mime="application/json"
        )
    
    with col3:
        st.download_button(
            label="🤖 Metadata Only",
            data=json.dumps(metadata, indent=2),
            file_name=f"metadata_{result['topic'][:20].replace(' ', '_')}.json",
            mime="application/json"
        )
    
    # New research button
    st.divider()
    if st.button("🔄 Start New Research", use_container_width=True):
        st.session_state.research_complete = False
        st.session_state.research_result = None
        st.rerun()

# Footer with information
st.divider()
st.markdown("""
---
### How Agentic Research Works

Unlike simple chatbots, this agent:

1. **Plans** - Decides what angles to research based on the topic
2. **Searches** - Executes multiple searches (not predetermined)
3. **Evaluates** - Ranks sources by credibility
4. **Analyzes** - Finds what sources agree and disagree on
5. **Iterates** - Discovers contradictions and researches deeper
6. **Reports** - Creates evidence-based reports showing consensus vs debate

**Each research session is unique** because the agent makes autonomous decisions based on what it discovers.

---
**Built with:** Groq API + Streamlit + Autonomous Agent Architecture

**Model:** Llama 3.3 70B (Free Tier)
""")
