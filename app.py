import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="A3 QC AI Platform", page_icon="⚡", layout="wide")

# Professional Dark Theme Styling with Enhanced Radio Button Visibility
st.markdown("""
<style>
    /* Entire App Background & Text Color */
    .stApp {
        background-color: #0B0F19;
        color: #F8FAFC;
    }
    
    /* Main Headings */
    .main-title { 
        text-align: center; 
        color: #38BDF8; 
        font-size: 2.8rem; 
        font-weight: 800; 
        margin-bottom: 2px; 
    }
    .sub-title { 
        text-align: center; 
        color: #94A3B8; 
        font-size: 1.15rem; 
        margin-bottom: 20px; 
        font-weight: 500; 
    }
    
    /* Project Card */
    .project-card { 
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); 
        color: #F8FAFC; 
        padding: 20px; 
        border-radius: 12px; 
        border-left: 6px solid #3B82F6; 
        margin-bottom: 25px; 
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); 
    }
    .project-card h4 { color: #60A5FA; margin-bottom: 8px; }
    
    /* Module Headers */
    .module-header { 
        font-size: 1.6rem; 
        font-weight: 700; 
        color: #38BDF8; 
        margin-bottom: 12px; 
        border-bottom: 2px solid #334155; 
        padding-bottom: 8px; 
    }

    /* Fix text colors and sizes for inputs and labels in dark mode */
    .stTextInput label, .stSelectbox label, .stSlider label, .stNumberInput label, .stTextArea label, .stFileUploader label {
        color: #E2E8F0 !important;
        font-size: 1.05rem !important;
    }

    /* Make Radio Options Prominent and Larger */
    .stRadio label p, .stRadio div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Main Title & Header
st.markdown("<div class='main-title'>⚡ A3 QC AI Platform</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>An All-in-One Multi-Module Artificial Intelligence System</div>", unsafe_allow_html=True)

# Project Metadata Card
with st.container():
    st.markdown("""
    <div class='project-card'>
        <h4>🏛️ Punjab College — Quaid Campus (ICS • CQ-31 Section)</h4>
        <p><b>Project Supervisor:</b> Prof. Naveed Asif (Computer & Artificial Intelligence)</p>
        <p><b>Team 48 Project:</b> A3 QC AI Project</p>
        <p><b>Team Members:</b> Abdul Shakoor (2651949) | Ahasan Nisar (2651943) | Abdul Qadoos (2651950)</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar API Key Setup
st.sidebar.header("⚙️ System Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if not api_key:
    st.warning("⚠️ Please enter your free **Gemini API Key** in the sidebar to activate all AI modules.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # =========================================================
    # CHAT SECTION: "Where should we start?"
    # =========================================================
    st.markdown("### 💬 AI Interactive Chat Assistant")
    st.markdown("<p style='color: #94A3B8;'>Where should we start? Ask anything or chat with your AI partner below:</p>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_chat_input := st.chat_input("Where should we start? Type your query here..."):
        st.session_state.messages.append({"role": "user", "content": user_chat_input})
        with st.chat_message("user"):
            st.markdown(user_chat_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                chat_prompt = f"You are A3 QC AI Assistant built by Team 48, Punjab College Quaid Campus. Answer helpfully: {user_chat_input}"
                chat_res = model.generate_content(chat_prompt)
                st.markdown(chat_res.text)
                st.session_state.messages.append({"role": "assistant", "content": chat_res.text})

    st.write("---")

    # =========================================================
    # MODULES SECTION
    # =========================================================
    st.subheader("🎯 Choose Your AI Module")
    
    selected_module = st.radio(
        "Select Module:",
        [
            "📚 AI Smart Learning Assistant",
            "🎯 AI Career Guidance System",
            "🌱 AI Eco Vision (Smart Waste Classifier)",
            "💰 AI Budget & Expense Advisor",
            "🌐 AI Accessibility & Language Assistant"
        ],
        horizontal=True
    )

    st.write("---")

    # =========================================================
    # MODULE 1: AI SMART LEARNING ASSISTANT
    # =========================================================
    if selected_module == "📚 AI Smart Learning Assistant":
        st.markdown("<div class='module-header'>📚 AI Smart Learning Assistant</div>", unsafe_allow_html=True)
        st.info("Generates quizzes, explains complex concepts, and builds personalized study schedules.")

        sub_tab1, sub_tab2, sub_tab3 = st.tabs(["📝 Quiz Generator", "💡 Topic Explainer", "📅 Study Plan Creator"])

        with sub_tab1:
            quiz_topic = st.text_input("Topic for Quiz:", placeholder="e.g., Photosynthesis, Data Structures")
            num_q = st.slider("Number of Questions:", 3, 10, 5)
            difficulty = st.selectbox("Difficulty Level:", ["Easy", "Medium", "Hard"])
            if st.button("Generate Quiz Now"):
                with st.spinner("Creating Quiz..."):
                    prompt = f"Generate a {difficulty} level quiz with {num_q} MCQs on {quiz_topic}. Include options (A,B,C,D) and correct answer keys with explanations at the end."
                    res = model.generate_content(prompt)
                    st.markdown(res.text)

        with sub_tab2:
            concept = st.text_input("Complex Topic/Concept:", placeholder="e.g., Quantum Entanglement, Recursion")
            if st.button("Explain Topic"):
                with st.spinner("Breaking down concept..."):
                    prompt = f"Explain the concept of '{concept}' simply using real-world analogies, step-by-step breakdown, and common misconceptions."
                    res = model.generate_content(prompt)
                    st.markdown(res.text)

        with sub_tab3:
            subject = st.text_input("Exam / Subject Name:")
            days_left = st.number_input("Days Left for Exam:", min_value=1, value=7)
            daily_hours = st.slider("Daily Study Hours Available:", 1, 12, 4)
            if st.button("Create Study Plan"):
                with st.spinner("Drafting Schedule..."):
                    prompt = f"Create a detailed day-by-day study schedule for {subject} covering {days_left} days with {daily_hours} hours of study per day. Use Spaced Repetition techniques."
                    res = model.generate_content(prompt)
                    st.markdown(res.text)

    # =========================================================
    # MODULE 2: AI CAREER GUIDANCE SYSTEM
    # =========================================================
    elif selected_module == "🎯 AI Career Guidance System":
        st.markdown("<div class='module-header'>🎯 AI Career Guidance System</div>", unsafe_allow_html=True)
        st.info("Analyzes skills & interests to provide tailored educational pathways and career options.")

        col1, col2 = st.columns(2)
        with col1:
            interests = st.text_area("Your Interests & Hobbies:", placeholder="e.g., Coding, Problem Solving, Gaming, Design")
            skills = st.text_area("Your Top Skills:", placeholder="e.g., Python, Communication, Mathematics, Art")
        with col2:
            education_level = st.selectbox("Current Education Level:", ["Matric / O-Levels", "ICS / FSC / A-Levels", "Undergraduate", "Other"])
            target_industry = st.text_input("Preferred Industry (Optional):", placeholder="e.g., Tech, Healthcare, Business")

        if st.button("Analyze & Recommend Careers"):
            with st.spinner("Analyzing Career Pathways..."):
                prompt = f"""
                Act as a Career Counselor. Analyze this student profile:
                - Education: {education_level}
                - Interests: {interests}
                - Skills: {skills}
                - Preferred Industry: {target_industry}

                Provide:
                1. Top 3 Career Roles aligned with their profile.
                2. Recommended University Majors / Certifications.
                3. Short-term and Long-term Action Plan.
                """
                res = model.generate_content(prompt)
                st.markdown(res.text)

    # =========================================================
    # MODULE 3: AI ECO VISION (SMART WASTE CLASSIFIER)
    # =========================================================
    elif selected_module == "🌱 AI Eco Vision (Smart Waste Classifier)":
        st.markdown("<div class='module-header'>🌱 AI Eco Vision — Smart Waste Classifier</div>", unsafe_allow_html=True)
        st.info("Identifies waste types from image or text descriptions and suggests sustainable recycling methods.")

        uploaded_file = st.file_uploader("Upload an Image of Waste Item:", type=["jpg", "jpeg", "png"])
        waste_desc = st.text_input("Or Describe the Waste Item (if no image available):", placeholder="e.g., Empty Plastic Soda Bottle, Electronic Circuit Board")

        if st.button("Classify Waste & Get Recycling Plan"):
            with st.spinner("Analyzing Waste Category..."):
                if uploaded_file is not None:
                    import PIL.Image
                    image = PIL.Image.open(uploaded_file)
                    st.image(image, caption="Uploaded Item", width=300)
                    prompt = ["Identify this waste item. Classify it into Plastic, Glass, Metal, Organic, E-waste, or Paper. Provide specific recycling steps and eco-friendly disposal guidelines.", image]
                    res = model.generate_content(prompt)
                    st.markdown(res.text)
                elif waste_desc:
                    prompt = f"Identify this waste item: '{waste_desc}'. Classify it (Plastic/Glass/Metal/Organic/E-Waste/Paper) and provide actionable recycling and disposal methods."
                    res = model.generate_content(prompt)
                    st.markdown(res.text)
                else:
                    st.warning("Please upload an image or type a description first!")

    # =========================================================
    # MODULE 4: AI BUDGET & EXPENSE ADVISOR
    # =========================================================
    elif selected_module == "💰 AI Budget & Expense Advisor":
        st.markdown("<div class='module-header'>💰 AI Budget & Expense Advisor</div>", unsafe_allow_html=True)
        st.info("Tracks expenses, visualizes spending breakdowns, and provides smart AI budgeting tips.")

        income = st.number_input("Total Monthly Income (PKR):", min_value=0, value=50000)

        st.subheader("Monthly Expenses")
        col1, col2, col3 = st.columns(3)
        with col1:
            rent = st.number_input("Rent / Utilities:", min_value=0, value=15000)
            food = st.number_input("Food & Groceries:", min_value=0, value=12000)
        with col2:
            transport = st.number_input("Transport / Fuel:", min_value=0, value=5000)
            education = st.number_input("Education / Books:", min_value=0, value=8000)
        with col3:
            entertainment = st.number_input("Entertainment / Misc:", min_value=0, value=4000)
            savings_goal = st.number_input("Monthly Target Savings:", min_value=0, value=6000)

        total_expense = rent + food + transport + education + entertainment
        remaining_balance = income - total_expense

        st.metric("Total Expenses", f"PKR {total_expense:,}")
        st.metric("Remaining Balance", f"PKR {remaining_balance:,}", delta=remaining_balance)

        if st.button("Get AI Financial Advice"):
            with st.spinner("Analyzing Budget..."):
                prompt = f"""
                Act as a Personal Financial Advisor.
                Monthly Income: PKR {income}
                Expenses: Rent ({rent}), Food ({food}), Transport ({transport}), Education ({education}), Misc ({entertainment})
                Total Expenses: PKR {total_expense}
                Remaining Savings Target: PKR {savings_goal}

                Give 4 concrete, realistic saving advice suggestions to optimize this budget for a student/family.
                """
                res = model.generate_content(prompt)
                st.markdown(res.text)

    # =========================================================
    # MODULE 5: AI ACCESSIBILITY & LANGUAGE ASSISTANT
    # =========================================================
    elif selected_module == "🌐 AI Accessibility & Language Assistant":
        st.markdown("<div class='module-header'>🌐 AI Accessibility & Language Assistant</div>", unsafe_allow_html=True)
        st.info("Translates languages, summarizes large text, and converts text into clear speech.")

        input_text = st.text_area("Enter Text:", height=150, placeholder="Paste paragraph, essay, or notes here...")

        act_tab1, act_tab2, act_tab3 = st.tabs(["🌐 Translate", "📝 Summarize", "🔊 Text-to-Speech"])

        with act_tab1:
            target_lang = st.selectbox("Select Target Language:", ["Urdu", "English", "Spanish", "French", "German", "Arabic"])
            if st.button("Translate Text"):
                if input_text:
                    with st.spinner("Translating..."):
                        prompt = f"Translate the following text accurately into {target_lang}:\n\n{input_text}"
                        res = model.generate_content(prompt)
                        st.markdown(res.text)
                else:
                    st.warning("Please enter text to translate.")

        with act_tab2:
            summary_length = st.select_slider("Summary Detail Level:", options=["Bullet Points", "Short Paragraph", "Detailed Executive Summary"])
            if st.button("Summarize Text"):
                if input_text:
                    with st.spinner("Summarizing..."):
                        prompt = f"Summarize the following text in {summary_length} format:\n\n{input_text}"
                        res = model.generate_content(prompt)
                        st.markdown(res.text)
                else:
                    st.warning("Please enter text to summarize.")

        with act_tab3:
            if st.button("Convert Text to Speech (Audio)"):
                if input_text:
                    with st.spinner("Generating Speech Audio..."):
                        try:
                            from gtts import gTTS
                            import io
                            tts = gTTS(text=input_text, lang='en')
                            fp = io.BytesIO()
                            tts.write_to_fp(fp)
                            st.audio(fp.getvalue(), format='audio/mp3')
                        except Exception as e:
                            st.error(f"Text-to-speech engine error: {e}")
                else:
                    st.warning("Please enter text first.")
