from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()


def define_maths_concept(topic):
    llm = OpenAI(temperature=0.3)

    prompt_template = PromptTemplate(
        input_variables=["topic"],
        template="explain the following topic to a senior high school student: {topic}"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="topic") ##  name_chain is expecting a dictionary (below)

    return name_chain({"topic": topic}) ## Here, name_chain is called with a dictionary {"equation": equation}. This dictionary is providing the actual value for the equation variable that was specified in the prompt template.


def langchain_agent(topic):
    llm= OpenAI(temperature=0.3)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent.run(topic)

    return result

if __name__ == "__main__":
    print(define_maths_concept(topic))
    #print(define_maths_concept("calculus"))
