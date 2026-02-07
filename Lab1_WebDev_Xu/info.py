# This file will contain the information to be displayed in your portfolio

# -----------------------
# About Me
# -----------------------
profile_picture = "images/profile.jpg"
about_me = (
    "Hi! I'm Haohan Xu (徐浩涵) from China. "
    "I'm studying Industrial Design at the Georgia Institute of Technology. "
    "I'm interested in human-centered design, product innovation, and visual storytelling. "
    "My current goal is to build a strong portfolio through hands-on projects, "
    "learn more about prototyping and design research, and prepare for an Industrial Design internship."
)

# -----------------------
# Sidebar (optional links/icons)
# -----------------------
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

# 你可以先用占位链接/邮箱，之后再换成自己的
my_linkedin_url = "https://www.linkedin.com"
my_github_url = "https://github.com"
my_email_address = "haohanxu@example.com"

# -----------------------
# Education
# -----------------------
education_data = {
    "Degree": "B.S. in Industrial Design",
    "Institution": "Georgia Institute of Technology",
    "Location": "Atlanta, GA",
    "Graduation Date": "TBD",
    "GPA": "TBD",
}

# 课程表（Portfolio.py 会把它做成 dataframe 展示）
course_data = {
    "code": ["ID 1XXX", "ID 2XXX", "LMC 2XXX", "MATH 1XXX"],
    "names": [
        "Design Foundations",
        "Design Methods & Prototyping",
        "Visual Communication",
        "Math / Quantitative Reasoning",
    ],
    "semester_taken": ["1st", "2nd", "2nd", "1st"],
    "skills": [
        "Sketching, form exploration, basic model making",
        "User research, ideation, rapid prototyping",
        "Layout, storytelling, presentation design",
        "Analytical thinking & problem-solving",
    ],
}

# -----------------------
# Professional Experience / Experience
# (可以是项目/经历/未来目标；每个条目 = (bullet list, image_path))
# -----------------------
experience_data = {
    "Industrial Design Practice (Personal Projects)": (
        [
            "- Built habits of sketching and iterative design (concept → refine → present).",
            "- Focused on usability and aesthetics through simple daily-object redesigns.",
            "- Documented process clearly: research, ideation, prototyping, and feedback."
        ],
        "images/cook.jpg"
    ),
    "Prototyping & Making (Workshop / Self-learning)": (
        [
            "- Practiced rapid prototyping using cardboard/foam/core materials and basic hand tools.",
            "- Explored how materials and structure affect form, strength, and user experience.",
            "- Goal: improve model quality and speed for studio-style projects."
        ],
        "images/cleaner.jpg"
    ),
    "Design Communication (Presentation & Portfolio)": (
        [
            "- Improved visual storytelling: clear hierarchy, consistent layout, and strong captions.",
            "- Learned to explain design decisions with evidence and concise writing.",
            "- Goal: build a polished portfolio ready for internship applications."
        ],
        "images/jelly.jpg"
    ),
}

# -----------------------
# Projects
# -----------------------
projects_data = {
    "Everyday Object Redesign Series": (
        "A mini-series of redesigns focusing on comfort, usability, and aesthetics. "
        "Includes sketches, concept iterations, and final presentation boards."
    ),
    "Prototype Sprint: One-Week Build": (
        "A fast-paced prototyping challenge to turn an idea into a physical model quickly, "
        "testing form factors and improving based on feedback."
    ),
}

# -----------------------
# Skills
# -----------------------
programming_data = {
    "Python": 55,
    "Java": 35,
    "C": 25,
}

programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🔧",
}

spoken_icons = {
    "Chinese": "🇨🇳",
    "English": "🇺🇸",
}

spoken_data = {
    "Chinese": "Native",
    "English": "Fluent",
}

# -----------------------
# Activities
# -----------------------
leadership_data = {
    "Design Growth Plan (This Semester)": (
        [
            "- Complete 2–3 portfolio-ready projects with clear process documentation.",
            "- Improve prototyping speed and craft quality through weekly practice.",
            "- Seek critique/feedback and iterate based on user needs."
        ],
        "images/puff.jpg"
    ),
}

activity_data = {
    "Community & Personal Interests": [
        "- Interested in product design, visual design, and creative making.",
        "- Enjoy exploring design inspiration, photography, and storytelling.",
    ]
}
