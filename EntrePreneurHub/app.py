import streamlit as st
import business_types
import replit_ai_guide
import educational_resources
import business_formation
import utils

def main():
    # Set page config
    st.set_page_config(
        page_title="South African Business Guide with Replit AI",
        page_icon="🇿🇦",
        layout="wide"
    )
    
    # Header
    st.title("Starting Businesses in South Africa with Replit AI")
    st.subheader("A Comprehensive Guide for Entrepreneurs")
    
    # Introduction
    with st.expander("Introduction", expanded=True):
        st.markdown("""
        Welcome to your comprehensive guide on starting businesses in South Africa using Replit AI. 
        This resource is designed to help entrepreneurs identify opportunities, 
        leverage technology, and navigate the business landscape in South Africa.
        
        Replit AI provides powerful tools for entrepreneurs to build, test, and deploy business solutions 
        without extensive technical knowledge. From creating websites to developing custom applications, 
        Replit AI can accelerate your business journey.
        """)
    
    # Navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio(
        "Go to",
        [
            "Business Opportunities in South Africa",
            "Leveraging Replit AI for Business",
            "Education & Skills Development",
            "Business Formation Process",
            "About This Guide"
        ]
    )
    
    # Display the selected section
    if selection == "Business Opportunities in South Africa":
        business_types.show()
    elif selection == "Leveraging Replit AI for Business":
        replit_ai_guide.show()
    elif selection == "Education & Skills Development":
        educational_resources.show()
    elif selection == "Business Formation Process":
        business_formation.show()
    elif selection == "About This Guide":
        show_about()
        
def show_about():
    st.header("About This Guide")
    st.markdown("""
    This guide was created to help aspiring entrepreneurs in South Africa understand:
    
    - The types of businesses they can start
    - How to leverage Replit AI for business development
    - Educational resources and skills development opportunities
    - Step-by-step process for business formation
    
    The information provided is based on current South African business regulations and tech industry practices.
    
    ### Disclaimer
    This guide is for informational purposes only and should not be considered legal or financial advice. 
    Always consult with qualified professionals before making business decisions.
    """)
    
    # Feedback form
    st.subheader("We'd love your feedback!")
    feedback = st.text_area("Share your thoughts or suggestions for improving this guide:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback! We'll use it to improve the guide.")

if __name__ == "__main__":
    main()
