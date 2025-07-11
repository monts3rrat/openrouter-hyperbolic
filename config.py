# config.py

DELAY_BETWEEN_MESSAGES = [20,100]
DELAY_BETWEEN_THREAD_START = [5,10]
ITERATIONS = [15, 30]
MAX_CONVERSATION_MEMORY = 10

OPENING_PROMPTS = [
    # Regulatory
    "Develop an adaptive compliance module: how to automate KYC rule changes when entering EU, UAE, and Singapore markets?",

    # UX
    "Create a flow for non-crypto users: how can we simplify on/off-ramps via bank cards while preserving self-custody?",

    # Partnerships
    "Devise a white-label strategy for neobanks: how can we integrate our SDK into their mobile apps with a rev-share model?",

    # DAO
    "Design a voting system with weighted coefficients: how to factor in stake, expertise, and early-contributor status?",

    # Risk Analysis
    "Study failure cases: why did projects like Terra and FTX fail stress tests? What mechanisms can prevent similar scenarios?",

    # Localization
    "Draft a roadmap for local markets: what adaptations are needed for the Middle East (Sharjah) vs Asia (Singapore) vs Latin America (El Salvador)?",

    # Integration
    "Design an API gateway for banks: how to ensure compatibility with ISO 20022 and legacy systems (SWIFT, SEPA)?"
]

SYSTEM_PROMPTS = [
    # Technical Implementation
    "As Chief Architect: propose 3 options balancing decentralization and compliance. Consider MiCA (EU) and FATF Travel Rule requirements. Request: evaluate trade-offs for the B2B segment.",

    # Economics
    "As a tokenomics expert: calculate parameters for 5-year sustainability. Include: dynamic burning, staking APY 15-25%, and volatility protection mechanisms. Request: stress-test for a 40% TVL drop.",

    # Regulatory
    "As a regulatory analyst: propose a white-label licensing solution. Focus: integration with national CBDCs (digital euro, e-rupee). Request: estimate implementation timelines for a pilot region.",

    # User Experience
    "As a UX strategist: suggest 3 interactive onboarding options (gamification, AI assistant, video tutorials). Request: metrics for conversion testing.",

    # Asset Security
    "As security lead: propose an architecture with risk separation: hot wallet for liquidity (<5% TVL), cold storage for reserves. Request: integration with hardware security modules (HSM).",

    # Business Development
    "As a BD director: map out partnerships (TradFi banks, payment processors, ERP systems). Request: monetization model for embedded finance.",

    # Decentralized Governance
    "As a DAO architect: suggest a mechanism for delegating votes to experts. Consider quadratic voting and Sybil-attack protection. Request: testnet scenarios.",

    # Risk Management
    "As a risk manager: develop a framework for sustainability audits (TVL diversification, oracle control, liquidity stress tests). Request: checklist for quarterly reviews.",

    # Global Expansion
    "As a localization expert: propose a hub-and-spoke model with local nodes. Consider: currency pairs, AML requirements, tax havens. Request: prioritize regions by TAM.",

    # System Integration
    "As an integration architect: propose a solution for real-time settlement between CBDCs, stablecoins, and fiat. Request: test cases for a neobank pilot."
]



OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'
OPENROUTER_MODELS = [
    {"model": "mistralai/devstral-small", "max_tokens": 4096, "temperature": 0.8},
    {"model": "openai/gpt-3.5-turbo", "max_tokens": 4096, "temperature": 0.8},
    {"model": "deepseek/deepseek-r1-0528", "max_tokens": 4096, "temperature": 0.8},
    {"model": "openai/openai/gpt-4.1-mini", "max_tokens": 4096, "temperature": 0.8},
    {"model": "openai/gpt-4.5-preview", "max_tokens": 4096, "temperature": 0.8},
    {"model": "sao10k/l3.1-euryale-70b", "max_tokens": 4096, "temperature": 0.8},
    {"model": "anthropic/claude-sonnet-4", "max_tokens": 4096, "temperature": 0.8},
    {"model": "google/gemini-2.5-flash", "max_tokens": 4096, "temperature": 0.8},
]


HYPERBOLIC_API_URL = "https://api.hyperbolic.xyz/v1/chat/completions"
HYPERBOLIC_MODELS = [
    {"model": "deepseek-ai/DeepSeek-R1-0528", "max_tokens": 512, "temperature": 0.1, "top_p": 0.9},
    {"model": "Qwen/Qwen3-235B-A22B", "max_tokens": 512, "temperature": 0.1, "top_p": 0.9},
    {"model": "deepseek-ai/DeepSeek-V3-0324", "max_tokens": 512, "temperature": 0.1, "top_p": 0.9},
    {"model": "Qwen/QwQ-32B", "max_tokens": 1024, "temperature": 0.6, "top_p": 0.95},
    {"model": "deepseek-ai/DeepSeek-R1", "max_tokens": 508, "temperature": 0.1, "top_p": 0.9},
    {"model": "meta-llama/Meta-Llama-3.1-405B-Instruct", "max_tokens": 512, "temperature": 0.7, "top_p": 0.9},
    {"model": "NousResearch/Hermes-3-Llama-3.1-70B", "max_tokens": 512, "temperature": 0.7, "top_p": 0.9},
    {"model": "meta-llama/Meta-Llama-3.1-405B-Instruct" , "max_tokens": 512, "temperature": 0.7, "top_p": 0.9}
]