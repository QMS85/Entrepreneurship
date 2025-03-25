import streamlit as st
import pandas as pd

def show():
    st.header("Education & Skills Development")
    
    st.markdown("""
    Building successful businesses with Replit AI requires both technical knowledge and business acumen. 
    This section outlines educational pathways and resources tailored for South African entrepreneurs.
    """)
    
    # Key skill areas section
    st.subheader("Key Skill Areas for Tech Entrepreneurs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Technical Skills")
        st.markdown("""
        - **Programming Fundamentals**: Basic understanding of coding concepts
        - **Web Development**: HTML, CSS, JavaScript basics
        - **Data Analysis**: Basic data interpretation skills
        - **AI Literacy**: Understanding how to work with AI tools
        - **Problem Solving**: Logical approach to technical challenges
        """)
        
    with col2:
        st.markdown("### Business Skills")
        st.markdown("""
        - **South African Business Regulations**: Understanding local requirements
        - **Market Research**: Identifying viable opportunities
        - **Financial Management**: Budgeting and financial planning
        - **Marketing**: Digital marketing skills
        - **Customer Development**: Understanding user needs
        """)
    
    # Learning pathways
    st.subheader("Learning Pathways")
    
    pathways = [
        {
            "title": "Beginner Path (3-6 months)",
            "description": """
            For those new to both technology and entrepreneurship:
            
            1. **Programming Basics** (1-2 months)
               - Complete a basic programming course focusing on Python or JavaScript
               - Learn to use Replit AI for code generation and explanation
            
            2. **Web Development Fundamentals** (1-2 months)
               - Learn HTML, CSS basics
               - Understand how websites function
            
            3. **South African Business Basics** (1 month)
               - Learn about business registration requirements
               - Understand basic tax obligations
               - Explore funding options for small businesses
            
            4. **First Project** (1 month)
               - Build a simple website or application using Replit AI
               - Focus on solving a specific problem for a potential customer
            """
        },
        {
            "title": "Intermediate Path (6-12 months)",
            "description": """
            For those with some technical or business background:
            
            1. **Advanced Programming Skills** (2-3 months)
               - Learn about APIs and integrations
               - Database fundamentals
               - More complex front-end development
            
            2. **South African Business Development** (2-3 months)
               - Digital marketing for the South African market
               - Local competition analysis
               - Understanding regulatory compliance in specific sectors
            
            3. **Product Development** (2-3 months)
               - User experience design
               - Product management basics
               - Customer feedback implementation
            
            4. **Growth Project** (1-3 months)
               - Build a fully-functional business solution with Replit AI
               - Implement South African payment integrations
               - Create a go-to-market strategy
            """
        },
        {
            "title": "Advanced Path (12+ months)",
            "description": """
            For scaling existing businesses or complex technical solutions:
            
            1. **Specialized Technical Skills** (3-6 months)
               - AI/ML implementation
               - Advanced security considerations
               - Performance optimization
               - Complex integrations with South African services
            
            2. **Business Scaling** (3-6 months)
               - Investment strategies in the South African context
               - Team building and management
               - Compliance with additional regulations as you grow
               - Partnership development
            
            3. **Industry Specialization** (6+ months)
               - Deep dive into industry-specific requirements
               - Networking with industry partners
               - Developing specialized solutions for your sector
            """
        }
    ]
    
    for pathway in pathways:
        with st.expander(pathway["title"]):
            st.markdown(pathway["description"])
    
    # South African educational resources
    st.subheader("South African Educational Resources")
    
    # Create tabs for different types of resources
    tab1, tab2, tab3, tab4 = st.tabs([
        "Formal Education", 
        "Bootcamps & Short Courses", 
        "Government Programs", 
        "Online Learning"
    ])
    
    with tab1:
        st.markdown("### Universities and Colleges")
        
        formal_education = pd.DataFrame({
            "Institution": [
                "University of Cape Town",
                "University of the Witwatersrand",
                "Stellenbosch University",
                "University of Johannesburg",
                "University of Pretoria"
            ],
            "Relevant Programs": [
                "Information Systems, Computer Science, Business Science",
                "Digital Business, Computer Science, Entrepreneurship",
                "Business Management, Computer Science, Information Systems",
                "Business IT, Entrepreneurship, Tech Innovation",
                "Informatics, Business Management, Entrepreneurship"
            ],
            "Website": [
                "https://www.uct.ac.za",
                "https://www.wits.ac.za",
                "https://www.sun.ac.za",
                "https://www.uj.ac.za",
                "https://www.up.ac.za"
            ]
        })
        
        st.dataframe(formal_education, use_container_width=True)
        
        st.markdown("""
        **Note**: Most South African universities now offer specialized courses in technology entrepreneurship, 
        digital business, and innovation. Some provide part-time and distance learning options suitable for working professionals.
        """)
    
    with tab2:
        st.markdown("### Bootcamps & Short Courses")
        
        bootcamps = pd.DataFrame({
            "Provider": [
                "CodeSpace Academy",
                "HyperionDev",
                "ALX Africa",
                "Digital Academy",
                "Umuzi"
            ],
            "Focus Areas": [
                "Web Development, Software Engineering",
                "Software Engineering, Data Science, Web Development",
                "Software Engineering, Entrepreneurship",
                "Web Development, UX Design, Digital Marketing",
                "Web Development, Data Science, Digital Marketing"
            ],
            "Duration": [
                "3-6 months",
                "3-6 months",
                "6-12 months",
                "3 months",
                "12 months"
            ],
            "Website": [
                "https://www.codespace.co.za",
                "https://www.hyperiondev.com",
                "https://www.alxafrica.com",
                "https://www.digitalacademy.co.za",
                "https://www.umuzi.org"
            ]
        })
        
        st.dataframe(bootcamps, use_container_width=True)
        
        st.markdown("""
        **Benefits**: These intensive programs often provide practical skills that can be immediately applied to your business. 
        Many offer mentorship and networking opportunities with industry professionals.
        """)
    
    with tab3:
        st.markdown("### Government and Support Programs")
        
        gov_programs = pd.DataFrame({
            "Program": [
                "Small Enterprise Development Agency (SEDA)",
                "Technology Innovation Agency (TIA)",
                "National Youth Development Agency (NYDA)",
                "Industrial Development Corporation (IDC)",
                "Companies and Intellectual Property Commission (CIPC)"
            ],
            "Support Offered": [
                "Business planning, Mentorship, Training workshops",
                "Innovation funding, Technical support, Commercialization",
                "Youth entrepreneurship, Skills development, Funding",
                "Business funding, Industry knowledge, Market access",
                "Business registration, IP registration, Compliance guidance"
            ],
            "Website": [
                "https://www.seda.org.za",
                "https://www.tia.org.za",
                "https://www.nyda.gov.za",
                "https://www.idc.co.za",
                "https://www.cipc.co.za"
            ]
        })
        
        st.dataframe(gov_programs, use_container_width=True)
        
        st.markdown("""
        **Access**: Many government programs offer free or subsidized training specifically for entrepreneurs. 
        Some have special focus areas for technology businesses or youth-owned enterprises.
        """)
    
    with tab4:
        st.markdown("### Online Learning Platforms")
        
        online_learning = pd.DataFrame({
            "Platform": [
                "GetSmarter (in partnership with South African universities)",
                "Coursera",
                "Udemy",
                "FreeCodeCamp",
                "Replit's Learning Resources"
            ],
            "Relevant Courses": [
                "Digital Marketing, Business Management, Data Analysis",
                "Programming, Web Development, Business courses",
                "Practical coding, Entrepreneurship, Marketing",
                "Web Development, JavaScript, Python (free)",
                "Coding tutorials focused on Replit platform (free)"
            ],
            "South African Context": [
                "Some courses specifically address South African business context",
                "Global content, but applicable skills",
                "Some South African instructors offer localized content",
                "Global content, supportive community",
                "Directly relevant to using Replit AI"
            ],
            "Website": [
                "https://www.getsmarter.com",
                "https://www.coursera.org",
                "https://www.udemy.com",
                "https://www.freecodecamp.org",
                "https://replit.com/learn"
            ]
        })
        
        st.dataframe(online_learning, use_container_width=True)
        
        st.markdown("""
        **Flexibility**: Online learning allows you to develop skills at your own pace while building your business. 
        Look for courses with practical projects that you can apply directly to your business needs.
        """)
    
    # South African business communities
    st.subheader("South African Tech & Business Communities")
    
    communities = [
        {
            "name": "Silicon Cape",
            "description": "A community of tech entrepreneurs, developers, and investors focused on growing the Western Cape tech ecosystem.",
            "url": "https://www.siliconcape.com"
        },
        {
            "name": "Heavy Chef",
            "description": "A learning platform for entrepreneurs with regular events and resources.",
            "url": "https://heavychef.com"
        },
        {
            "name": "Startup Grind South Africa",
            "description": "Local chapter of global startup community with events across major South African cities.",
            "url": "https://www.startupgrind.com/south-africa"
        },
        {
            "name": "ZATech",
            "description": "South African tech Slack community with channels for developers, entrepreneurs, and job opportunities.",
            "url": "https://zatech.co.za"
        },
        {
            "name": "Python South Africa (PyConZA)",
            "description": "Community for Python developers with annual conferences and regular meetups.",
            "url": "https://za.pycon.org"
        }
    ]
    
    for community in communities:
        st.markdown(f"**[{community['name']}]({community['url']})**: {community['description']}")
    
    st.info("""
    💡 **Networking Tip**: Joining tech communities is particularly valuable for entrepreneurs using Replit AI, 
    as you can connect with both technical talent and potential business partners or clients.
    """)
    
    # Skills development plan
    st.subheader("Creating Your Skills Development Plan")
    
    st.markdown("""
    To effectively build a business using Replit AI, create a personalized skills development plan:
    
    1. **Assess your current skills**:
       - Technical capabilities
       - Business knowledge
       - South African market understanding
    
    2. **Identify your skills gaps**:
       - What technical knowledge do you need to effectively use Replit AI?
       - What business skills do you need to succeed in your chosen sector?
       - What South African regulatory knowledge is required?
    
    3. **Prioritize learning needs**:
       - Focus first on skills that directly impact your ability to launch
       - Balance technical and business learning
    
    4. **Select appropriate resources**:
       - Choose learning options that fit your schedule and learning style
       - Look for South African-specific content when possible
    
    5. **Create a learning schedule**:
       - Set aside dedicated time for skills development
       - Balance learning with actual business building
    
    6. **Apply skills immediately**:
       - Use Replit AI to implement what you learn
       - Test concepts on real business challenges
    
    7. **Track progress and adjust**:
       - Document what you've learned
       - Identify new skill needs as your business evolves
    """)
    
    st.success("""
    **Remember**: The goal isn't to become an expert in everything, but to develop enough knowledge to effectively 
    leverage Replit AI for your business needs. For specialized requirements, consider partnering with experts or using 
    freelance services to complement your skills.
    """)
