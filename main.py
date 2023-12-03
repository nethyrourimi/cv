# Create a dictionary to store the applicant's information
applicant = {
    "name": "Mohamed Nethir Eloureyemmi",
    "date_of_birth": "14/04/02",
    "marital_status": "Single",
    "address": "03 street of environment kalaa sghira sousse 4021",
    "education": {
        "degree": "Bachelor of Science in Information Technology",
        "expected_graduation": "2024",
        "institution": "University of Sousse, Sousse, Tunisia"
    },
    "technical_skills": {
        "programming_languages": ["Python", "R"],
        "nlp_frameworks": ["SpaCy", "NLTK", "TensorFlow"],
        "machine_learning_algorithms": ["Classification", "Regression", "Clustering"],
        "statistical_analysis": ["Data Visualization", "Hypothesis Testing", "Regression Analysis"]
    },
    "writing_skills": [
        "Excellent written and verbal communication skills",
        "Ability to simplify complex technical concepts for a non-technical audience",
        "Experience writing various forms of technical content, including blogs, articles, how-to guides, and tutorials"
    ],
    "additional_skills": [
        "Proficient in Microsoft Office Suite",
        "Strong problem-solving and analytical skills",
        "Ability to work independently and as part of a team",
        "Excellent time management skills"
    ],
    "projects": [
        "Developed a Python script to classify customer sentiment from Twitter data",
        "Created a how-to guide on using SpaCy for NLP tasks",
        "Wrote a blog article on the latest trends in NLP"
    ],
    "languages": {
        "Arabic": "Native",
        "English": "Advanced",
        "French": "Intermediate",
        "Spanish": "Basic"
    },
    "interests": {
        "sports": "Football",
        "entertainment": "Watching series"
    }
}

# Print the applicant's information in a formatted way
print("**Mohamed Nethir Eloureyemmi**")
print("**Technical Content Writer**")
print("**Contact Information**")
print("Address:", applicant["address"])
print("Email:", "barcanethir@email.com")
print("Phone Number:", "+216 29 118 181")
print("\n**Education**")
print(applicant["education"]["degree"])
print(applicant["education"]["expected_graduation"])
print(applicant["education"]["institution"])
print("\n**Technical Skills**")
print("Programming Languages:", ", ".join(applicant["technical_skills"]["programming_languages"]))
print("NLP Frameworks:", ", ".join(applicant["technical_skills"]["nlp_frameworks"]))
print("Machine Learning Algorithms:", ", ".join(applicant["technical_skills"]["machine_learning_algorithms"]))
print("Statistical Analysis:", ", ".join(applicant["technical_skills"]["statistical_analysis"]))
print("\n**Writing Skills**")
for skill in applicant["writing_skills"]:
    print("-", skill)
print("\n**Additional Skills**")
for skill in applicant["additional_skills"]:
    print("-", skill)
print("\n**Projects**")
for project in applicant["projects"]:
    print("-", project)
print("\n**Languages**")
for language, proficiency in applicant["languages"].items():
    print("-", language, ":", proficiency)
print("\n**Interests**")
print("-", applicant["interests"]["sports"])
print("-", applicant["interests"]["entertainment"])