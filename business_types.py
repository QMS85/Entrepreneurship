import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.header("Business Opportunities in South Africa")
    
    st.markdown("""
    South Africa offers diverse business opportunities across multiple sectors. 
    Here are some business types that are well-suited for entrepreneurs looking to leverage Replit AI:
    """)
    
    # Display tabs for different categories
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Tech & Software", 
        "E-commerce", 
        "Educational", 
        "Financial Services", 
        "Consulting"
    ])
    
    with tab1:
        st.subheader("Tech & Software Businesses")
        st.markdown("""
        ### 1. Web Development Agency
        Build websites for local businesses using Replit AI to quickly prototype and demonstrate solutions.
        
        ### 2. Mobile App Development
        Develop mobile applications for specific South African market needs using Replit AI for backend services.
        
        ### 3. Custom Software Solutions
        Create bespoke software for industries like mining, agriculture, or healthcare that are prominent in South Africa.
        
        ### 4. AI Chatbot Development
        Build specialized chatbots for customer service, educational content, or healthcare guidance using Replit AI's capabilities.
        """)
        
        st.info("The software development market in South Africa is growing at approximately 12% annually, creating significant opportunities for new entrants.")
    
    with tab2:
        st.subheader("E-commerce Businesses")
        st.markdown("""
        ### 1. Online Marketplace
        Create niche marketplaces connecting South African producers with consumers, using Replit AI for backend and recommendation systems.
        
        ### 2. Dropshipping Business
        Build a dropshipping site focused on South African or African products using Replit to manage your storefront.
        
        ### 3. Subscription Box Service
        Develop subscription services for local products with a tech-enabled management system built on Replit.
        
        ### 4. Digital Product Store
        Sell digital products like templates, courses, or e-books with a custom platform built using Replit AI.
        """)
        
        st.info("E-commerce in South Africa grew by over 66% during the pandemic and continues to expand as more consumers shop online.")
    
    with tab3:
        st.subheader("Educational Businesses")
        st.markdown("""
        ### 1. Coding Academy
        Launch a coding academy that teaches South African students using Replit as the learning platform.
        
        ### 2. Online Tutoring Platform
        Create a platform connecting tutors with students, possibly focusing on areas with educational gaps in South Africa.
        
        ### 3. Corporate Training Services
        Offer specialized digital skills training to businesses looking to upskill their workforce.
        
        ### 4. Educational Content Creation
        Develop interactive educational content tailored to the South African curriculum using Replit AI.
        """)
        
        st.info("There's a significant skills gap in South Africa, particularly in technology fields, creating demand for accessible education services.")
    
    with tab4:
        st.subheader("Financial Services")
        st.markdown("""
        ### 1. Fintech Solutions
        Develop specialized financial services applications addressing unique South African market needs.
        
        ### 2. Financial Literacy Platform
        Create interactive financial education tools tailored to South African economic realities.
        
        ### 3. SME Funding Platform
        Build platforms connecting small businesses with investors or alternative funding sources.
        
        ### 4. Automated Accounting Solutions
        Develop simplified accounting systems for small businesses with South African tax compliance built-in.
        """)
        
        st.info("South Africa has a growing fintech sector with opportunities to serve both banked and underbanked populations.")
    
    with tab5:
        st.subheader("Consulting Services")
        st.markdown("""
        ### 1. Digital Transformation Consulting
        Help traditional businesses digitize their operations using Replit AI to demonstrate proof-of-concepts.
        
        ### 2. AI Implementation Consulting
        Assist businesses in implementing AI solutions for efficiency and growth using Replit AI as a development platform.
        
        ### 3. Tech-Enabled Marketing Services
        Offer data-driven marketing services with custom analytics tools built on Replit.
        
        ### 4. Business Process Automation
        Help businesses automate repetitive tasks with custom solutions built using Replit AI.
        """)
        
        st.info("As South African businesses seek to digitize operations, there's growing demand for consultants who can bridge technical and business requirements.")
    
    # Market opportunity visualization
    st.subheader("Market Opportunity Analysis")
    
    # Create dataframe for visualization
    data = {
        'Business Category': ['Tech & Software', 'E-commerce', 'Educational Services', 'Fintech', 'Consulting'],
        'Market Size (Billions ZAR)': [15.2, 28.6, 9.7, 22.4, 18.9],
        'Annual Growth (%)': [12, 18, 14, 16, 9],
        'Startup Cost (1-10)': [4, 5, 6, 7, 3],
        'Tech Complexity (1-10)': [8, 6, 5, 9, 4]
    }
    
    df = pd.DataFrame(data)
    
    # Create visualization
    fig = px.scatter(
        df, 
        x="Startup Cost (1-10)", 
        y="Annual Growth (%)", 
        size="Market Size (Billions ZAR)", 
        color="Business Category",
        hover_name="Business Category",
        size_max=60,
        labels={
            "Startup Cost (1-10)": "Initial Investment Required (Lower is Better)",
            "Annual Growth (%)": "Annual Market Growth (%)"
        },
        title="Business Opportunity Analysis by Category"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ## Key Factors for Business Success in South Africa
    
    When choosing a business type, consider these important factors:
    
    1. **Market Need**: Identify genuine problems faced by South African consumers or businesses
    2. **Regulatory Requirements**: Understand the specific regulations for your industry
    3. **Infrastructure Considerations**: Plan for infrastructure challenges like internet connectivity or power supply
    4. **Local Competition**: Research existing solutions and identify your unique value proposition
    5. **Scalability**: Consider how Replit AI can help you scale operations without proportional cost increases
    """)
    
    st.success("💡 **Pro Tip**: Start with a Minimum Viable Product (MVP) to test your business concept before significant investment. Replit AI is perfect for rapid prototyping and MVP development.")
