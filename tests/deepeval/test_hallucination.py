# LLM Metrics evaluation for Hallucination


from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric
from app.banking_chatbot import chatbot

def test_hallucination_Metrics():

    # Parameters for LLMTestCase:
    # Input
    # Output
    # Context

    query = "What is the maximum personal loan can customer avail and what are the interest rate and tenure details?"
    output = chatbot(query)
    print(output)
    context = [
        "The maximum loan can be provided as 10L INR.",
        "The rate of interest is 10%",
        "The maximum tenure allowed is 5 years"
    ]

    test_case = LLMTestCase(

        input = query,
        actual_output = output,
        context = context
    )

    hal_metric = HallucinationMetric(threshold=0.9)
    evaluate([test_case],[hal_metric])