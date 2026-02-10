from transformers import pipeline

print("AI Resume Advisor Starting...")
print("Loading LLM Model..")

llm = pipeline(
    "text-generation",
    model = "gpt2"
)
print("LLM Load Successfully")

print("Testing LLM response...")

response = llm("Say hello and tell who are you:", max_length = 50)
print("LLM response..")
print(response[0]["generated_text"])

print("\n--- Resume & JD Input Step ---")

resume_text = input("\nPaste your RESUME text and press Enter:\n")

jd_text = input("\nPaste the JOB DESCRIPTION text and press Enter:\n")

print("\nResume and Job Description captured successfully")
print("\n--- Building Prompt for LLM ---")

prompt = f"""
You are an AI Career Advisor.

Analyze the following resume against the given job description.

Resume:
{resume_text}

Job Description:
{jd_text}

Provide the analysis in the following format:
1. Overall match assessment
2. Key strengths
3. Missing skills or gaps
4. Suggestions to improve the resume
"""

print("Prompt created successfully")

print("\n--- Sending prompt to LLM ---")

response = llm(prompt, max_length=500)

print("\n===== AI RESUME ANALYSIS =====\n")
print(response[0]["generated_text"])
