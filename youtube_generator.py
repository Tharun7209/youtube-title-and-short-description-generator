from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials
creds = Credentials(
    api_key="21pxDV9GEsY2oQ2DF0V-I-4FpN_-7DBOCdoIyC-1SESu",  # Replace if needed
    url="https://us-south.ml.cloud.ibm.com"
)
model = ModelInference(
    model_id="mistralai/mistral-small-3-1-24b-instruct-2503",  # Instruction model
    credentials=creds,
    project_id="5e4a6471-5bd2-4f7a-aa45-e4e80ced637b"
)
topic_input = input(" Enter your YouTube video topic or idea:\n")

# Step 4: Title generation prompt
title_prompt = f'''
You are a YouTube assistant. Generate a catchy YouTube video title (in double quotes, under 100 characters)
based on the following topic:

\"\"\"{topic_input}\"\"\"

Title:
'''

desc_prompt = f'''
You are a professional YouTube content assistant.

Your task is to write a short (2–3 sentence), SEO-optimized YouTube video **description** only. Do NOT write a video script.

 Description must:
- Hook the viewer
- Use relevant keywords
- Be complete (no cutoff)
- Be followed by ---END---

Examples:

Topic: AI in Education  
Description: Discover how artificial intelligence is transforming the classroom. From smart tutors to personalized learning, this video explores how AI is reshaping education. ---END---

Topic: Fun Space Facts  
Description: Explore incredible facts about space, planets, and black holes. Learn how the universe works in ways that will amaze you. ---END---

Now write a description for:
\"\"\"{topic_input}\"\"\"

Description:
'''

title_response = model.generate_text(title_prompt)
desc_response = model.generate_text(desc_prompt)

if "---END---" in desc_response:
    desc_clean = desc_response.split("---END---")[0].strip()
else:
    desc_clean = desc_response.strip()

print("\n Final Output:\n")
print(title_response.strip())
print(desc_clean)
