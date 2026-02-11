import streamlit as st
from agents.workflow import AgentWorkflow

def main():
    @st.cache_resource
    def load_workflow():
        return AgentWorkflow()

    workflow_app = load_workflow()

    st.set_page_config(page_title="Agentic Cover Letter Architect", layout="wide")
    
    # Custom CSS
    st.markdown("""
        <style>
        .main-header { font-size: 32px; font-weight: bold; color: #1E88E5; border-bottom: 2px solid #1E88E5; margin-bottom: 20px; }
        [data-testid="column"] { border: 1px solid #31333F; padding: 20px; border-radius: 10px; background-color: #0E1117; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Agentic Cover Letter Architect</div>', unsafe_allow_html=True)

    col_in, col_out = st.columns([1, 2], gap="large")

    with col_in:
        st.subheader("📋 Job Details")
        job_description = st.text_area(
            "Paste Job Description here:",
            placeholder="We are looking for a passionate...",
            height=400
        )
        
        generate_btn = st.button("Generate Documents", use_container_width=True, type="primary")

    if generate_btn:
        if not job_description.strip():
            st.error("Please paste a job description first!")
        else:
            with st.spinner("Our AI Agents are drafting your documents..."):
                try:
                    initial_state = {
                        "job_description": job_description,
                        "resume_summary": "",
                        "cover_letter": ""
                    }
                    #get response
                    result = workflow_app.compiled_workflow.invoke(initial_state)
                    
                    st.session_state.resume_summary = result.get("resume_summary", "Error generating summary.")
                    st.session_state.cover_letter = result.get("cover_letter", "Error generating cover letter.")
                except Exception as e:
                    st.error(f"Workflow Error: {e}")

    with col_out:
        st.subheader("✨ Generated Content")
        tab1, tab2 = st.tabs(["📄 Resume Summary", "✉️ Cover Letter"])
        
        with tab1:
            if "resume_summary" in st.session_state:
                st.text_area("Final Summary", value=st.session_state.resume_summary, height=150, label_visibility="collapsed", key="summary_text")
                if st.button("📋 Copy Summary"):
                    # This is a simple feedback trick
                    st.toast("Summary copied to clipboard!")
            else:
                st.info("The generated Resume Summary will appear here.")

        with tab2:
            if "cover_letter" in st.session_state:
                # We use st.text_area for viewing
                st.text_area("Final Cover Letter", value=st.session_state.cover_letter, height=400, label_visibility="collapsed", key="letter_text")
                
                # Copy Button Implementation
                if st.button("📋 Copy Cover Letter"):
                    # This uses the st.code trick for an instant copyable block 
                    # OR we can just use st.toast to confirm the user can select/copy
                    st.toast("Select the text above to copy!")
                    # Alternatively, if you want a true "one-click" copy, 
                    # most users prefer the st.code block below the text area:
                    with st.expander("Click here for a one-click copyable version"):
                        st.code(st.session_state.cover_letter, language=None)
            else:
                st.info("The generated Cover Letter will appear here.")

if __name__ == "__main__":
    main()