# services/llm_manager.py


from services.llm.groq_provider import GroqProvider



class LLMManager:


    def __init__(self):

        self.provider = GroqProvider()



    def generate_response(self, prompt):

        return self.provider.generate(prompt)





llm = LLMManager()