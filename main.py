from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

class HybridREFramework:

    def __init__(self):
        self.stakeholders = []
        self.requirements = []

    def stakeholder_analysis(self, scenario):
        prompt = f"""Identify stakeholders from this software project:

{scenario}

Return a stakeholder list.
"""

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    def draft_requirements(self, scenario):
        prompt = f"""Generate functional and non-functional requirements
from the following scenario:

{scenario}
"""

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    def evaluate_requirements(self, requirements):
        rubric = '''
Evaluate using:
- Clarity (1-5)
- Completeness (1-5)
- Consistency (1-5)
- Structure (1-5)
- Stakeholder Relevance (1-5)
'''

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": rubric + requirements}]
        )

        return response.choices[0].message.content


if __name__ == "__main__":
    scenario = "Design an online university course management system."
    framework = HybridREFramework()
    print(framework.stakeholder_analysis(scenario))
