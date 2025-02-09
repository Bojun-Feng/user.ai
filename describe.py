from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="""1. Go to https://password-locker.com/
2. Summarize the main page content
3. Identify one verbose specific audience profile for the tool
 a. Please feel free to be verbose! Give First and Last names, occupation, location, specific job and company, and their daily task on a specific project in their respective field
 b. Also, provide a story on how they wandered upon the website. Potential causes are online ads, word of mouth from collegues or friends
 c. Provide a brief career history of their past 3 years. Please be very specific as if you are coming up with a real world person's autobiography
4. For each profile, pretend that you are the individual. Then, I want you to give REAL and HARSH and DIRECT feedbacks on the main page:
 a. Given your background story, what is your expectation of the tool? What do you expect it to help you in your specific task
 b. Do you understand what EXACTLY it is doing? Please ONLY answer yes if you know exactly how and at where you can apply it in a SPECIFIC workflow of your job or life
 c. What is your first impression of the website? You have VERY LIMITED attention and is likely to only pay <5 seconds of attention to the site. Ignore all details and only focus on large / bolded text or visuals that stand out
 d. Focus specifically on the cons of the website. Be DIRECT and HARSH! Tell me why potentially the site is boring, confusing, unintersting, not applicable to you, or likely a scam.
 e. Give me 5 concrete and specific reasons why you would NOT pay money for this website in any way shape or form.""",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print("\n\n\n\n\n")
    print(result)
    print("\n\n\n\n\n")

asyncio.run(main())
