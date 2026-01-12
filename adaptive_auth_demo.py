import streamlit as st

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Adaptive Authentication Demo",
    layout="wide"
)

st.title("🔐 Adaptive Authentication Demo – Chat Application")

st.markdown(
    """
This demo **simulates adaptive authentication behavior** using contextual signals.
Authentication strength dynamically changes based on risk.
"""
)

# -------------------------------
# Session state initialization
# -------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "chat" not in st.session_state:
    st.session_state.chat = []

# -------------------------------
# Sidebar: Contextual signals
# -------------------------------
st.sidebar.header("🧠 Contextual Signals (Simulated)")

same_ip = st.sidebar.checkbox("Same Internet / IP Address")
same_browser = st.sidebar.checkbox("Same Browser")
same_device = st.sidebar.checkbox("Same Device")
same_location = st.sidebar.checkbox("Same Location")
normal_time = st.sidebar.checkbox("Usual Login Time")

signals = [
    same_ip,
    same_browser,
    same_device,
    same_location,
    normal_time
]

signal_count = sum(signals)

st.sidebar.markdown("---")
st.sidebar.metric("Signals Matched", signal_count)

# -------------------------------
# Risk-based decision engine
# -------------------------------
def determine_auth_method(count):
    if count >= 4:
        return "PIN"
    elif count >= 3:
        return "PASSWORD"
    else:
        return "SECURITY_QUESTION"

auth_method = determine_auth_method(signal_count)

# -------------------------------
# Authentication Panel
# -------------------------------
st.subheader("🛂 Authentication Checkpoint")

if not st.session_state.authenticated:

    if auth_method == "PIN":
        st.success("Low Risk Detected → PIN Authentication")
        pin = st.text_input("Enter 4-digit PIN", type="password")
        if st.button("Login with PIN"):
            if pin == "1234":
                st.session_state.authenticated = True
                st.success("Authentication Successful ✅")
            else:
                st.error("Invalid PIN")

    elif auth_method == "PASSWORD":
        st.warning("Medium Risk Detected → Password Required")
        password = st.text_input("Enter Password", type="password")
        if st.button("Login with Password"):
            if password == "password123":
                st.session_state.authenticated = True
                st.success("Authentication Successful ✅")
            else:
                st.error("Invalid Password")

    else:
        st.error("High Risk Detected → Security Question Required")
        answer = st.text_input("Who was your childhood best friend?")
        if st.button("Verify Answer"):
            if answer.lower().strip() == "rahul":
                st.session_state.authenticated = True
                st.success("Identity Verified ✅")
            else:
                st.error("Incorrect Answer")

else:
    st.success("User Authenticated – Chat Unlocked 🔓")

# -------------------------------
# Chat Application
# -------------------------------
st.markdown("---")
st.subheader("💬 Secure Chat Application")

if st.session_state.authenticated:

    chat_col, context_col = st.columns([3, 1])

    with chat_col:
        st.markdown("### Chat Window")

        for msg in st.session_state.chat:
            st.markdown(f"**You:** {msg}")

        user_msg = st.text_input("Type your message")

        if st.button("Send Message"):
            if user_msg:
                st.session_state.chat.append(user_msg)

    with context_col:
        st.markdown("### 🔍 Auth Context")
        st.write(f"Matched Signals: **{signal_count}**")
        st.write(f"Auth Method Used: **{auth_method}**")
        st.write("Risk Level:")
        if auth_method == "PIN":
            st.success("Low")
        elif auth_method == "PASSWORD":
            st.warning("Medium")
        else:
            st.error("High")

else:
    st.info("Authenticate to access chat")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Demo use-case: Adaptive Authentication | Zero-Trust | Risk-Based Access Control")
