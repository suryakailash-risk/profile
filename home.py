import streamlit as st
# Projects Page
from datetime import datetime
# from st_pages import Page, show_pages, add_page_title
# Top navigation buttons using HTML + query string
import streamlit as st
from datetime import datetime

# Set up page config
st.set_page_config(page_title="Suryakailash | Portfolio", page_icon="🧠", layout="wide")

# Top navbar
st.markdown("""
    <style>
        .top-nav {
            display: flex;
            justify-content: center;
            gap: 20px;
            background-color: #0e1117;
            padding: 12px;
            position: sticky;
            top: 0;
            z-index: 999;
        }
        .top-nav a {
            color: white;
            text-decoration: none;
            padding: 6px 16px;
            border-radius: 8px;
            background-color: #262730;
            font-weight: 500;
        }
        .top-nav a:hover {
            background-color: #007ACC;
        }
    </style>
    <div class="top-nav">
        <a href="/?page=home">🏠 Home</a>
        <a href="/?page=projects">📂 Projects</a>
        <a href="/?page=experinces">📂 experinces</a>
        <a href="/?page=skills">🧰 Skills</a>
        <a href="/?page=certifications">🏅 Certifications</a>
        <a href="/?page=resume">📄 Resume</a>
        <a href="/?page=contact">📬 Contact</a>
    </div>
""", unsafe_allow_html=True)

# Determine selected page
page = st.query_params.get("page", "home")


