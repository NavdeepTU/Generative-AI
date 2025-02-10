from crewai import Crew, Process
from agents1 import blog_researcher, blog_writer
from tasks3 import research_task, write_task

# forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential, # optional: Sequential task execution is default
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)

# start the task execution process with enhanced feedback
result = crew.kickoff(inputs={"topic":"Generative AI using LangChain | GENAI for Beginners | CampusX"})
print(result)