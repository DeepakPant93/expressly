#!/usr/bin/env python
import sys
import warnings

from expressly_server.crew import ExpresslyServer
import dotenv

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

dotenv.load_dotenv()


def run():
    """
    Run the crew.
    """
    # inputs = {
    #     "context": "I want to thanks DeepLearning and John from the crewAI for this amazing course..",
    #     "format": {
    #         "name": "Chat",
    #         "description": "A conversational and interactive response that mimics real-time messaging. It focuses on direct, clear, and natural communication with a friendly tone.",
    #         "max_length": 200,
    #         "negative": "Do not use overly formal language, complex sentence structures, or impersonal tones. Avoid too much technical information and hashtags.",
    #     },
    #     "tone": {
    #         "name": "Friendly",
    #         "description": "Warm and approachable, making the user feel comfortable.",
    #     },
    #     "target_audience": {
    #         "name": "WhatsApp Message",
    #         "description": "Casual or semi-formal communication meant for direct, personal messaging. Used for sending quick updates, reminders, or messages to small groups, often informal in tone.",
    #         "ideal_audience": "Friends, family, small teams, personal contacts, colleagues in a more relaxed setting",
    #     },
    # }

    inputs = {
        'prompt': "I want to thanks DeepLearning and John from the crewAI for this amazing course..",
        'format': "Chat",
        'tone': "Friendly",
        'target_audience': "LinkedIn Post",
        'active_tab': "target_audience"
    }


    ExpresslyServer().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        ExpresslyServer().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ExpresslyServer().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        ExpresslyServer().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
