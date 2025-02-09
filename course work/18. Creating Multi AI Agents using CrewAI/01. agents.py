from crewai import Agent


# create a senior blog content researcher
blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get the relevent video content for the topic {topic} from Yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and Gen AI and providing suggestions."
    ),
    tool=[],
    allow_delegation=True
)

# creating a senior blog writer agent with YT tool
blog_writer = Agent(
    role = "Blog Writer",
    goal = "Narrate compelling tech stories about the video {topic} from YT channel",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools = [],
    allow_delegation = False
)