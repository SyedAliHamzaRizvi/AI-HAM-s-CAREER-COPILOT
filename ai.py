import json
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



def analyze_resume(resume_text, user_goal):

    prompt = f"""
You are a senior software engineer and hiring manager.

Evaluate the resume based on the user's goal.

User goal:
{user_goal}

STRICT RULES:
- Extract only relevant skills for this goal
- Remove irrelevant tools
- Identify real skill gaps
- Generate roadmap only for missing skills
- Make output different based on goal

Return only JSON:

{{
"skills":[],
"missing_skills":[],
"roadmap":[],
"interview_questions":[]
}}

Resume:
{resume_text}
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )


        content = response.text.strip()


        start = content.find("{")
        end = content.rfind("}") + 1


        return json.loads(content[start:end])


    except Exception as e:

        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }