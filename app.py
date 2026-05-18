import re
import streamlit as st

from llm_client import LLMClient
from prompts import build_prompt_diagnosis_prompt, SYSTEM_PROMPT

EXAMPLE_DATA = {
    "raw_prompt": "Check if this product listing violates any IP rules.",
    "error_info": "The AI just outputs 'Yes' or 'No'. It doesn't tell me which specific rule is violated (Trademark, Copyright, Counterfeit), and it often hallucinates fake brand names that aren't even in the image or description.",
    "expected_result": "I need the AI to output a JSON containing 'is_violation' (boolean), 'violation_type' (string), 'confidence_score' (0-100), and 'reasoning' (step-by-step explanation citing specific text or image elements from the listing). It must strictly say 'Unknown' if the brand is not in our database."
}

def init_session_state() -> None:
    """Initialize widget state before rendering Streamlit widgets."""
    defaults = {
        "raw_prompt": "",
        "error_info": "",
        "expected_result": "",
        "messages": [],
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)

def reset_chat() -> None:
    st.session_state.messages = []

def clean_output(text: str) -> str:
    """Remove <thinking> tags and their content before rendering."""
    cleaned = re.sub(r'<thinking>.*?</thinking>', '', text, flags=re.DOTALL)
    return cleaned.strip()

def render_chat_message(content: str) -> None:
    """Clean the LLM output and render the final highlighted prompt directly."""
    cleaned = re.sub(r'<thinking>.*?</thinking>', '', content, flags=re.DOTALL)
    
    prompt_match = re.search(r'<FINAL_PROMPT>(.*?)</FINAL_PROMPT>', cleaned, flags=re.DOTALL)
    
    if prompt_match:
        final_prompt_html = prompt_match.group(1).strip()
        
        # 1. First, strip HTML tags to get the pure text version for the copy button
        pure_text_prompt = re.sub(r'<[^>]+>', '', final_prompt_html).strip()
        
        st.subheader("✨ Optimized Final Prompt (Visual Diff)")
        # 2. Render the highlighted prompt using HTML directly so users can see what changed
        st.markdown(final_prompt_html, unsafe_allow_html=True)
        
        st.subheader("📋 Copyable Version")
        # 3. Use st.code to provide the native copy button with pure text
        st.code(pure_text_prompt, language="markdown")
    else:
        st.markdown(cleaned.strip())

def fill_example() -> None:
    """Fill all input widgets with the built-in example."""
    for key, value in EXAMPLE_DATA.items():
        st.session_state[key] = value

def main() -> None:
    st.set_page_config(
        page_title="PromptClinic: TikTok Shop IPR",
        page_icon="🛡️",
        layout="wide",
    )
    init_session_state()

    st.title("PromptClinic: TikTok Shop IPR Governance & Experience")

    if not st.session_state.messages:
        st.caption(
            "Exclusive Prompt Engineering Tool for the TikTok Shop IPR Governance & Experience Department."
        )
        st.info(
            "Provide your original prompt, the unsatisfactory output, and your expected result. "
            "The system will diagnose structural flaws, analyze root causes, and generate a highly robust prompt."
        )

        st.text_area(
            "Original Prompt (Required)",
            key="raw_prompt",
            height=100,
            placeholder="e.g., Check if this product listing violates any IP rules.",
        )

        st.text_area(
            "Unsatisfactory Output / Error (Required)",
            key="error_info",
            height=100,
            placeholder="e.g., The AI just outputs 'Yes' or 'No' without providing specific violation types or citing evidence.",
        )

        st.text_area(
            "Expected Result (Required)",
            key="expected_result",
            height=100,
            placeholder="e.g., Output a JSON with 'is_violation', 'violation_type', and 'reasoning'.",
        )

        action_col1, action_col2 = st.columns([1, 1])
        with action_col1:
            st.button("Load Example", on_click=fill_example)
        with action_col2:
            start_diagnosis = st.button("Start Diagnosis", type="primary")

        if start_diagnosis:
            raw_prompt = st.session_state.raw_prompt.strip()
            error_info = st.session_state.error_info.strip()
            expected_result = st.session_state.expected_result.strip()

            if not raw_prompt or not error_info or not expected_result:
                st.warning("Please fill in all three required fields (Original Prompt, Error Info, Expected Result) to proceed.")
                return

            diagnosis_prompt = build_prompt_diagnosis_prompt(
                raw_prompt=raw_prompt,
                error_info=error_info,
                expected_result=expected_result,
            )

            st.session_state.messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": diagnosis_prompt, "display": "Diagnosis request submitted."}
            ]

            with st.spinner("Analyzing prompt structure and simulating output..."):
                client = LLMClient()
                reply = client.chat_with_history(st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            st.rerun()

    else:
        col1, col2 = st.columns([8, 2])
        with col1:
            st.caption("💡 Diagnosis complete. If you encounter new issues after testing the optimized prompt, provide feedback below for further iteration.")
        with col2:
            st.button("🔄 Reset / New Diagnosis", on_click=reset_chat, use_container_width=True)
            
        st.divider()

        for msg in st.session_state.messages:
            if msg["role"] == "system":
                continue
            
            with st.chat_message(msg["role"]):
                if msg["role"] == "user":
                    st.markdown(msg.get("display", msg["content"]))
                else:
                    render_chat_message(msg["content"])
        
        if user_input := st.chat_input("Test failed? Provide new errors or feedback for further optimization..."):
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            with st.chat_message("user"):
                st.markdown(user_input)
            
            with st.chat_message("assistant"):
                with st.spinner("Iterating and optimizing based on feedback..."):
                    client = LLMClient()
                    reply = client.chat_with_history(st.session_state.messages)
                    render_chat_message(reply)
            
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.rerun()

if __name__ == "__main__":
    main()