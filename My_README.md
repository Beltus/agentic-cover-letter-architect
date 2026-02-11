## SEQUENTIAL DESIGN PATTERN - Mini Project

Sequential design pattern or prompt chain is an AI system design pattern where the output of one LLM serves as the input to the next.
This allows complex tasks to be broken down into a sequence of steps and each step executed before the next. Each step can be an LLM call. 

A good example of this is a typical ML classification life cycle which starts with data collection, annotation, processing, training, evaluation, deployment and inference.

This mini project aims to build a simple Job Application Assistant, that uses this prompt chaining workflow pattern to help job applicants create a customized and personalized cover letter given job description.

## Assumption
1. Applicant has no generic resume. So first, we generate a custom resume that matches the job description. Then use the resume to generate a final cover letter.  

2. We can assume the applicant already has a resume but that resume is not tailored to the specific role. Therefore, the first step could be, to use the applicants generic resume to generate a customed resume that matches the role. Then, this customized resume can be fed into another LLM to generate a final cover letter. This is basically, leveraging RAG. 

Here are the main steps based on Assumption 1:

* Step 1: Generate a custom Resume 
* Step 2: Generate a final draft

More details of each step

## Step 1:
* An LLM will read the **job description** and generate a resume summary that is tailored to the role. This is the first agent. It represents a node in our LangGraph workflow to be developed.

## Step 2:
* The resume summary from the first LLM is then passed as input into the next LLM to generate a cover letter suitable for submitting with a job application. This is the next step in the sequence, and the second agent. It is another node in the workflow.

## Other Details
* How will the data from LLM 1 flow to LLM 2? This is where we must start by defining a state variable of TypedDict which acts as a container or bucket, containing all intermediate and final outputs of the workflow.

For instance, we already know we have 2 LLM, which means 2 outputs. From LLM 1, we get resume summary and from LLM 2 we get final cover letter. So for sure, state must hold these outputs.

Also, to generate the final cover letter for the job application, LLM 2 will need the job description input, so somehow, state should also hold job description so that it can be passed from LLM 1 to LLM 2 or it can be accessed by both LLMs. 


```
class ChainState(TypedDict):
    job_description: str
    resume_summary: str
    cover_letter: str
```


**Note:**

So, when constructing **State** variable, the best and quickest way to think about it is in terms of inputs and outputs from each agent or LLM in your workflow. Once you identify these, you can for sure, see the inputs and outputs that transfer from one node to another through the workflow.





## Notes:

* I need to always seperate front-end from back-end when thinking about the requirements of a system design. 
For instance, For the project above, when I'm thinking about it, I am thinking about what the user will input into the UI.  But, this can be done later.
Instead, I should think about what happens at each step of the sequential pattern, what data is fed into what component and what is the output.

So,
I know, user needs a job. User searches for job vacancies on LinkedIn, and finds a few. User copies the job description and then paste it into the system. 
This is still front-end thinking, but it helps to identify the input data, which is job description which is text. 

The user prompts or instruct an LLM to generate a draft of a cover letter that's tailored to the job description. So there's a user query or prompt

# Initial Input Data
1. Job Description: str - text data


## IDEA: I can do this for scholarship students
* Using the methods I uncovered in my book, we can create amazing personalized letter of intent or statement of purpose. 




