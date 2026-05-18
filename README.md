# PromptClinic: TikTok Shop IPR Governance & Experience

PromptClinic is an exclusive, highly specialized Prompt Engineering and Debugging tool customized for the **TikTok Shop IPR Governance & Experience** department. 

It is not a simple "prompt rewriter." It is a robust, logic-driven Prompt Linter that diagnoses structural flaws, performs Root Cause Analysis (RCA) on unsatisfactory AI outputs, and reconstructs prompts with professional-grade engineering techniques (such as Chain of Thought, Edge Case Defense, and XML Tagging)—all while strictly preserving the user's original business logic.

---

## 🎯 User Pain Points

- **Vague Prompts**: Users often write prompts that lack context, boundary conditions, or structured output formats, leading to unpredictable AI responses.
- **Hallucinations in Enforcement**: When detecting counterfeits or IP violations, AI models may hallucinate fake brand names or policies if not strictly constrained.
- **Loss of Nuance**: Typical "prompt optimizers" often over-abstract the user's input, deleting crucial business logic or specific parameters in the name of "better structure."
- **Iterative Blindness**: When an AI output fails, users often don't know *why* it failed or *which part* of their prompt caused the issue.

---

## ✨ Core Features

1. **Strict Fidelity (Zero-Loss Optimization)**: The underlying LLM is strictly instructed to retain 100% of your original nouns, parameters, and business logic. It reorganizes your prompt into a robust framework without deleting your soul.
2. **Visual Diff Tracking**: Generates a `<HIGHLIGHTED_PROMPT>` using HTML to visually highlight (in green) exactly what constraints, rules, or structural elements the AI added to your original prompt.
3. **Internal Self-Critique**: Before outputting the final prompt, the AI performs a hidden `<thinking>` simulation to inventory your requirements, simulate the output, and fix loopholes.
4. **Chat-based Iteration**: If the optimized prompt still fails in testing, you can chat with the AI directly in the app to feed it the new error logs and iterate further.

---

## 🛠️ High-Level Optimization Dimensions

When reconstructing your prompt, PromptClinic automatically applies these advanced Prompt Engineering techniques:

- **Chain of Thought (CoT)**: Guides the model to think step-by-step before concluding if an item violates IPR.
- **Edge Case Defense**: Anticipates model hallucinations and sets strict boundaries (e.g., "If the brand is not in the database, you MUST output 'Unknown'").
- **Signal-to-Noise Ratio**: Removes ambiguities and structures instructions cleanly.
- **Parameterization**: Uses bracketed placeholders (e.g., `[Insert Product Title Here]`) for missing dynamic variables instead of fabricating data.

---

## 🚀 How to Run Locally

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/promptclinic.git
cd promptclinic
pip install -r requirements.txt
```

### 3. Configure API Key
Copy the example environment file and add your DeepSeek API Key:

```bash
cp .env.example .env
```
Edit `.env` to include your actual API key:
```ini
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-reasoner
```

### 4. Start the Application
Run the Streamlit app:
```bash
streamlit run app.py
```

---

## ☁️ How to Deploy on Streamlit Community Cloud

1. Push this repository to your GitHub account.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and click **New app**.
3. Select your repository, branch (`main`), and set the main file path to `app.py`.
4. Click **Advanced settings...** and add your environment variables in the **Secrets** section:
   ```toml
   DEEPSEEK_API_KEY="your_api_key_here"
   DEEPSEEK_BASE_URL="https://api.deepseek.com"
   DEEPSEEK_MODEL="deepseek-reasoner"
   ```
5. Click **Deploy!**

---

## 📁 Project Structure

```text
promptclinic/
├── app.py               # Streamlit frontend & chat iteration UI
├── llm_client.py        # DeepSeek API client with error handling
├── prompts.py           # Core system prompts & simulation logic
├── requirements.txt     # Python dependencies
├── .env.example         # Template for environment variables
└── README.md            # Project documentation
```

---

## 🗺️ Future Iterations (Post-MVP)

- **Prompt Version Control**: Save history of iterations to compare which prompt performed better in production.
- **A/B Testing Integration**: Hook up to an evaluation framework to run the old vs. new prompt against a golden dataset of TikTok Shop listings.
- **Team Prompt Library**: A shared repository where IPR investigators can save and reuse the highest-performing prompts.