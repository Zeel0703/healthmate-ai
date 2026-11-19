import os

import streamlit as st

from services.ai_service import get_health_advice, HealthMateConfigurationError
from utils.response_parser import extract_sections

st.set_page_config(
    page_title="HealthMate AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode


def get_theme_colors(dark):
    if dark:
        return {
            "bg_color": "#121212",
            "text_color": "#E0E0E0",
            "sidebar_bg": "#1E1E1E",
            "input_bg": "#2C2C2C",
            "button_bg": "#00C896",
            "button_text": "#FFFFFF",
        }
    return {
        "bg_color": "#FFFFFF",
        "text_color": "#202020",
        "sidebar_bg": "#F8F8F8",
        "input_bg": "#FFFFFF",
        "button_bg": "#00C896",
        "button_text": "#FFFFFF",
    }


theme = get_theme_colors(st.session_state.dark_mode)

with st.sidebar:
    logo_path = "assets/logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=120)
    st.markdown(
        f"<h3 style='text-align:center;color:{theme['text_color']}'>HealthMate AI</h3>",
        unsafe_allow_html=True,
    )
    st.button("🌙 / ☀️ Toggle Theme", on_click=toggle_theme)
    page = st.selectbox(
        "📚 Navigate",
        ["🏠 Homepage", "📝 Symptom Checker", "📖 About Us", "⚠️ Disclaimer"],
    )

st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {theme['bg_color']}; color: {theme['text_color']}; }}
    [data-testid="stSidebar"] {{ background-color: {theme['sidebar_bg']}; }}
    .stTextArea textarea, .stSelectbox div {{
        background-color: {theme['input_bg']} !important;
        color: {theme['text_color']} !important;
        border-radius: 10px;
    }}
    .stButton button {{
        background-color: {theme['button_bg']} !important;
        color: {theme['button_text']} !important;
        border-radius: 10px;
        font-weight: 600;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


if page == "🏠 Homepage":
    st.title("🏠 Welcome to HealthMate AI")

    st.markdown(
        """
        **HealthMate AI** is an educational, AI-powered health information
        assistant developed in support of **SDG 3: Good Health and Well-being**.

        ### What it can do
        - Accept symptom descriptions in natural language.
        - Generate general information about possible causes.
        - Suggest basic home-care measures.
        - Present responses in English, Hindi, or Gujarati.

        ### How it works
        1. Describe your symptoms.
        2. The application sends the description to the configured language model.
        3. The response is translated into your selected language when requested.
        4. The application displays the generated information.
        """
    )

    if st.button("🔍 Get Advice"):
        st.info("Please select Symptom Checker from the navigation menu.")

elif page == "📝 Symptom Checker":
    st.title("📝 Symptom Checker")

    st.warning(
        "This educational tool cannot diagnose conditions or assess emergencies. "
        "Do not delay professional medical care based on its output."
    )

    language = st.selectbox(
        "🌐 Choose Language",
        ["English", "Hindi", "Gujarati"]
    )

    language_codes = {
        "English": "en",
        "Hindi": "hi",
        "Gujarati": "gu"
    }

    symptom_input = st.text_area(
        "💬 Describe your symptoms",
        height=150,
        placeholder="e.g., I have a sore throat and fever",
        max_chars=2000,
    )

    if st.button("🔍 Get Advice"):
        if not symptom_input.strip():
            st.warning("Please enter your symptoms above.")

        else:
            try:
                with st.spinner("Generating general health information..."):
                    response = get_health_advice(
                        symptom_input.strip(),
                        language
                    )

                    # Extract sections before translation.
                    sections = extract_sections(response)

                    possible_causes = sections["possible_causes"]
                    home_remedies = sections["home_remedies"]

                    possible_causes = sections["possible_causes"]
                    home_remedies = sections["home_remedies"]

                st.subheader("🧠 Possible Causes")

                with st.expander("View information", expanded=True):
                    st.write(
                        possible_causes
                        or "No clearly labelled possible-causes section was found."
                    )

                st.subheader("🏠 Home-Care Suggestions")

                with st.expander("View suggestions", expanded=True):
                    st.write(
                        home_remedies
                        or "No clearly labelled home-care section was found."
                    )

            except HealthMateConfigurationError as exc:
                st.error(str(exc))

            except Exception:
                st.error(
                    "We couldn't generate health information right now. "
                    "Please try again in a moment."
                )

elif page == "📖 About Us":
    st.title("📖 About Us")

    st.markdown(
        """
        HealthMate AI was developed as a capstone project during the
        **GTU Summer Internship 2025**, organized by CSRBOX in collaboration
        with IBM SkillsBuild.

        The project explores how conversational AI and a simple web interface
        can make general health information easier to access.
        """
    )

elif page == "⚠️ Disclaimer":
    st.title("⚠️ Disclaimer")

    st.warning(
        """
        HealthMate AI is an educational project that provides general,
        AI-generated health information only.

        It is not a medical device, diagnostic system, or substitute for
        professional medical advice, diagnosis, or treatment. AI-generated
        content can be inaccurate or incomplete. Consult a qualified
        healthcare professional about medical concerns. For urgent or
        emergency symptoms, contact local emergency services immediately.
        """
    )
