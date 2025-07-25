# 🎯 Agentic GenAI Marketing Campaign Generator

> Generate, Review, and Refine Personalized Marketing Campaigns with Autonomous Agents using **CrewAI** and **Cohere LLMs**

![GenAI Badge](https://img.shields.io/badge/Powered_by-GenerativeAI-blueviolet)
![Cohere Badge](https://img.shields.io/badge/LLM-Cohere_command-blue)
![Agentic Badge](https://img.shields.io/badge/Agentic_Architecture-CrewAI-ff69b4)

---

## 🧠 Overview

This project builds an intelligent **multi-agent system** using [CrewAI](https://crewai.com) and [Cohere](https://cohere.com) to automatically create and review **tailored marketing campaigns**.

- 💡 Powered by **Generative AI** (`command` LLM from Cohere)
- 🤖 Uses two expert **Agents**:
  - **Marketing Campaign Creator**
  - **Marketing QA Reviewer**
- 🌐 Pulls **real-time insights** from [MarketingWeek.com](https://www.marketingweek.com/)
- 📄 Outputs a **ready-to-send campaign** for any product

---

## 🚀 Features

✅ Multi-step agentic reasoning  
✅ Web scraping tool integration  
✅ Custom product-based input  
✅ Generated content includes:
- 📊 Strategy
- 📧 Emails
- 📢 Ad Copy
- 📱 Social Posts
- 🛠 Distribution Channels

---

## 🧩 Architecture

```mermaid
flowchart LR
    Start([📥 Product Name Input])
    Start --> A[🧠 Marketing Campaign Specialist (Agent 1)]
    A --> B[📑 Campaign Strategy & Content Generation]
    B --> C[🔍 Marketing QA Specialist (Agent 2)]
    C --> D[✅ Final Review & Refinement]
    D --> End([📤 Output Campaign File])

    subgraph LLM [Cohere LLM]
        A
        C
    end
