import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.header("Business Formation Process in South Africa")
    
    st.markdown("""
    Starting a business in South Africa involves several legal and regulatory steps. 
    This guide outlines the process, with special focus on how Replit AI can help streamline your business formation.
    """)
    
    # Legal business structures
    st.subheader("Legal Business Structures in South Africa")
    
    business_structures = {
        "Sole Proprietorship": {
            "description": "An unincorporated business owned by one individual",
            "pros": "Simple to establish, minimal paperwork, full control, lower compliance costs",
            "cons": "Unlimited personal liability, limited access to funding, potential difficulty scaling",
            "registration": "No formal registration required, but must register with SARS for tax purposes",
            "suitable_for": "Freelancers, consultants, small online businesses with limited liability concerns"
        },
        "Private Company (Pty Ltd)": {
            "description": "A separate legal entity owned by shareholders",
            "pros": "Limited liability, easier access to funding, professional image, perpetual existence",
            "cons": "More expensive to set up, higher compliance requirements, more complex administration",
            "registration": "Register with CIPC, obtain company registration number, register for tax",
            "suitable_for": "Technology startups, e-commerce businesses, businesses seeking investment"
        },
        "Personal Liability Company (Inc)": {
            "description": "Company where directors are jointly liable for company debts",
            "pros": "Professional credibility, perpetual existence, suitable for professional services",
            "cons": "Directors have personal liability, compliance requirements",
            "registration": "Register with CIPC, followed by tax registration",
            "suitable_for": "Professional service providers like law firms, accounting practices"
        },
        "Business Trust": {
            "description": "Legal entity created by a trust deed",
            "pros": "Protection of assets, tax benefits, privacy",
            "cons": "Complex to establish, expensive setup, regulatory scrutiny",
            "registration": "Create trust deed, register with Master of High Court, register for tax",
            "suitable_for": "Asset holding, estate planning, complex businesses with significant assets"
        },
        "Cooperative": {
            "description": "An autonomous association of persons united voluntarily to meet common economic and social needs",
            "pros": "Democratic member control, limited liability, possible tax advantages",
            "cons": "Complex decision-making process, potential conflicts between members",
            "registration": "Register with CIPC as a cooperative, register for tax",
            "suitable_for": "Community-based businesses, agricultural ventures, collaborative tech initiatives"
        }
    }
    
    structure_selection = st.selectbox(
        "Select a business structure to learn more:",
        list(business_structures.keys())
    )
    
    selected_structure = business_structures[structure_selection]
    
    # Display structure details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### {structure_selection}")
        st.markdown(f"**Description**: {selected_structure['description']}")
        st.markdown(f"**Suitable for**: {selected_structure['suitable_for']}")
        st.markdown(f"**Registration process**: {selected_structure['registration']}")
    
    with col2:
        st.markdown("#### Pros")
        st.markdown(selected_structure['pros'])
        st.markdown("#### Cons")
        st.markdown(selected_structure['cons'])
    
    # Step-by-step business registration process
    st.subheader("Step-by-Step Business Registration Process")
    
    steps = [
        {
            "step": "1. Choose a Business Name",
            "description": """
            - Search for availability on the CIPC website
            - Ensure the name complies with regulations
            - Reserve the name before registration
            
            **How Replit AI can help**: Create a script to check name availability through CIPC APIs or web scraping.
            """
        },
        {
            "step": "2. Prepare Required Documents",
            "description": """
            - Memorandum of Incorporation (for companies)
            - Certified copies of ID documents for all directors/members
            - Proof of address for the business
            - Registration forms (available on CIPC website)
            
            **How Replit AI can help**: Generate templates for required business documents.
            """
        },
        {
            "step": "3. Register with CIPC",
            "description": """
            - Submit registration application to CIPC
            - Pay registration fees
            - Receive company registration certificate
            
            **How Replit AI can help**: Create a tracking system for your registration process.
            """
        },
        {
            "step": "4. Register for Tax with SARS",
            "description": """
            - Apply for income tax registration
            - Register for VAT (if applicable)
            - Register as an employer (if applicable)
            - Register for UIF (Unemployment Insurance Fund)
            
            **How Replit AI can help**: Build a tax calendar app with reminders for filing dates.
            """
        },
        {
            "step": "5. Open a Business Bank Account",
            "description": """
            - Compare business banking options
            - Prepare required documentation
            - Visit bank or complete online application
            
            **How Replit AI can help**: Create a comparison tool for different bank offerings.
            """
        },
        {
            "step": "6. Register with Department of Labor",
            "description": """
            - Register for UIF and COIDA (Compensation for Occupational Injuries and Diseases Act)
            - Understand employment regulations
            
            **How Replit AI can help**: Generate employee documentation templates compliant with South African labor law.
            """
        },
        {
            "step": "7. Additional Industry-Specific Registrations",
            "description": """
            - Research licenses or permits required for your specific industry
            - Apply for relevant permits
            
            **How Replit AI can help**: Build a database of industry-specific requirements based on your business type.
            """
        },
        {
            "step": "8. Create a Business Website and Online Presence",
            "description": """
            - Register a domain name (preferably .co.za)
            - Develop a business website
            - Set up social media profiles
            
            **How Replit AI can help**: Generate a complete business website with your company details.
            """
        }
    ]
    
    for step_info in steps:
        with st.expander(step_info["step"]):
            st.markdown(step_info["description"])
    
    # Timeline visualization
    st.subheader("Estimated Timeline for Business Formation")
    
    timeline_data = {
        'Stage': [
            'Name Reservation', 
            'Company Registration', 
            'Tax Registration', 
            'Bank Account Setup', 
            'Labor Registration',
            'Website Development'
        ],
        'Minimum Days': [2, 7, 10, 5, 5, 1],
        'Maximum Days': [10, 21, 30, 15, 14, 7]
    }
    
    timeline_df = pd.DataFrame(timeline_data)
    
    # Create a horizontal bar chart for timeline
    fig = px.bar(timeline_df, 
                 y='Stage', 
                 x=['Minimum Days', 'Maximum Days'], 
                 barmode='group',
                 orientation='h',
                 labels={"value": "Days Required", "variable": "Duration"},
                 title="Estimated Business Formation Timeline (in Working Days)",
                 color_discrete_sequence=["#2C6EBF", "#4CA3DD"])
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.caption("Note: Actual timelines may vary based on current processing times and the completeness of your application.")
    
    # Costs section
    st.subheader("Estimated Costs for Business Formation")
    
    cost_data = {
        'Item': [
            'Name Reservation', 
            'Company Registration', 
            'Business Bank Account', 
            'Domain Registration (.co.za)', 
            'Basic Website Development',
            'Accounting Services Setup',
            'Business Logo Design'
        ],
        'Estimated Cost (ZAR)': [50, 175, 0, 150, 0, 1500, 500],
        'Notes': [
            'Fee paid to CIPC',
            'Fee paid to CIPC for private company',
            'Many banks offer free business accounts for new businesses',
            'Annual cost through local domain providers',
            'Using Replit AI to create your website',
            'Basic accounting setup (varies widely)',
            'Using design services or AI tools'
        ]
    }
    
    cost_df = pd.DataFrame(cost_data)
    
    st.dataframe(cost_df, use_container_width=True)
    
    st.info("""
    💡 **Cost-Saving Tip**: By using Replit AI to create your business website, business management tools, 
    and even to help draft certain documents, you can significantly reduce startup costs compared to hiring developers.
    """)
    
    # Using Replit AI for business formation
    st.subheader("How Replit AI Can Support Your Business Formation")
    
    replit_applications = [
        {
            "title": "CIPC Registration Tracker",
            "description": """
            Build a simple application to track your registration progress with CIPC, 
            including document checklists, submission dates, and status updates.
            """
        },
        {
            "title": "Business Plan Generator",
            "description": """
            Create a tool that helps you draft a comprehensive business plan based on South African business standards, 
            including sections specifically focused on local market conditions.
            """
        },
        {
            "title": "South African Tax Calendar",
            "description": """
            Develop a tax reminder system that alerts you about upcoming filing deadlines 
            for provisional tax, VAT, PAYE, and other tax obligations specific to South Africa.
            """
        },
        {
            "title": "Business Website with Legal Compliance",
            "description": """
            Generate a business website that includes all legally required elements like privacy policy, 
            terms of service, and POPIA compliance statements tailored to South African law.
            """
        },
        {
            "title": "B-BBEE Calculator and Planner",
            "description": """
            Build a tool to calculate your B-BBEE (Broad-Based Black Economic Empowerment) score 
            and identify actions to improve your rating, which can help with government contracts.
            """
        }
    ]
    
    for i, app in enumerate(replit_applications):
        with st.expander(f"{i+1}. {app['title']}"):
            st.markdown(app['description'])
    
    # Additional resources
    st.subheader("Additional Resources for Business Formation")
    
    st.markdown("""
    ### Official Government Resources
    
    - [Companies and Intellectual Property Commission (CIPC)](https://www.cipc.co.za)
    - [South African Revenue Service (SARS)](https://www.sars.gov.za)
    - [Department of Labor](https://www.labour.gov.za)
    - [Small Enterprise Development Agency (SEDA)](https://www.seda.org.za)
    
    ### Business Support Organizations
    
    - [Business Partners](https://www.businesspartners.co.za)
    - [National Small Business Chamber](https://www.nsbc.org.za)
    - [Black Business Council](https://www.blackbusinesscouncil.org)
    - [South African Chamber of Commerce and Industry](https://www.sacci.org.za)
    
    ### Legal Resources
    
    - [Legal Aid South Africa](https://legal-aid.co.za)
    - [ProBono.Org](https://www.probono.org.za)
    - [Law Society of South Africa](https://www.lssa.org.za)
    """)
    
    # Local business ecosystem map
    st.subheader("South African Business Ecosystem")
    
    # Display South Africa map
    st.markdown("""
    <div style="text-align: center">
        <svg width="600" height="400" viewBox="0 0 600 400">
            <path d="M300,50 Q450,100 400,200 Q350,300 300,350 Q250,300 200,200 Q150,100 300,50" fill="#f0f0f0" stroke="#333" stroke-width="2"/>
            <circle cx="300" cy="100" r="30" fill="#e74c3c" opacity="0.7"/>
            <text x="300" y="105" text-anchor="middle" fill="white" font-weight="bold">Gauteng</text>
            <circle cx="370" cy="200" r="25" fill="#3498db" opacity="0.7"/>
            <text x="370" y="205" text-anchor="middle" fill="white" font-weight="bold">WC</text>
            <circle cx="230" cy="200" r="25" fill="#2ecc71" opacity="0.7"/>
            <text x="230" y="205" text-anchor="middle" fill="white" font-weight="bold">KZN</text>
            <circle cx="300" cy="280" r="20" fill="#f39c12" opacity="0.7"/>
            <text x="300" y="285" text-anchor="middle" fill="white" font-weight="bold">EC</text>
            <circle cx="250" cy="150" r="15" fill="#9b59b6" opacity="0.7"/>
            <text x="250" y="155" text-anchor="middle" fill="white" font-weight="bold">FS</text>
            <text x="300" y="30" text-anchor="middle" font-weight="bold">South African Business Hubs</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    st.caption("Major business hubs in South Africa showing relative tech ecosystem activity")
    
    st.markdown("""
    ### Key Regional Business Development Agencies:
    
    - **Gauteng**: [Gauteng Growth and Development Agency](https://www.ggda.co.za/)
    - **Western Cape**: [Wesgro](https://www.wesgro.co.za/)
    - **KwaZulu-Natal**: [Trade & Investment KZN](https://www.tikzn.co.za/)
    - **Eastern Cape**: [Eastern Cape Development Corporation](https://www.ecdc.co.za/)
    """)
    
    st.success("""
    **Final Tip**: While using Replit AI can dramatically reduce the technical barriers to starting a business, 
    it's always advisable to consult with a legal professional or business advisor who specializes in South African 
    business law to ensure full compliance with all regulations.
    """)
