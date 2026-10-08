# Implementation of Correctness using deepeval

from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase, SingleTurnParams
from deepeval.metrics import GEval
from app.banking_chatbot import chatbot

def test_correctness_metrics():

    query = "How to apply for a personal loan?"
    response = chatbot(query)
    expected_output = """you can apply personal loan through online banking or
    you can connect with the bank or customer support team"""

    test_case = LLMTestCase(

        input = query,
        actual_output = response,
        expected_output = expected_output
    )
    correctness = GEval(

        name = "Correctness",
        criteria = "Check if the answer is factually and logically correct or not",
        evaluation_params=[
            SingleTurnParams.INPUT,
            SingleTurnParams.ACTUAL_OUTPUT,
            SingleTurnParams.EXPECTED_OUTPUT
        ],

        evaluation_steps=[

            "Check if the output is as per the query",
            "Check the accuracy of answer",
            "All the data inside the response should be factually correct"
        ],
        threshold=0.9
    )

    result = evaluate([test_case], [correctness])
    print(result)