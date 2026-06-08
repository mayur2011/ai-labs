# ai-labs

A professional collection of Proof of Concepts (PoCs), prototypes, and architectural patterns leveraging Artificial Intelligence, Large Language Models (LLMs), Generative AI, and Foundation Models. 

This repository acts as a polyglot testing ground, implementing AI capabilities across multiple programming languages to evaluate performance, SDK ecosystems, and integration patterns.

---

## 🛠️ Repository Structure

To maintain clean dependencies and avoid build conflicts, this repository is strictly organized by programming language at the root level.

```text
ai-labs/
├── go/                  # Go (Golang) implementations
│   ├── .golangci.yml
│   └── go.mod
├── java/                # Java implementations
│   └── pom.xml / build.gradle
├── javascript/          # Node.js / JavaScript implementations
│   └── package.json
├── perl/                # Perl 5 legacy/modern integrations
│   └── cpanfile
├── python/              # Python implementations
│   └── requirements.txt
└── README.md
```

---

## 🚀 Core Focus Areas

The PoCs within this repository explore the following domains:
*   **Foundation Model Orchestration:** Interfacing with frontier models via native SDKs and APIs.
*   **RAG (Retrieval-Augmented Generation):** Vector database integrations and semantic search pipelines.
*   **Agentic Workflows:** Autonomous tool-use and multi-agent reasoning chains.
*   **Prompt Engineering:** Programmatic prompt optimization and structured data extraction.

---

## 💻 Language & Stack Overview

### 🐍 Python (`/python`)
*   **Primary Focus:** Heavy data processing, rapid prototyping, and framework evaluation.
*   **Key Tech:** LangChain, LlamaIndex, OpenAI/Anthropic SDKs, Hugging Face.

### 🦫 Go (`/go`)
*   **Primary Focus:** High-performance concurrent services and lightweight deployments.
*   **Key Tech:** LangChainGo, official cloud provider SDKs.

### ⬢ JavaScript / Node.js (`/javascript`)
*   **Primary Focus:** Full-stack integrations, edge functions, and real-time streaming interfaces.
*   **Key Tech:** LangChain.js, Vercel AI SDK.

### ☕ Java (`/java`)
*   **Primary Focus:** Enterprise integration patterns, strict typing architectures, and robust pipelines.
*   **Key Tech:** LangChain4j.

### 🐪 Perl 5 (`/perl`)
*   **Primary Focus:** Text processing, legacy integrations, and lightweight API clients.
*   **Key Tech:** REST::Client, JSON::MaybeXS, custom model wrappers.

---

## ⚙️ Prerequisites & Setup

Each language directory contains its own localized setup instructions. However, all projects generally require:

1.  **API Credentials:** Set up your environment variables in a root or localized `.env` file.
    ```bash
    OPENAI_API_KEY="your_key_here"
    ANTHROPIC_API_KEY="your_key_here"
    ```
2.  **Language Runtimes:** Ensure you have the appropriate runtimes installed (e.g., Python 3.10+, Node 18+, Go 1.20+, JDK 17+, Perl 5.30+).

Please navigate to the specific language subdirectory for detailed installation and execution commands.

---

## 📄 License

This repository is available under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code patterns demonstrated here.

