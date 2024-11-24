import streamlit as st

def detect_spam(email_content):
    try:
        with open('spam.txt', 'r') as file:
            spam_keywords = [line.strip().lower() for line in file.readlines()] 
    except FileNotFoundError:
        print("Error: 'spam.txt' file not found. Please ensure it exists in the same directory.")
        return None
    lowercased_email = email_content.lower()
    for keyword in spam_keywords:
        if keyword in lowercased_email:
            return False 

    return True  

def main():
    st.set_page_config(page_title="Email Detection", page_icon=":email:", layout="centered")
    
    st.title("Email Detection App")
    st.markdown("""
        **Welcome to the Email Detection App!**  

        Enter the content of an email to determine if it's legitimate or unwanted.
    """)
    
    st.sidebar.header("Instructions")
    st.sidebar.markdown("""
        1. Enter the content of the email in the text box below.
        2. Click the "Predict" button to analyze the email.
        3. View the result indicating whether the email is legitimate or unwanted.
    """)
    
    email = st.text_area("Email Content", height=150)
    
    if st.button("Predict"):
        if not email:
            st.warning("Please enter the content of the email.")
        else:
            is_legit = detect_spam(email_content=email)

            if is_legit:
                st.success("The email is considered legitimate.")
            else:
                st.error("The email is considered unwanted.")
    
    st.markdown("---")
    st.markdown("""
        **Need Help?**  
        For further assistance, contact support or visit our [Help Center](#).
    """)

if __name__ == "__main__":
    main()
