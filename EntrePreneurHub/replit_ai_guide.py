import streamlit as st

def show():
    st.header("Leveraging Replit AI for Business")
    
    st.markdown("""
    Replit AI is a powerful tool that can accelerate your business development process. 
    It combines coding, deployment, and AI assistance in one platform, making it particularly 
    valuable for entrepreneurs without extensive technical backgrounds.
    """)
    
    # What is Replit AI section
    st.subheader("What is Replit AI?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Replit AI** is an AI-powered coding assistant integrated into the Replit development platform. It helps you:
        
        - Generate code based on natural language descriptions
        - Debug and improve existing code
        - Explain code and concepts
        - Provide guidance on best practices
        - Assist with creating entire applications
        
        It's designed to make programming more accessible, especially for beginners, while also 
        boosting productivity for experienced developers.
        """)
    
    with col2:
        st.info("""
        **Key Advantage**: Replit AI combines code generation with an integrated development environment (IDE) and hosting, 
        letting you go from idea to live application in one platform.
        """)
    
    # Business applications section
    st.subheader("How Replit AI Can Power Your South African Business")
    
    use_cases = {
        "Website Development": """
        - Create a professional business website without extensive coding knowledge
        - Build e-commerce platforms with integrated payment systems (including South African payment methods)
        - Develop customized landing pages for marketing campaigns
        - How Replit AI helps: Generate HTML, CSS, and JavaScript code based on your descriptions of what you want
        """,
        
        "Custom Business Applications": """
        - Develop internal tools for business management
        - Create customer-facing applications
        - Build prototypes to validate business ideas quickly
        - How Replit AI helps: Guide you through creating a complete application, from database design to user interface
        """,
        
        "Automation Solutions": """
        - Automate repetitive business tasks
        - Create data processing workflows
        - Build integrations between different business tools
        - How Replit AI helps: Generate scripts that automate processes based on your description of the task
        """,
        
        "Data Analysis & Reporting": """
        - Create custom dashboards for business intelligence
        - Build data analysis pipelines
        - Generate automated reports
        - How Replit AI helps: Assist with data processing code and visualization implementation
        """,
        
        "AI-Enhanced Customer Service": """
        - Build customer service chatbots
        - Create automated response systems
        - Develop personalized recommendation engines
        - How Replit AI helps: Generate code for AI interactions and integrations with messaging platforms
        """
    }
    
    for use_case, description in use_cases.items():
        with st.expander(use_case):
            st.markdown(description)
    
    # Step-by-step guide
    st.subheader("Step-by-Step Guide: Building a Business Solution with Replit AI")
    
    steps = [
        {
            "title": "1. Create a Replit Account",
            "content": """
            - Go to [Replit](https://replit.com) and sign up for an account
            - Verify your email address
            - Complete your profile with a professional username
            """
        },
        {
            "title": "2. Start a New Project",
            "content": """
            - Click the "+ Create" button
            - Choose a template based on your project needs (e.g., Node.js for a web application, Python for data analysis)
            - Name your project appropriately
            """
        },
        {
            "title": "3. Describe Your Requirements to Replit AI",
            "content": """
            - Use the AI chat feature (typically in the sidebar)
            - Clearly describe what you want to build
            - Be specific about South African requirements (e.g., "Create a form that collects South African ID numbers with validation")
            """
        },
        {
            "title": "4. Review and Refine the Generated Code",
            "content": """
            - Examine the code provided by Replit AI
            - Ask the AI to explain any parts you don't understand
            - Request modifications as needed
            """
        },
        {
            "title": "5. Test Your Solution",
            "content": """
            - Run the code within Replit
            - Test all features thoroughly
            - Use the Replit AI to help debug any issues
            """
        },
        {
            "title": "6. Deploy Your Solution",
            "content": """
            - Replit automatically hosts your application
            - Get a shareable link to your application
            - Configure custom domains if needed for your business
            """
        },
        {
            "title": "7. Integrate with Business Systems",
            "content": """
            - Connect your solution to other business tools
            - Set up analytics to track usage
            - Implement South African-specific integrations (e.g., payment gateways like PayFast or Peach Payments)
            """
        }
    ]
    
    for step in steps:
        with st.expander(step["title"]):
            st.markdown(step["content"])
    
    # Example prompts
    st.subheader("Effective Prompts for South African Business Solutions")
    
    st.markdown("""
    How you communicate with Replit AI significantly impacts the quality of the code it generates. 
    Here are some example prompts tailored for South African business contexts:
    """)
    
    example_prompts = [
        {
            "title": "E-commerce Website",
            "prompt": """
            "Create a simple e-commerce website that supports South African Rand (ZAR) as the currency, 
            integrates with PayFast payment gateway, and calculates VAT at 15%. 
            Include product listing, shopping cart, and checkout pages."
            """
        },
        {
            "title": "Business Registration Form",
            "prompt": """
            "Build a form that collects information needed for registering a business in South Africa, 
            including company name validation, tax number validation, and required fields 
            according to CIPC standards. Include validation for South African ID numbers."
            """
        },
        {
            "title": "Invoice Generator",
            "prompt": """
            "Create an invoice generator that complies with SARS requirements for South African businesses. 
            Include fields for company details, VAT number, invoice number, client details, 
            line items, VAT calculation at 15%, and totals in ZAR."
            """
        },
        {
            "title": "Social Media Analytics Dashboard",
            "prompt": """
            "Develop a dashboard that tracks social media performance for a South African business. 
            Include metrics like engagement rate, follower growth, and post reach. 
            Display time data in SAST (South African Standard Time) and allow filtering by date ranges."
            """
        }
    ]
    
    for example in example_prompts:
        with st.expander(example["title"]):
            st.code(example["prompt"], language="")
    
    # Tips for success
    st.subheader("Tips for Success with Replit AI")
    
    success_tips = [
        "**Be Specific**: Clearly describe what you need, including South African-specific requirements",
        "**Start Small**: Begin with core functionality and expand gradually",
        "**Learn Iteratively**: Use each interaction to learn more about coding and development",
        "**Leverage Templates**: Use Replit's templates as starting points for common business applications",
        "**Document Your Process**: Keep track of successful prompts and approaches for future reference",
        "**Understand Limitations**: Some complex business logic may require additional guidance or expertise"
    ]
    
    for tip in success_tips:
        st.markdown(f"- {tip}")
    
    # Resources section
    st.subheader("Additional Replit AI Resources")
    
    st.markdown("""
    - [Replit Documentation](https://docs.replit.com/)
    - [Replit AI Documentation](https://docs.replit.com/programming-ide/ai-help)
    - [Replit Templates](https://replit.com/templates)
    - [Replit Community](https://replit.com/community)
    """)
    
    st.success("💡 **Pro Tip**: Join South African developer communities on platforms like Discord or Slack to find other entrepreneurs using Replit AI for their businesses. Sharing experiences and code solutions can accelerate your progress significantly.")