# Home Page
if page == "home":
    # Background gradient and centered greeting
    st.markdown("""
        <style>
        .hero {
            text-align: center;
            padding: 60px 30px 30px;
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            border-radius: 12px;
            margin-bottom: 40px;
            color: white;
        }
        .hero h1 {
            font-size: 42px;
            margin-bottom: 10px;
        }
        .hero h3 {
            font-weight: 400;
            color: #cccccc;
        }
        .profile-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 30px;
            backdrop-filter: blur(8px);
            text-align: center;
            margin: auto;
            width: 80%;
            max-width: 700px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        }
        .specialties {
            display: flex;
            justify-content: space-around;
            margin-top: 40px;
            gap: 20px;
            flex-wrap: wrap;
        }
        .specialty-box {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            width: 220px;
            text-align: center;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
            transition: transform 0.2s ease;
        }
        .specialty-box:hover {
            transform: translateY(-6px);
        }
        .specialty-box p {
            color: #aaa;
            margin-top: 10px;
            font-size: 14px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="hero">
            <h1>Hi, I'm <span style='color:#66d9ef;'>Suryakailash</span> 👨‍💻</h1>
            <h3>A Data Scientist passionate about ML, AI, and storytelling with data.</h3>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="profile-card">
            <img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="100%" style="border-radius: 10px; margin-bottom: 20px;" />
            <p style="color: #ccc; font-size: 15px;">Welcome to my portfolio. I love transforming raw data into impactful insights and building AI-powered solutions that make lives easier.</p>
        </div>
    """, unsafe_allow_html=True)

    # Specialties
    st.markdown("### 🔍 What I Do", unsafe_allow_html=True)
    st.markdown("""
        <div class="specialties">
            <div class="specialty-box">
                <img src="https://cdn-icons-png.flaticon.com/512/1087/1087815.png" width="48" />
                <p><strong>Predictive Modeling</strong><br>ML pipelines, evaluation, and deployment</p>
            </div>
            <div class="specialty-box">
                <img src="https://cdn-icons-png.flaticon.com/512/3466/3466798.png" width="48" />
                <p><strong>Data Visualization</strong><br>Dashboards with Tableau, Streamlit</p>
            </div>
            <div class="specialty-box">
                <img src="https://cdn-icons-png.flaticon.com/512/2721/2721298.png" width="48" />
                <p><strong>Cloud Platforms</strong><br>Deployments on Azure, GCP, Cloudinary</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif page == "projects":
    st.markdown("<h2 style='text-align:center;'>🚀 Explore My Projects</h2>", unsafe_allow_html=True)

    projects = {
        "🧠 AI-Powered Video Captioning": {
            "desc": "Generate smart captions for videos using NLP and computer vision.",
            "page": "Video_Captioning",
            "img": "https://cdn-icons-png.flaticon.com/512/3466/3466798.png",
            "date": "2025-06-10",
            "tags": ["#AI", "#NLP", "#ComputerVision"]
        },
        "📍 Seattle Crime Mapping": {
            "desc": "Visualize and analyze crime data spatially in Seattle.",
            "page": "Crime_Mapping",
            "img": "https://cdn-icons-png.flaticon.com/512/684/684908.png",
            "date": "2025-05-05",
            "tags": ["#GIS", "#CrimeAnalysis", "#Visualization"]
        },
        "🧪 Youth Drug Use Prediction": {
            "desc": "Predict youth drug behavior using classification models.",
            "page": "Youth_Drug_Use",
            "img": "https://cdn-icons-png.flaticon.com/512/2920/2920216.png",
            "date": "2025-04-18",
            "tags": ["#Health", "#ML", "#Classification"]
        },
        "📈 CO2 Emissions Forecasting": {
            "desc": "Forecast carbon emissions trends using time series modeling.",
            "page": "CO2_Emissions",
            "img": "https://cdn-icons-png.flaticon.com/512/2903/2903482.png",
            "date": "2025-03-15",
            "tags": ["#Forecasting", "#Climate", "#TimeSeries"]
        }
    }

    # Filter Controls
    col1, col2, col3 = st.columns([2, 2, 3])

    with col1:
        all_tags = sorted({tag for p in projects.values() for tag in p["tags"]})
        selected_tag = st.selectbox("🎯 Filter by Tag", ["All"] + all_tags)

    with col2:
        date_range = st.date_input("📅 Filter by Date", [datetime(2025, 1, 1), datetime(2025, 12, 31)])

    with col3:
        search_query = st.text_input("🔍 Search Projects", "").lower()

    start_date = date_range[0]
    end_date = date_range[1]

    def match(project):
        title, info = project
        project_date = datetime.strptime(info["date"], "%Y-%m-%d").date()
        match_text = search_query in title.lower()
        match_tag = selected_tag == "All" or selected_tag in info["tags"]
        match_date = start_date <= project_date <= end_date
        return match_text and match_tag and match_date

    filtered = dict(filter(match, projects.items()))

    if not filtered:
        st.warning("No matching projects found.")
    else:
        cols = st.columns(2)
        for i, (title, info) in enumerate(filtered.items()):
            with cols[i % 2]:
                tags_html = " ".join([
                    f"<span style='background:#444;padding:3px 8px;border-radius:6px;margin-right:5px;font-size:12px;'>{tag}</span>"
                    for tag in info["tags"]
                ])
                st.markdown(f"""
                    <div style='
                        background-color: #1e1e1e;
                        padding: 20px;
                        border-radius: 12px;
                        margin-bottom: 25px;
                        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
                        display: flex;
                        flex-direction: column;
                        align-items: flex-start;
                    '>
                        <img src='{info["img"]}' width='100' style='border-radius: 8px; object-fit: contain; margin-bottom: 10px;' />
                        <h4 style='margin-bottom: 5px;'>{title}</h4>
                        <p style='color: #aaaaaa; font-size: 14px; margin: 5px 0;'>{info["desc"]}</p>
                        <p style='font-size: 12px; color: #888;'>📅 {datetime.strptime(info["date"], "%Y-%m-%d").strftime("%B %d, %Y")}</p>
                        <div style="margin: 8px 0;">{tags_html}</div>
                        <a href='/{info["page"]}' target='_self'>
                            <button style='
                                background-color: #007ACC;
                                color: white;
                                padding: 8px 18px;
                                font-size: 14px;
                                border: none;
                                border-radius: 6px;
                                cursor: pointer;
                                margin-top: 8px;
                            '>
                                🔎 Know More
                            </button>
                        </a>
                    </div>
                """, unsafe_allow_html=True)

# Resume Page
elif page == "resume":
    st.markdown("## 📄 My Resume")
    st.markdown("[🔗 View My Resume](https://example.com/resume.pdf)", unsafe_allow_html=True)
elif page == "experinces":

    experiences = [
        {
            "company": "NVIT",
            "logo": "https://cdn-icons-png.flaticon.com/512/1183/1183672.png",
            "role": "Full-Stack Software Engineer Intern",
            "period": "Jan 2025 – Present",
            "desc": "Developed AI-powered media tools using React, Node.js, and Cloudinary. Integrated GenAI features like video captioning and thumbnail generation.",
        },
        {
            "company": "Cognizant",
            "logo": "https://cdn-icons-png.flaticon.com/512/732/732221.png",
            "role": "Programmer Analyst",
            "period": "Jul 2021 – Aug 2023",
            "desc": "Built scalable data pipelines and automated reporting tools using SQL, Python, and Tableau for global retail clients.",
        },
        {
            "company": "UT Arlington",
            "logo": "https://cdn-icons-png.flaticon.com/512/1973/1973867.png",
            "role": "MS in Computer Science",
            "period": "Aug 2023 – May 2025",
            "desc": "Specialized in AI/ML, cloud-native apps, and system design. GPA: 3.9/4.0.",
        }
    ]

    for exp in experiences:
        st.markdown(f"""
            <div style="display: flex; gap: 20px; align-items: flex-start; margin-bottom: 30px;">
                <img src="{exp['logo']}" width="60" style="border-radius: 8px; margin-top: 5px;" />
                <div>
                    <h4 style="margin-bottom: 4px;">{exp['role']} @ {exp['company']}</h4>
                    <p style="margin: 0; color: #888;">📅 {exp['period']}</p>
                    <p style="margin-top: 5px;">{exp['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
elif page == "skills":
    st.markdown("## 🧰 My Skillset")
    st.markdown("Explore the tools and technologies I use across data science, software engineering, and storytelling.")

    def render_skill_row(skills):
        cols = st.columns(4)  # 4 per row
        for col, skill in zip(cols, skills):
            with col:
                st.markdown(f"""
                    <div title="{skill['desc']} ({skill['level']}% proficient)"
                        style='
                            background-color: #1e1e1e;
                            border-radius: 12px;
                            padding: 20px;
                            text-align: center;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
                            transition: transform 0.2s ease;
                            cursor: help;
                        '
                        onmouseover="this.style.transform='translateY(-5px)'"
                        onmouseout="this.style.transform='none'">
                        <img src="{skill['icon']}" width="40" style="margin-bottom: 10px;" />
                        <p style="color: white; font-weight: 500; margin: 0;">{skill['name']}</p>
                    </div>
                """, unsafe_allow_html=True)

    # === Sections ===
    st.markdown("### 🧠 Core Skills")
    render_skill_row([
    {"name": "Python", "icon": "https://cdn-icons-png.flaticon.com/512/5968/5968350.png", "desc": "Used for scripting, ML, APIs", "level": 95},
    {"name": "SQL", "icon": "https://cdn-icons-png.flaticon.com/512/4248/4248443.png", "desc": "Advanced queries, joins, CTEs", "level": 90},
    {"name": "Machine Learning", "icon": "https://cdn-icons-png.flaticon.com/512/1055/1055687.png", "desc": "Modeling and evaluation", "level": 85},
    {"name": "Pandas", "icon": "https://cdn-icons-png.flaticon.com/512/5968/5968520.png", "desc": "Data cleaning & analysis", "level": 92}
])

    render_skill_row([
    {"name": "Streamlit", "icon": "https://cdn-icons-png.flaticon.com/512/5969/5969323.png", "desc": "Interactive Python apps", "level": 90},
    {"name": "GitHub", "icon": "https://cdn-icons-png.flaticon.com/512/733/733553.png", "desc": "Version control & collaboration", "level": 85},
    {"name": "Docker", "icon": "https://cdn-icons-png.flaticon.com/512/919/919853.png", "desc": "Containerization & deployment", "level": 70},
    {"name": "Cloudinary", "icon": "https://res.cloudinary.com/practicaldev/image/fetch/s--gQ_JxZxY--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://thepracticaldev.s3.amazonaws.com/i/knzsab1z7je9eab2klqe.png", "desc": "Media storage & delivery", "level": 80}
])


    st.markdown("### 🛠️ Hands-On Tools")
    render_skill_row([
    {"name": "Streamlit", "icon": "https://cdn-icons-png.flaticon.com/512/5969/5969323.png", "desc": "Interactive Python apps", "level": 90},
    {"name": "GitHub", "icon": "https://cdn-icons-png.flaticon.com/512/733/733553.png", "desc": "Version control & collaboration", "level": 85},
    {"name": "Docker", "icon": "https://cdn-icons-png.flaticon.com/512/919/919853.png", "desc": "Containerization & deployment", "level": 70},
    {"name": "Cloudinary", "icon": "https://res.cloudinary.com/practicaldev/image/fetch/s--gQ_JxZxY--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://thepracticaldev.s3.amazonaws.com/i/knzsab1z7je9eab2klqe.png", "desc": "Media storage & delivery", "level": 80}
])


    st.markdown("### 🎨 Creative & Visualization Skills")
    render_skill_row([
    {"name": "Data Viz", "icon": "https://cdn-icons-png.flaticon.com/512/4150/4150897.png", "desc": "Charts and dashboards", "level": 90},
    {"name": "UI/UX", "icon": "https://cdn-icons-png.flaticon.com/512/2743/2743840.png", "desc": "Designing user interfaces", "level": 75},
    {"name": "Storytelling", "icon": "https://cdn-icons-png.flaticon.com/512/1087/1087815.png", "desc": "Explaining insights clearly", "level": 88},
    {"name": "Tableau", "icon": "https://cdn-icons-png.flaticon.com/512/888/888879.png", "desc": "Interactive dashboards", "level": 80}
])


# Contact Page
elif page == "📬 Contact":
    st.markdown("## 📬 Get In Touch")
    with st.form("contact_form"):
        st.text_input("Your Name")
        st.text_input("Your Email")
        st.text_area("Your Message")
        if st.form_submit_button("📨 Send Message"):
            st.success("✅ Thanks! Your message has been sent.")
