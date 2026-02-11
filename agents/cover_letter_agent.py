from langgraph.graph import StateGraph, END,START
from typing import TypedDict
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
import ollama


class ChainState(TypedDict):
    job_description: str
    resume_summary: str
    cover_letter: str


class CoverAgent:

    def __init__(self):

        self.model_name = "llama3.2-vision:11b"


    def generate_cover_letter(self, state: ChainState) -> ChainState:

        
        try:

            print("Sending Prompt to LLM....")

            cover_letter_llm = ollama.chat(
                model="llama3.2-vision:11b",

                messages=[
                    {
                        "role": "system",
                        "content": "You're a cover letter writing assistant. Your task is to write a professional and personalized cover letter for a job application."
                    },
                    {
                        "role": "user",
                        "content": f"""Please draft a cover letter for the job description:\n\n {state['job_description']}  using the resume:\n\n{state["resume_summary"]}"""
                    }
                ]
            )

            print("LLM processed prompt and responded successfully")
            

        except Exception as e:
            print(f"Error during model inference: {e}")
            raise RuntimeError("Failed to generate answer due to a model error.") from e
        
        #clean llm response
        llm_response = cover_letter_llm['message']['content'].strip()

        return {"cover_letter": llm_response}





if __name__ == "__main__":

    state = {
    "job_description": "We are looking for a data scientist with experience in machine learning, NLP..", 
    "resume_summary": "Results-driven data scientist with expertise in machine learning...",
    "cover_letter": ""
    }

    coveragent = CoverAgent()

    llm_res = coveragent.generate_cover_letter(state)

    print(llm_res["cover_letter"])