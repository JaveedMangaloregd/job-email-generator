import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0,groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-8b-instant" )
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing
            following keys: 'role', 'experience', 'skills' and 'description'.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self,job,links):
        prompt_email = PromptTemplate.from_template(
            """
              ### JOB DESCRIPTION:
              {job_description}
  
              ### INSTRUCTION:
              You are Javeed, an Engineering graduate specializing in Electronics and IoT systems.
              You have developed several real-time automation and embedded projects including:
              - IoT-based forest fire prevention system
              - Automatic door locker system using microcontroller
              - Gas detection and alert system
              - Smart street lighting project using Arduino and sensors
  
              You are skilled in C, C++, Python, and embedded programming, with hands-on experience using
              microcontrollers (AT89C51, ESP32), GSM/GPS modules, temperature and smoke sensors, 
              and real-time system integration. You also possess a solid understanding of 
              software engineering concepts including Data Structures, Algorithms, Database Management Systems (DBMS),
              Operating Systems, and Computer Networks.
  
              Your task is to write a professional cold email to the client regarding the job mentioned above,
              explaining how your technical background, project experience, and software proficiency make you a 
              strong fit for the role. Highlight your ability to apply both hardware and software knowledge to 
              real-world automation and IoT solutions.
  
              Also include the most relevant ones from the following portfolio links: {link_list}
  
              Remember, you are Javeed, an engineering graduate with expertise in IoT, automation, and software development.
              Do not provide a preamble.
  
              ### EMAIL (NO PREAMBLE):
              """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
