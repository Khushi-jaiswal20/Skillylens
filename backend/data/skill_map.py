SKILL_MAP = {
    "Full Stack Developer": {
        "required": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Express",
                     "MongoDB", "MySQL", "REST API", "Git", "Docker", "TypeScript"],
        "good_to_have": ["Redis", "GraphQL", "AWS", "CI/CD", "Kubernetes"],
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
    }
}

def get_roles():
    return list(SKILL_MAP.keys())

def get_skills_for_role(role):
    return SKILL_MAP.get(role, {})