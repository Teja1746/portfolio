import streamlit as st


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Tejaswini | Portfolio",
    page_icon="✨",
    layout="wide"
)


# --------------------------------------------------
# Custom styles
# --------------------------------------------------

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        max-width: 1100px;
    }

    .hero {
        background: linear-gradient(135deg, #6C63FF 0%, #00C9A7 100%);
        border-radius: 20px;
        padding: 2.4rem 2.6rem;
        color: #FFFFFF;
        margin-bottom: 1.4rem;
    }

    .hero h1 {
        color: #FFFFFF;
        margin: 0 0 0.3rem 0;
        font-size: 2.4rem;
    }

    .hero p {
        color: #F2F5FF;
        margin: 0.3rem 0 0 0;
        font-size: 1.05rem;
    }

    .pill {
        display: inline-block;
        background: rgba(255, 255, 255, 0.18);
        border: 1px solid rgba(255, 255, 255, 0.35);
        color: #FFFFFF;
        border-radius: 999px;
        padding: 0.3rem 0.9rem;
        margin: 0.5rem 0.5rem 0 0;
        font-size: 0.9rem;
    }

    .card {
        background: var(--secondary-background-color);
        border: 1px solid rgba(120, 120, 140, 0.35);
        border-radius: 14px;
        padding: 1.1rem 1.2rem;
        margin: 0.4rem 0 1rem 0;
        height: 100%;
    }

    .card h4 {
        margin-top: 0;
    }

    .card p,
    .card li {
        color: var(--text-color);
        font-size: 0.95rem;
    }

    .skill-pill {
        display: inline-block;
        background: var(--primary-color);
        color: #FFFFFF;
        border-radius: 8px;
        padding: 0.35rem 0.85rem;
        margin: 0.3rem 0.4rem 0 0;
        font-size: 0.9rem;
    }

    .avatar {
        width: 84px;
        height: 84px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6C63FF 0%, #00C9A7 100%);
        color: #FFFFFF;
        font-size: 2.2rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 0.7rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Profile data
# --------------------------------------------------

PROFILE = {
    "name": "Tejaswini",
    "tagline": "AI Developer, TSPARK AI Development Team",
    "location": "Hyderabad, India",
    "gitlab_handle": "teja1746",
    "gitlab_url": "https://gitlab.com/teja1746",
    "education": "B.Tech in Electronics & Communication Engineering",
}

SKILLS = [
    (
        "Artificial Intelligence",
        85,
        "Building AI-powered applications, working with machine "
        "learning models and intelligent workflows."
    ),
    (
        "Networking",
        80,
        "Strong fundamentals in network protocols, architecture "
        "and infrastructure."
    ),
]

TOOLS = ["Python", "Streamlit", "GitLab"]

EXPERIENCE = [
    {
        "role": "AI Developer",
        "company": "TSPARK",
        "team": "AI Development Team",
        "points": [
            "Developing AI-powered applications and features "
            "as part of the AI development team.",
            "Working with machine learning and NLP workflows "
            "to turn ideas into working products.",
            "Collaborating with the team on design, testing "
            "and delivery of AI solutions.",
        ],
    }
]

HOBBIES = [
    (
        "📚",
        "Reading Books",
        "Reading keeps me curious and continuously learning — "
        "from technology and AI to everything in between."
    ),
    (
        "🚶‍♀️",
        "Walking",
        "Daily walks help me clear my mind, stay active and "
        "come back to problems with fresh ideas."
    ),
]


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="avatar">T</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"**{PROFILE['name']}**")
    st.caption(PROFILE["tagline"])
    st.caption(f"📍 {PROFILE['location']}")

    st.markdown("")

    st.link_button(
        "🔗 GitLab Profile",
        PROFILE["gitlab_url"],
        use_container_width=True
    )

    st.markdown("")

    st.divider()

    st.caption(
        "Passionate about AI, technology and continuous learning."
    )


# --------------------------------------------------
# Hero section
# --------------------------------------------------

st.markdown(
    f"""
    <div class="hero">
        <h1>Hi, I'm {PROFILE['name']} 👋</h1>
        <p>{PROFILE['tagline']}</p>
        <p>
            B.Tech (ECE) graduate building intelligent applications
            at TSpark. Based in {PROFILE['location']}.
        </p>
        <span class="pill">🤖 Artificial Intelligence</span>
        <span class="pill">🌐 Networking</span>
        <span class="pill">📍 Hyderabad</span>
        <span class="pill">🎓 B.Tech ECE</span>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Navigation tabs
# --------------------------------------------------

tab_about, tab_skills, tab_experience, tab_education, tab_hobbies, tab_contact = st.tabs(
    [
        "👤 About",
        "💡 Skills",
        "💼 Experience",
        "🎓 Education",
        "🌿 Hobbies",
        "📮 Contact",
    ]
)


# -----------------
# About
# -----------------

with tab_about:

    st.subheader("👤 About Me")

    st.write(
        f"""
        I'm **{PROFILE['name']}**, an AI developer working with the
        **AI Development Team at TSPARK**. I hold a
        **{PROFILE['education']}** degree, which gave me a strong
        foundation in both electronics and computing, and I currently
        focus on building intelligent, AI-powered applications.

        I'm based in **{PROFILE['location']}**, and outside of work
        you'll usually find me **reading a book** or out on a
        **long walk**.
        """
    )

    st.subheader("⚡ Quick Facts")

    fact_1, fact_2, fact_3, fact_4 = st.columns(4)

    with fact_1:
        st.metric("📍 Location", "Hyderabad")

    with fact_2:
        st.metric("💼 Company", "TSPARK")

    with fact_3:
        st.metric("🎓 Degree", "B.Tech ECE")

    with fact_4:
        st.metric("🎯 Focus", "AI")


# -----------------
# Skills
# -----------------

with tab_skills:

    st.subheader("💡 Skills")

    for name, level, description in SKILLS:

        st.markdown(f"**{name}** — `{level}%`")
        st.progress(level / 100)
        st.caption(description)
        st.markdown("")

    st.subheader("🧰 Tools I Work With")

    st.markdown(
        " ".join(
            f'<span class="skill-pill">{tool}</span>'
            for tool in TOOLS
        ),
        unsafe_allow_html=True
    )


# -----------------
# Experience
# -----------------

with tab_experience:

    st.subheader("💼 Work Experience")

    for job in EXPERIENCE:

        st.markdown(
            f"""
            <div class="card">
                <h4>{job['role']} · {job['company']}</h4>
                <p><em>{job['team']}</em></p>
                <ul>
                    <li>{job['points'][0]}</li>
                    <li>{job['points'][1]}</li>
                    <li>{job['points'][2]}</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )


# -----------------
# Education
# -----------------

with tab_education:

    st.subheader("🎓 Education")

    st.markdown(
        f"""
        <div class="card">
            <h4>{PROFILE['education']}</h4>
            <p>
                A strong foundation in electronics, communication
                and computing — the base for my work in AI
                development today.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------
# Hobbies
# -----------------

with tab_hobbies:

    st.subheader("🌿 Hobbies")

    hobby_columns = st.columns(len(HOBBIES))

    for column, (icon, title, description) in zip(
        hobby_columns, HOBBIES
    ):

        with column:
            st.markdown(
                f"""
                <div class="card">
                    <h4>{icon} {title}</h4>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


# -----------------
# Contact
# -----------------

with tab_contact:

    st.subheader("📮 Contact")

    st.write(
        "The best way to reach me is through my GitLab profile. "
        f"I'm currently based in **{PROFILE['location']}**."
    )

    contact_1, contact_2 = st.columns(2)

    with contact_1:
        st.link_button(
            f"🔗 gitlab.com/{PROFILE['gitlab_handle']}",
            PROFILE["gitlab_url"],
            use_container_width=True
        )

    with contact_2:
        st.markdown(
            f"""
            <div class="card">
                <h4>📍 Location</h4>
                <p>{PROFILE['location']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    f"© 2026 {PROFILE['name']} · Built with Streamlit "
    "💙"
)
