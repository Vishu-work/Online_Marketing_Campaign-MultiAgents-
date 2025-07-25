import os
from crewai import Agent, Task, Crew, LLM
from crewai_tools import ScrapeWebsiteTool
from dataclasses import dataclass
from typing import Dict, List
import pickle



os.environ["COHERE_API_KEY"] = "YOUR_API_KEY"
os.environ["COHERE_MODEL_NAME"] = "command"

llm = LLM(
    provider="cohere",
    model="command",
    config={
        "api_key": os.getenv("YPUR_API_KEY")
    }
)


campaign_creator_agent = Agent(
    role="Marketing Campaign Specialist",
    goal="Create a personalized marketing campaign for a given product, including strategy, content, and distribution channels.",
    backstory=(
        "You are a seasoned marketing expert at crewAI (https://crewai.com), working on a request from DeepLearningAI. "
        "Your task is to craft a tailored marketing campaign for a product specified by Andrew Ng. "
        "You use your expertise to develop strategies, create engaging content, and select optimal channels."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

campaign_reviewer_agent = Agent(
    role="Marketing Quality Assurance Specialist",
    goal="Ensure the marketing campaign is comprehensive, accurate, and optimized for the target audience.",
    backstory=(
        "You are a meticulous quality assurance expert at crewAI (https://crewai.com), ensuring that campaigns for DeepLearningAI "
        "meet the highest standards. You review the campaign for completeness, relevance, and engagement, "
        "providing feedback to refine it before delivery to Andrew Ng."
    ),
    verbose=True,
    llm=llm
)

marketing_trends_tool = ScrapeWebsiteTool(
    website_url="https://www.marketingweek.com/"
)

create_campaign_task = Task(
    description=(
        "DeepLearningAI, represented by Andrew Ng, has requested a personalized marketing campaign for their product: {product_name}. "
        "Create a campaign that includes:\n"
        "- A marketing strategy tailored to the product category (e.g., electronics, clothing, education).\n"
        "- Content for social media, email, and ad copy, incorporating the product name and strategy.\n"
        "- A selection of distribution channels best suited for the product.\n"
        "Use your expertise and, if needed, external resources to ensure the campaign is innovative and effective."
    ),
    expected_output=(
        "A detailed marketing campaign including:\n"
        "- A clear marketing strategy.\n"
        "- Content for social media, email, and ad copy.\n"
        "- A list of recommended distribution channels.\n"
        "The campaign should be tailored to the product and maintain a professional yet engaging tone."
    ),
    tools=[marketing_trends_tool],
    agent=campaign_creator_agent
)

review_campaign_task = Task(
    description=(
        "Review the marketing campaign created for product: {product_name}. "
        "Ensure the campaign is comprehensive, accurate, and tailored to the product’s target audience. "
        "Verify that:\n"
        "- The strategy aligns with the product category.\n"
        "- The content is engaging, clear, and consistent across platforms.\n"
        "- The distribution channels are optimal for reaching the target audience.\n"
        "Provide feedback and refine the campaign to meet high-quality standards."
    ),
    expected_output=(
        "A finalized marketing campaign ready to be sent to DeepLearningAI, including:\n"
        "- A refined marketing strategy.\n"
        "- Polished content for social media, email, and ad copy.\n"
        "- An optimized list of distribution channels.\n"
        "The response should be professional, friendly, and leave no questions unanswered."
    ),
    agent=campaign_reviewer_agent
)

crew = Crew(
    agents=[campaign_creator_agent, campaign_reviewer_agent],
    tasks=[create_campaign_task, review_campaign_task],
    cache=True,
    verbose=True,
    memory=False,
    llm=llm,
    embedder={
        "provider": "cohere",
        "config": {"model": "embed-english-v3.0"}
    }
)

product_name = input("Enter the product name for the campaign: ")

inputs = {
    "product_name": product_name
}

result = crew.kickoff(inputs=inputs)

print("\n🎯 Final Marketing Campaign:\n")
print(result)

with open("generated_campaign.txt", "w", encoding="utf-8") as f:
    f.write(str(result))

print("\n✅ Campaign saved as 'generated_campaign.txt'")
