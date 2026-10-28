import streamlit as st
from PIL import Image
from io import BytesIO
from datetime import date

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Construction Intelligence Platform",
    page_icon="🏗️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.title {
    font-size: 34px;
    font-weight: bold;
    color: #17365D;
}
.subtitle {
    color: #555555;
    font-size: 16px;
}
div[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #e5e7eb;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    '<div class="title">🏗️ Construction Intelligence Platform</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered support for construction planning, '
    'site monitoring, safety, and cost estimation.</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ----------------

st.sidebar.title("🏗️ Navigation")

page = st.sidebar.radio(
    "Select a module",
    [
        "Dashboard",
        "Site Image Analysis",
        "Construction Safety",
        "Project Planning",
        "Cost Estimation",
        "AI Construction Assistant",
        "About Project"
    ]
)

st.sidebar.divider()
st.sidebar.info("Final-Year B.Tech CSE Project")

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.subheader("Project Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Platform Status", "Running")
    col2.metric("AI Modules", "6")
    col3.metric("Today's Date", date.today().strftime("%d %b %Y"))

    st.divider()

    st.subheader("Platform Features")

    c1, c2 = st.columns(2)

    with c1:
        st.info("📷 **Site Image Analysis**")
        st.write(
            "Upload construction site images for initial visual review."
        )

        st.info("🦺 **Construction Safety**")
        st.write(
            "Review common construction hazards and safety precautions."
        )

        st.info("📋 **Project Planning**")
        st.write(
            "Prepare a basic project plan with activities and durations."
        )

    with c2:
        st.info("💰 **Cost Estimation**")
        st.write(
            "Estimate construction cost using area and cost per square foot."
        )

        st.info("🤖 **Construction Assistant**")
        st.write(
            "Get general construction guidance from a built-in knowledge base."
        )

        st.info("🌦️ **Weather Advisory**")
        st.write(
            "Review general precautions for different weather conditions."
        )

    st.warning(
        "This is a working prototype. Actual AI image recognition, "
        "live weather data, and multimodal language-model integration "
        "are not yet connected."
    )

# ---------------- SITE IMAGE ANALYSIS ----------------

elif page == "Site Image Analysis":

    st.subheader("📷 Construction Site Image Analysis")

    st.write(
        "Upload a construction site photograph for image validation "
        "and preliminary visual inspection."
    )

    uploaded_file = st.file_uploader(
        "Upload site image",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded_file is not None:

        try:
            image = Image.open(uploaded_file).convert("RGB")

            st.image(
                image,
                caption="Uploaded Construction Site Image",
                use_container_width=True
            )

            width, height = image.size

            col1, col2, col3 = st.columns(3)

            col1.metric("Image Width", f"{width} px")
            col2.metric("Image Height", f"{height} px")
            col3.metric(
                "File Size",
                f"{uploaded_file.size / 1024:.2f} KB"
            )

            st.success("Image uploaded and opened successfully.")

            st.subheader("Inspection Checklist")

            checklist = [
                "Check whether workers are wearing appropriate PPE.",
                "Look for exposed electrical wires.",
                "Check for unprotected edges and openings.",
                "Look for visible cracks or surface damage.",
                "Check whether materials obstruct walkways."
            ]

            for item in checklist:
                st.checkbox(item, key=f"check_{item}")

            st.warning(
                "The checklist is for manual inspection. "
                "The application does not automatically detect cracks "
                "or safety hazards yet. A qualified professional should "
                "assess structural concerns."
            )

        except Exception:
            st.error("Unable to open the image. Please upload a valid image.")

# ---------------- CONSTRUCTION SAFETY ----------------

elif page == "Construction Safety":

    st.subheader("🦺 Construction Safety Guidance")

    hazard = st.selectbox(
        "Select a potential hazard",
        [
            "Working at Height",
            "Electrical Hazard",
            "Falling Objects",
            "Unsafe Excavation",
            "Missing Personal Protective Equipment",
            "Fire Hazard",
            "Slippery Surface"
        ]
    )

    safety_guidance = {
        "Working at Height": [
            "Use appropriate fall-protection systems.",
            "Inspect scaffolding and ladders before use.",
            "Protect exposed edges and openings."
        ],
        "Electrical Hazard": [
            "Keep clear of exposed or damaged electrical wiring.",
            "Isolate power before authorized maintenance.",
            "Use qualified electricians for electrical work."
        ],
        "Falling Objects": [
            "Wear a suitable safety helmet.",
            "Secure tools and materials at height.",
            "Keep people away from overhead work zones."
        ],
        "Unsafe Excavation": [
            "Arrange a competent-person excavation inspection.",
            "Use appropriate protective systems where required.",
            "Keep equipment and spoil piles safely away from edges."
        ],
        "Missing Personal Protective Equipment": [
            "Use suitable helmets, footwear, and high-visibility clothing.",
            "Use eye, hearing, and respiratory protection when required.",
            "Follow the site's task-specific PPE requirements."
        ],
        "Fire Hazard": [
            "Keep emergency exits and access routes clear.",
            "Store flammable materials appropriately.",
            "Follow approved hot-work and fire-safety procedures."
        ],
        "Slippery Surface": [
            "Clean up spills promptly using safe procedures.",
            "Provide suitable warning signs.",
            "Keep walkways clear and use appropriate footwear."
        ]
    }

    st.write(f"### Recommended precautions: {hazard}")

    for step in safety_guidance[hazard]:
        st.write(f"✅ {step}")

    st.error(
        "If an immediate danger is present, stop the affected work, "
        "keep people away, and notify the site safety supervisor."
    )

# ---------------- PROJECT PLANNING ----------------

elif page == "Project Planning":

    st.subheader("📋 Basic Construction Project Planner")

    project_name = st.text_input(
        "Project Name",
        placeholder="Example: Residential Building"
    )

    start_date = st.date_input(
        "Project Start Date",
        value=date.today()
    )

    project_type = st.selectbox(
        "Project Type",
        [
            "Residential Building",
            "Commercial Building",
            "Road Construction",
            "Renovation"
        ]
    )

    duration = st.number_input(
        "Estimated Duration (days)",
        min_value=1,
        max_value=3000,
        value=180
    )

    if st.button("Generate Basic Project Plan"):

        from datetime import timedelta

        end_date = start_date + timedelta(days=int(duration))

        if not project_name.strip():
            st.error("Please enter a project name.")

        else:
            st.success("Basic project plan generated.")

            st.write(f"**Project:** {project_name}")
            st.write(f"**Type:** {project_type}")
            st.write(f"**Start Date:** {start_date}")
            st.write(f"**Estimated Completion:** {end_date}")
            st.write(f"**Duration:** {duration} days")

            st.subheader("Suggested Project Stages")

            stages = [
                ("Site Survey and Preparation", 10),
                ("Foundation Work", 20),
                ("Structural Work", 30),
                ("Masonry and Roofing", 20),
                ("Electrical and Plumbing", 10),
                ("Finishing and Inspection", 10)
            ]

            total = sum(days for _, days in stages)

            for stage, percentage in stages:
                stage_days = round(duration * percentage / total)
                st.write(f"• {stage}: approximately {stage_days} days")

            st.caption(
                "These are illustrative estimates, not an engineered schedule. "
                "Actual durations depend on project conditions, resources, "
                "approvals, and dependencies."
            )

# ---------------- COST ESTIMATION ----------------

elif page == "Cost Estimation":

    st.subheader("💰 Construction Cost Estimator")

    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input(
            "Construction Area (square feet)",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

    with col2:
        rate = st.number_input(
            "Estimated Cost per Square Foot (₹)",
            min_value=0.0,
            value=1800.0,
            step=100.0
        )

    contingency = st.slider(
        "Contingency Allowance (%)",
        min_value=0,
        max_value=30,
        value=10
    )

    if st.button("Calculate Estimated Cost"):

        if area <= 0 or rate <= 0:
            st.error("Enter an area and rate greater than zero.")

        else:
            base_cost = area * rate
            contingency_cost = base_cost * contingency / 100
            total_cost = base_cost + contingency_cost

            col1, col2, col3 = st.columns(3)

            col1.metric("Base Cost", f"₹{base_cost:,.2f}")
            col2.metric(
                "Contingency",
                f"₹{contingency_cost:,.2f}"
            )
            col3.metric("Total Estimate", f"₹{total_cost:,.2f}")

            st.caption(
                "This is a preliminary estimate. It excludes any items "
                "not represented by the input rate and is not a professional "
                "quotation or property valuation."
            )

# ---------------- AI CONSTRUCTION ASSISTANT ----------------

elif page == "AI Construction Assistant":

    st.subheader("🤖 Construction Knowledge Assistant")

    st.write(
        "Ask a general construction question. This prototype uses "
        "a small built-in knowledge base rather than a live AI model."
    )

    question = st.text_input(
        "Enter your question",
        placeholder="Example: What is a building foundation?"
    )

    if st.button("Get Answer"):

        if not question.strip():
            st.warning("Please enter a question.")

        else:
            q = question.lower()

            if "foundation" in q:
                answer = (
                    "A foundation transfers building loads to the ground. "
                    "Its design depends on soil conditions, structural loads, "
                    "groundwater, and applicable building codes. "
                    "A qualified structural or geotechnical engineer should "
                    "determine the suitable foundation."
                )

            elif "concrete" in q:
                answer = (
                    "Concrete is made from cementitious materials, water, "
                    "and aggregates. Its strength and durability depend on "
                    "mix design, placement, compaction, and curing."
                )

            elif "crack" in q:
                answer = (
                    "Cracks can have different causes, including shrinkage, "
                    "temperature changes, settlement, or structural movement. "
                    "Do not judge structural safety from a photograph alone. "
                    "Have significant, widening, or concerning cracks "
                    "assessed by a qualified professional."
                )

            elif "safety" in q or "helmet" in q:
                answer = (
                    "Follow the construction site's risk assessment, "
                    "approved safety procedures, and PPE requirements. "
                    "Report hazards to the site safety supervisor."
                )

            elif "planning" in q or "schedule" in q:
                answer = (
                    "Construction planning includes defining activities, "
                    "durations, dependencies, resources, milestones, "
                    "risks, and inspection points. Review the schedule "
                    "regularly as site conditions change."
                )

            elif "cost" in q or "estimate" in q:
                answer = (
                    "A preliminary construction estimate can use area "
                    "multiplied by an appropriate local rate. A more "
                    "reliable estimate also considers quantities, materials, "
                    "labour, equipment, location, taxes, and contingencies."
                )

            else:
                answer = (
                    "This prototype does not have a prepared answer for "
                    "that question. A multimodal language model and a "
                    "verified construction knowledge base can be integrated "
                    "to support broader questions."
                )

            st.info(answer)

# ---------------- ABOUT PROJECT ----------------

elif page == "About Project":

    st.subheader("📘 About the Project")

    st.write("""
    **AI-Powered Multimodal Construction Intelligence Platform**

    This final-year project aims to support construction planning,
    execution, and monitoring through a unified software platform.

    **Main objectives:**
    - Review construction-site images.
    - Provide general construction safety guidance.
    - Estimate preliminary construction costs.
    - Generate basic construction project plans.
    - Answer common construction knowledge questions.
    - Provide a foundation for integrating multimodal AI.
    """)

    st.subheader("Technology Stack")

    st.write("""
    - Frontend prototype: Streamlit
    - Programming language: Python
    - Image handling: Pillow
    - Future full-stack frontend: React.js
    - Future backend API: FastAPI
    - Future AI integration: Multimodal language model
    """)

    st.warning(
        "This single-file version is a functional prototype, not the "
        "complete AI system described in the project brief. Real crack "
        "detection, automated safety detection, real estate valuation, "
        "live weather integration, and multimodal AI require additional "
        "models, data, APIs, and validation."
    )

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Construction Intelligence Platform | Academic Prototype"
)