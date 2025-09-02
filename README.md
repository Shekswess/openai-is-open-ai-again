# OpenAI is Open AI Again 📢

This repository contains the code examples shown in the [GDG event "OpenAI is Open AI Again"](https://www.linkedin.com/feed/update/urn:li:activity:7364598475147112472/) held on September 02, 2025 in [Base42](https://base42.mk/)

## Useful Links ✨

- [Open models by OpenAI](https://openai.com/open-models/)
- [Introducing gpt-oss - Model Card](https://openai.com/index/introducing-gpt-oss/)
- [OpenAI Harmony Response Format](https://cookbook.openai.com/articles/openai-harmony)
- [gpt-oss: How to Run & Fine-tune - Tutorial](https://docs.unsloth.ai/basics/gpt-oss-how-to-run-and-fine-tune)
- [gpt-oss playground](https://gpt-oss.com/)

## Agent Examples 🚀

This repository includes two different agent implementations using OpenAI's `gpt-oss-120b` model from Cerebras via Hugging Face:

### Agent with OpenAI SDK (`agent_openai_sdk`)

The `agent_openai_sdk/main.py` demonstrates how to create a simple agent using the Agents SDK. The agent is capable of performing tasks such as calculating sums and retrieving the current time, utilizing function tools for enhanced functionality.

### Agent with Google ADK (`agent_google_adk`)

The `agent_google_adk/main.py` shows how to implement the same functionality using Google's Agents Development Kit (ADK). This implementation provides an alternative approach to building agents with similar capabilities.

### How to Run

1. Clone the repository

```bash
git clone https://github.com/Shekswess/openai-is-open-ai-again.git
```

2. Install uv package manager

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Navigate to either agent directory

```bash
# For OpenAI SDK implementation
cd openai-is-open-ai-again/agent_openai_sdk

# OR for Google ADK implementation  
cd openai-is-open-ai-again/agent_google_adk
```

4. Set up your environment variables (create a `.env` file with your HuggingFace token)

5. Run the agent

```bash
uv run main.py
```

## Fine-tuning Example 🎯

The `finetuning/gpt_oss_20b_fine_tuning_unsloth.ipynb` notebook provides a comprehensive guide to fine-tuning the `gpt-oss-20b` model using the Unsloth library. It covers:

- Data preparation using the `HuggingFaceH4/Multilingual-Thinking` dataset.
- Training with LoRA adapters for parameter-efficient fine-tuning.
- Inference and reasoning effort customization (low, medium, high).
- Saving and loading fine-tuned models.

### How to Run

1. Open the notebook in Google Colab.
2. Follow the step-by-step instructions to fine-tune the model.
3. Save the fine-tuned model for future use.

## Local Inference Example 🖥

The `local_inference/run_gpt_oss_20b_on_colab.ipynb` notebook demonstrates how to run the `gpt-oss-20b` model in a resource-constrained environment like Google Colab. It includes:

- Setting up the environment with the latest PyTorch and CUDA.
- Loading the model from Hugging Face.
- Customizing reasoning effort for chat-based tasks.

### How to Run

1. Open the notebook in Google Colab.
2. Install the required dependencies.
3. Load the model and run inference with custom prompts.

## Presentation 📊

The `presentation/gpt-oss.pdf` contains the slides from the GDG event "OpenAI is Open AI Again" held on September 02, 2025, providing an overview of the topics covered and the examples demonstrated.

## Repository Structure 🗂

```
.
├── agent_google_adk/
│   ├── .python-version
│   ├── main.py
│   ├── pyproject.toml
│   └── uv.lock
├── agent_openai_sdk/
│   ├── .python-version
│   ├── main.py
│   ├── pyproject.toml
│   └── uv.lock
├── finetuning/
│   └── gpt_oss_20b_fine_tuning_unsloth.ipynb
├── local_inference/
│   └── run_gpt_oss_20b_on_colab.ipynb
├── presentation/
│   └── gpt-oss.pdf
├── LICENSE
└── README.md
```

## License 📜

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for details.
