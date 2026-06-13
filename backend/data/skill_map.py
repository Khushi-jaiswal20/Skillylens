SKILL_MAP = {
    "Full Stack Developer": {
        "required": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Express",
                     "MongoDB", "MySQL", "REST API", "Git", "Docker", "TypeScript"],
        "good_to_have": ["Redis", "GraphQL", "AWS", "CI/CD", "Kubernetes"],
        "suggested_projects": [
        "Build a full-stack e-commerce site with React + Node.js",
        "Create a real-time chat app using Socket.io",
        "Make a REST API with authentication using JWT",
        "Build a expense tracker with MySQL backend",
        "Deploy a portfolio website on AWS/Render", ],
        "ai_tools": {
            "famous": [
                {"name": "GitHub Copilot", "use": "AI pair programmer", "link": "https://copilot.github.com"},
                {"name": "ChatGPT", "use": "Code explanation & debugging", "link": "https://chat.openai.com"},
                {"name": "Vercel v0", "use": "AI UI generation", "link": "https://v0.dev"},
            ],
            "underrated": [
                {"name": "Cursor IDE", "use": "AI-native code editor, better than Copilot for context", "link": "https://cursor.sh"},
                {"name": "Warp Terminal", "use": "AI terminal with command suggestions", "link": "https://warp.dev"},
                {"name": "Pieces.app", "use": "AI snippet manager with context memory", "link": "https://pieces.app"},
                {"name": "Mintlify", "use": "Auto-generates code documentation", "link": "https://mintlify.com"},
            ]
            
        }
    },
    "Data Analyst": {
        "required": ["Python", "SQL", "Excel", "Pandas", "NumPy", "Tableau",
                     "Power BI", "Data Visualization", "Statistics", "EDA"],
        "good_to_have": ["Machine Learning", "Spark", "Airflow", "dbt", "Looker"],
        "suggested_projects": [
        "Sales dashboard in Power BI or Tableau",
        "EDA on Kaggle dataset using Pandas + Matplotlib",
        "Sentiment analysis on Twitter data using Python",
        "SQL-based business insights report from real dataset",
        "Customer churn prediction model with Scikit-learn",
    ],
        "ai_tools": {
            "famous": [
                {"name": "Power BI Copilot", "use": "AI-powered BI reports", "link": "https://powerbi.microsoft.com"},
                {"name": "Tableau AI", "use": "Auto-insights from data", "link": "https://tableau.com"},
            ],
            "underrated": [
                {"name": "Julius AI", "use": "Chat with your CSV/Excel data", "link": "https://julius.ai"},
                {"name": "TPOT", "use": "AutoML pipeline optimizer", "link": "https://epistasislab.github.io/tpot/"},
                {"name": "Rath (Kanaries)", "use": "Autonomous EDA tool", "link": "https://kanaries.net"},
                {"name": "Dify", "use": "Build LLM data apps without backend", "link": "https://dify.ai"},
            ]
        }
    },
    "Machine Learning Engineer": {
        "required": ["Python", "TensorFlow", "PyTorch", "Scikit-learn", "NumPy",
                     "Pandas", "MLflow", "Docker", "REST API", "Git", "SQL"],
        "good_to_have": ["Kubernetes", "Spark", "Hugging Face", "ONNX", "Ray"],
        "suggested_projects": [
        "Image classifier using CNN with PyTorch",
        "Chatbot using LangChain + Groq API",
        "House price prediction with feature engineering",
        "Resume parser using NLP and spaCy",
        "Deploy an ML model as REST API using FastAPI",
    ],
        "ai_tools": {
            "famous": [
                {"name": "Hugging Face", "use": "Model hub & transformers", "link": "https://huggingface.co"},
                {"name": "Weights & Biases", "use": "Experiment tracking", "link": "https://wandb.ai"},
            ],
            "underrated": [
                {"name": "LanceDB", "use": "Serverless vector database for AI apps", "link": "https://lancedb.com"},
                {"name": "Evidently AI", "use": "ML model monitoring & drift detection", "link": "https://evidentlyai.com"},
                {"name": "Marimo", "use": "Reactive Python notebooks (better than Jupyter)", "link": "https://marimo.io"},
                {"name": "Outlines", "use": "Structured text generation from LLMs", "link": "https://github.com/outlines-dev/outlines"},
            ]
        }
    },
    "UI/UX Designer": {
        "required": ["Figma", "Adobe XD", "Wireframing", "Prototyping", "User Research",
                     "Design Systems", "Typography", "Color Theory", "HTML", "CSS"],
        "good_to_have": ["Motion Design", "Framer", "User Testing", "Accessibility", "Blender"],
        "ai_tools": {
            "famous": [
                {"name": "Figma AI", "use": "Auto-layout and design suggestions", "link": "https://figma.com"},
                {"name": "Adobe Firefly", "use": "AI image generation for design", "link": "https://firefly.adobe.com"},
            ],
            "underrated": [
                {"name": "Uizard", "use": "Sketch to Figma wireframe instantly", "link": "https://uizard.io"},
                {"name": "Attention Insight", "use": "AI predicts where users look on your design", "link": "https://attentioninsight.com"},
                {"name": "Relume", "use": "AI sitemap & wireframe generator", "link": "https://relume.io"},
                {"name": "Framer AI", "use": "Full website from text prompt", "link": "https://framer.com"},
            ]
        }
    },
    "DevOps Engineer": {
        "required": ["Linux", "Docker", "Kubernetes", "CI/CD", "Jenkins", "AWS",
                     "Terraform", "Git", "Bash", "Nginx", "Monitoring"],
        "good_to_have": ["Ansible", "Helm", "Prometheus", "Grafana", "ArgoCD"],
        "ai_tools": {
            "famous": [
                {"name": "GitHub Actions", "use": "Automated CI/CD pipelines", "link": "https://github.com/features/actions"},
                {"name": "AWS CodeWhisperer", "use": "AI for cloud infra code", "link": "https://aws.amazon.com/codewhisperer"},
            ],
            "underrated": [
                {"name": "k9s", "use": "Terminal UI to manage Kubernetes clusters", "link": "https://k9scli.io"},
                {"name": "Runme", "use": "Run runbooks & docs as code", "link": "https://runme.dev"},
                {"name": "Infracost", "use": "AI cost estimation for Terraform", "link": "https://infracost.io"},
                {"name": "Spacelift", "use": "Intelligent IaC management", "link": "https://spacelift.io"},
            ]
        }
    },
    "Cybersecurity Analyst": {
        "required": ["Networking", "Linux", "Python", "Ethical Hacking", "SIEM",
                     "Wireshark", "Metasploit", "OWASP", "Cryptography", "Firewalls"],
        "good_to_have": ["Cloud Security", "Reverse Engineering", "Malware Analysis", "CEH", "CISSP"],
        "ai_tools": {
            "famous": [
                {"name": "CrowdStrike Falcon", "use": "AI-powered threat detection", "link": "https://crowdstrike.com"},
            ],
            "underrated": [
                {"name": "Nuclei", "use": "Fast, template-based vulnerability scanner", "link": "https://nuclei.projectdiscovery.io"},
                {"name": "Pentest-GPT", "use": "AI-guided penetration testing", "link": "https://github.com/GreyDGL/PentestGPT"},
                {"name": "Semgrep", "use": "Static analysis to catch code vulnerabilities", "link": "https://semgrep.dev"},
                {"name": "Shuffle", "use": "Open-source SOAR platform", "link": "https://shuffler.io"},
            ]
        }
    },
    "Backend Developer": {
        "required": ["Python/Java/Node.js", "REST API", "SQL", "NoSQL", "Docker",
                     "Git", "Authentication", "Caching", "Microservices", "Message Queues"],
        "good_to_have": ["gRPC", "GraphQL", "Redis", "Kafka", "AWS Lambda"],
        "ai_tools": {
            "famous": [
                {"name": "GitHub Copilot", "use": "Code completion", "link": "https://copilot.github.com"},
                {"name": "Postman AI", "use": "Auto-generate API tests", "link": "https://postman.com"},
            ],
            "underrated": [
                {"name": "HTTPie AI", "use": "Smart API client with AI suggestions", "link": "https://httpie.io"},
                {"name": "Hoppscotch", "use": "Lightweight open-source Postman alternative", "link": "https://hoppscotch.io"},
                {"name": "Zuplo", "use": "AI-powered API gateway", "link": "https://zuplo.com"},
                {"name": "Scalar", "use": "Beautiful API docs from OpenAPI spec", "link": "https://scalar.com"},
            ]
        }
    },
    "Android Developer": {
        "required": ["Kotlin", "Java", "Android SDK", "Jetpack Compose", "XML Layouts",
                     "REST API", "SQLite/Room", "Git", "Firebase", "Material Design"],
        "good_to_have": ["Kotlin Coroutines", "MVVM", "Hilt/Dagger", "CI/CD", "Flutter"],
        "ai_tools": {
            "famous": [
                {"name": "Android Studio AI", "use": "Gemini integrated code assistant", "link": "https://developer.android.com"},
                {"name": "Firebase Genkit", "use": "AI flows for mobile apps", "link": "https://firebase.google.com/products/genkit"},
            ],
            "underrated": [
                {"name": "Appmap", "use": "AI runtime code analysis", "link": "https://appmap.io"},
                {"name": "Codeium", "use": "Free AI autocomplete for Android dev", "link": "https://codeium.com"},
                {"name": "Maestro", "use": "Simplest mobile UI testing framework", "link": "https://maestro.mobile.dev"},
                {"name": "Emerald (Gradle Doctor)", "use": "Optimize slow Android builds with AI tips", "link": "https://github.com/runningcode/gradle-doctor"},
            ]
        }
    },
    "Cloud Engineer": {
        "required": ["AWS", "Azure", "GCP", "Terraform", "Docker", "Kubernetes",
                     "Linux", "Networking", "IAM", "S3", "EC2", "CI/CD"],
        "good_to_have": ["Helm", "Serverless", "CDN", "Cost Optimization", "Multi-cloud"],
        "ai_tools": {
            "famous": [
                {"name": "AWS CodeWhisperer", "use": "AI for cloud infra code", "link": "https://aws.amazon.com/codewhisperer"},
            ],
            "underrated": [
                {"name": "Infracost", "use": "AI cost estimation for Terraform", "link": "https://infracost.io"},
                {"name": "Cloudquery", "use": "Cloud asset inventory as SQL", "link": "https://cloudquery.io"},
                {"name": "Steampipe", "use": "Query cloud APIs with SQL", "link": "https://steampipe.io"},
            ]
        }
    },
    "Blockchain Developer": {
        "required": ["Solidity", "Ethereum", "Web3.js", "Smart Contracts", "JavaScript",
                     "Python", "Cryptography", "Git", "Hardhat", "IPFS"],
        "good_to_have": ["Rust", "Polkadot", "DeFi", "NFT Standards", "Layer 2"],
        "ai_tools": {
            "famous": [
                {"name": "ChatGPT", "use": "Solidity code review & audit", "link": "https://chat.openai.com"},
            ],
            "underrated": [
                {"name": "Mythril", "use": "AI smart contract vulnerability scanner", "link": "https://github.com/ConsenSys/mythril"},
                {"name": "Tenderly", "use": "Smart contract debugging & simulation", "link": "https://tenderly.co"},
                {"name": "Slither", "use": "Static analysis for Solidity", "link": "https://github.com/crytic/slither"},
            ]
        }
    },
    "Game Developer": {
        "required": ["Unity", "C#", "Unreal Engine", "C++", "3D Math", "Physics",
                     "Git", "Game Design", "Animation", "UI/UX"],
        "good_to_have": ["Blender", "Shader Programming", "Multiplayer Networking", "AR/VR", "Mobile Gaming"],
        "ai_tools": {
            "famous": [
                {"name": "Unity Muse", "use": "AI textures, animation & code in Unity", "link": "https://unity.com/products/muse"},
            ],
            "underrated": [
                {"name": "Scenario.gg", "use": "AI game asset generator", "link": "https://scenario.gg"},
                {"name": "Inworld AI", "use": "AI-powered NPC characters", "link": "https://inworld.ai"},
                {"name": "Promethean AI", "use": "AI world-building assistant", "link": "https://prometheanai.com"},
            ]
        }
    },
    "Embedded Systems Engineer": {
        "required": ["C", "C++", "Microcontrollers", "Arduino", "Raspberry Pi",
                     "RTOS", "UART/SPI/I2C", "PCB Design", "Assembly", "Linux"],
        "good_to_have": ["FreeRTOS", "Zephyr", "IoT Protocols", "FPGA", "Power Management"],
        "ai_tools": {
            "famous": [
                {"name": "GitHub Copilot", "use": "C/C++ embedded code completion", "link": "https://copilot.github.com"},
            ],
            "underrated": [
                {"name": "Wokwi", "use": "AI-powered online embedded simulator", "link": "https://wokwi.com"},
                {"name": "PlatformIO AI", "use": "Embedded dev environment with AI", "link": "https://platformio.org"},
                {"name": "Renode", "use": "Full system simulation for embedded", "link": "https://renode.io"},
            ]
        }
    },
    "Product Manager": {
        "required": ["Product Roadmap", "Agile", "Scrum", "User Research", "SQL",
                     "Data Analysis", "Wireframing", "Stakeholder Management", "A/B Testing", "PRD Writing"],
        "good_to_have": ["Python", "Figma", "OKRs", "Growth Metrics", "Competitive Analysis"],
        "ai_tools": {
            "famous": [
                {"name": "Notion AI", "use": "PRD and roadmap writing", "link": "https://notion.so"},
                {"name": "Jira AI", "use": "Sprint planning & ticket management", "link": "https://atlassian.com/jira"},
            ],
            "underrated": [
                {"name": "Productboard AI", "use": "AI feature prioritization", "link": "https://productboard.com"},
                {"name": "Sprig", "use": "AI user research & session replay", "link": "https://sprig.com"},
                {"name": "Kraftful", "use": "AI product coach for PMs", "link": "https://kraftful.com"},
            ]
        }
    },
    "QA Engineer": {
        "required": ["Selenium", "Python/Java", "Manual Testing", "Test Cases", "API Testing",
                     "Postman", "SQL", "Git", "Bug Reporting", "Agile"],
        "good_to_have": ["Cypress", "JMeter", "Performance Testing", "CI/CD", "Mobile Testing"],
        "ai_tools": {
            "famous": [
                {"name": "Postman AI", "use": "Auto-generate API tests", "link": "https://postman.com"},
            ],
            "underrated": [
                {"name": "Testim", "use": "AI-powered test automation", "link": "https://testim.io"},
                {"name": "Applitools", "use": "AI visual testing", "link": "https://applitools.com"},
                {"name": "Mabl", "use": "Intelligent test automation platform", "link": "https://mabl.com"},
                {"name": "Checkly", "use": "Monitoring-as-code with AI", "link": "https://checklyhq.com"},
            ]
        }
    },
    "Data Engineer": {
        "required": ["Python", "SQL", "Apache Spark", "Kafka", "Airflow", "dbt",
                     "AWS/GCP", "ETL Pipelines", "Data Warehousing", "Docker"],
        "good_to_have": ["Snowflake", "Databricks", "Flink", "Delta Lake", "Terraform"],
        "ai_tools": {
            "famous": [
                {"name": "Databricks AI", "use": "Lakehouse with built-in AI", "link": "https://databricks.com"},
            ],
            "underrated": [
                {"name": "Mage AI", "use": "Modern data pipeline builder with AI", "link": "https://mage.ai"},
                {"name": "dbt Copilot", "use": "AI SQL transformations in dbt", "link": "https://getdbt.com"},
                {"name": "Soda", "use": "AI-powered data quality monitoring", "link": "https://soda.io"},
                {"name": "Datahub", "use": "Open-source data catalog with lineage", "link": "https://datahubproject.io"},
            ]
        }
    },
    "iOS Developer": {
        "required": ["Swift", "SwiftUI", "Xcode", "UIKit", "REST API", "Core Data",
                     "Git", "Firebase", "App Store Guidelines", "Auto Layout"],
        "good_to_have": ["Combine", "RxSwift", "ARKit", "CoreML", "WidgetKit"],
        "ai_tools": {
            "famous": [
                {"name": "Xcode AI", "use": "Apple Intelligence code completion", "link": "https://developer.apple.com"},
            ],
            "underrated": [
                {"name": "Codeium", "use": "Free AI autocomplete for Swift", "link": "https://codeium.com"},
                {"name": "RocketSim", "use": "Enhanced iOS simulator with AI testing", "link": "https://rocketsim.app"},
                {"name": "Emerge Tools", "use": "AI app size & performance optimization", "link": "https://emergetools.com"},
            ]
        }
    },
    "Technical Writer": {
        "required": ["Documentation", "Markdown", "API Docs", "Git", "HTML",
                     "Research", "Content Strategy", "Editing", "DITA/XML", "User Guides"],
        "good_to_have": ["Swagger/OpenAPI", "Confluence", "Docusaurus", "Video Tutorials", "Localization"],
        "ai_tools": {
            "famous": [
                {"name": "Grammarly AI", "use": "Writing clarity & tone improvement", "link": "https://grammarly.com"},
                {"name": "Notion AI", "use": "Documentation drafting", "link": "https://notion.so"},
            ],
            "underrated": [
                {"name": "Mintlify", "use": "Auto-generate docs from code", "link": "https://mintlify.com"},
                {"name": "Swimm", "use": "AI docs that stay in sync with code", "link": "https://swimm.io"},
                {"name": "Archbee", "use": "AI knowledge base builder", "link": "https://archbee.com"},
            ]
        }
    },
    "AR/VR Developer": {
        "required": ["Unity", "C#", "Unreal Engine", "3D Modeling", "WebXR",
                     "Spatial Computing", "OpenXR", "Git", "UX for XR", "Shader Programming"],
        "good_to_have": ["Blender", "ARKit", "ARCore", "Meta SDK", "Hand Tracking"],
        "ai_tools": {
            "famous": [
                {"name": "Meta AI SDK", "use": "AI for Quest spatial experiences", "link": "https://developer.meta.com"},
            ],
            "underrated": [
                {"name": "Needle Tools", "use": "Web-based XR with AI components", "link": "https://needle.tools"},
                {"name": "Meshy AI", "use": "Text to 3D model generation", "link": "https://meshy.ai"},
                {"name": "Luma AI", "use": "Real-world to 3D NeRF capture", "link": "https://lumalabs.ai"},
            ]
        }
    },
    "Prompt Engineer": {
        "required": ["LLM Fundamentals", "Python", "API Integration", "Chain-of-Thought",
                     "RAG", "Vector Databases", "LangChain", "Evaluation Metrics", "NLP Basics", "Git"],
        "good_to_have": ["Fine-tuning", "LlamaIndex", "Hugging Face", "MLflow", "Semantic Search"],
        "ai_tools": {
            "famous": [
                {"name": "LangChain", "use": "LLM app framework", "link": "https://langchain.com"},
                {"name": "OpenAI Playground", "use": "Prompt testing & iteration", "link": "https://platform.openai.com"},
            ],
            "underrated": [
                {"name": "PromptLayer", "use": "Prompt version control & analytics", "link": "https://promptlayer.com"},
                {"name": "Braintrust", "use": "AI eval & prompt management", "link": "https://braintrustdata.com"},
                {"name": "Agenta", "use": "Open-source LLMOps platform", "link": "https://agenta.ai"},
                {"name": "Langfuse", "use": "LLM observability & tracing", "link": "https://langfuse.com"},
            ]
        }
    },
    "Digital Marketing Analyst": {
        "required": ["Google Analytics", "SEO", "SEM", "Meta Ads", "Excel",
                     "Content Strategy", "Email Marketing", "CRM", "A/B Testing", "SQL"],
        "good_to_have": ["Python", "Tableau", "HubSpot", "Copywriting", "Video Marketing"],
        "ai_tools": {
            "famous": [
                {"name": "HubSpot AI", "use": "AI marketing automation", "link": "https://hubspot.com"},
                {"name": "Jasper AI", "use": "AI marketing content generation", "link": "https://jasper.ai"},
            ],
            "underrated": [
                {"name": "Surfer SEO", "use": "AI content optimization for ranking", "link": "https://surferseo.com"},
                {"name": "Mutiny", "use": "AI website personalization", "link": "https://mutinyhq.com"},
                {"name": "Pencil", "use": "AI ad creative generation", "link": "https://trypencil.com"},
            ]
        }
    },
    "Network Engineer": {
        "required": ["TCP/IP", "Routing & Switching", "Cisco IOS", "Firewalls", "VPN",
                     "Linux", "Wireshark", "DNS/DHCP", "BGP/OSPF", "Network Security"],
        "good_to_have": ["SD-WAN", "Network Automation", "Python", "Ansible", "Cloud Networking"],
        "ai_tools": {
            "famous": [
                {"name": "Cisco AI Network Analytics", "use": "AI network monitoring", "link": "https://cisco.com"},
            ],
            "underrated": [
                {"name": "NetBrain", "use": "AI network automation & troubleshooting", "link": "https://netbraintech.com"},
                {"name": "Batfish", "use": "Network config analysis & verification", "link": "https://batfish.org"},
                {"name": "Forward Networks", "use": "AI network digital twin", "link": "https://forwardnetworks.com"},
            ]
        }
    }
}

def get_roles():
    return list(SKILL_MAP.keys())

def get_skills_for_role(role):
    return SKILL_MAP.get(role, {})