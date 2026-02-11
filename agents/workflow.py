from langgraph.graph import StateGraph, END,START
from typing import TypedDict
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
import ollama

from .cover_letter_agent import CoverAgent
from .resume_summary_agent import SummaryAgent


class ChainState(TypedDict):
    job_description: str
    resume_summary: str
    cover_letter: str


class AgentWorkflow:

    def __init__(self):

        #initialize all agents
        self.cover_agent = CoverAgent()
        self.summary_agent = SummaryAgent()
        #initial workflow by building and compiling it.
        self.compiled_workflow = self.build_workflow()
        
    # build and compile workflow
    def build_workflow(self):
       
        workflow = StateGraph(ChainState)

        workflow.add_node("resume_summary_node", self._create_resume_summary_agent)

        workflow.add_node("cover_letter_node", self._create_cover_letter_agent)

        #edge to connect resume_summary_node and cover_letter_node
        workflow.add_edge("resume_summary_node", "cover_letter_node")

        #set entry point to resume_summary_state
        workflow.set_entry_point("resume_summary_node")

        workflow.set_finish_point("cover_letter_node")
        
        return workflow.compile()

    
    # Execute workflow given user query to complete agent task
    def execute_pipeline(self, user_query: str):

        #initialize Agent state with user query (job description)
        initial_state = ChainState(
            job_description = user_query,
            resume_summary="",
            cover_letter=""
        )

        try:

            final_response = self.compiled_workflow.invoke(initial_state)

            return {
                "cover_letter": final_response['cover_letter']
            }

        except Exception as e:
            print(f"Workflow execution failed: {e}")
            raise

    #Wrapper for resume_summary Agent node
    def _create_resume_summary_agent(self, state) -> ChainState:
        summary_response = self.summary_agent.generate_resume_summary(state)

        return {**state, "resume_summary":summary_response['resume_summary']}
    
    # Wrapper for cover letter Agent node
    def _create_cover_letter_agent(self, state):

        cover_letter_response = self.cover_agent.generate_cover_letter(state)

        return {**state, "cover_letter": cover_letter_response["cover_letter"]}


if __name__ == "__main__":

    input_state = "We are looking for a data scientist with experience in machine learning, NLP, and Python. Prior work with large datasets and experience deploying models into production is required."

    agent_app = AgentWorkflow()

    result = agent_app.execute_pipeline(input_state)

    print(result)

