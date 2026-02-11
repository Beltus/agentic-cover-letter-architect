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


class SummaryAgent:

    def __init__(self):

        self.model_name = "llama3.2-vision:11b"
        
        print("Model defined")

    def generate_resume_summary(self, state: ChainState) -> ChainState:
        """
        Defines an agent node to generate resume summary. 
        
        """
        try:

            print("Sending Prompt to LLM....")

            resume_llm_response= ollama.chat(
                model=self.model_name,
                messages=[
                {
                    "role": "system", 
                    "content": "You are a professional resume assistant. Your task is to summarize job descriptions from the perspective of a strong applicant's resume summary."
                },
                {
                    "role": "user", 
                    "content": f"Please summarize this job description:\n\n{state['job_description']}"
                }
                ]
                )
            
            print("LLM processed prompt and responded successfully")
        

        except Exception as e:
            print(f"Error during model inference: {e}")
            raise RuntimeError("Failed to generate answer due to a model error.") from e
        

        llm_response = resume_llm_response['message']['content'].strip()

        #return {**state, "resume_summary": llm_response}
        return {"resume_summary": llm_response}

if __name__ == "__main__":

    state_1 = {
        "job_description": "We are looking for passionate Research Scientists to join our core AI pillars. This unified role covers three of our most critical research areas. Depending on your expertise and interest, you will join one of the following teams:Language AI: Building the world's leading translation and text-improvement systems, taking responsibility for the entire model lifecycle from data to deployment. Foundation Model Task Adaptation (FMTA): Shaping how our models learn beyond pre-training. You will focus on RLHF, alignment, and post-training to enable new reasoning and controllability capabilities.",
        "resume_summary": "",
        "cover_letter" : ""
        }

    summary_agent = SummaryAgent()

    res = summary_agent.generate_resume_summary(state_1)

    print(res["resume_summary"])