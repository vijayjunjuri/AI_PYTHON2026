from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval
from app.banking_chatbot import chatbot

def test_answer_relevancy():
    query = "How to apply a personal loan"
    output = chatbot(query)
   # output = "You can apply personal loan via online banking or by visiting Vijay's House"
    print(output)

    # we have to prepare an LLM Test Case
         
    test_case = LLMTestCase(
    input = query,
    actual_output = output
    )

    # prepare a metrics - Answer Relevancy

   # answer_relevancy = AnswerRelevancyMetric(threshold=0.8)

    # Assertion - Validation

    result = evaluate([test_case], [answer_relevancy])
    print(result)



# deepeval test run filePath

# Instead of AnswerRelevancyMetrics step20, we can use GEval for more correctness achievement

answer_relevancy = GEval (

    name = "Answer_Relevancy",
    criteria = "Check if the name is relevant",
    evaluation_params = [

        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT
    ],

    evaluation_steps = [

        "check if the answer is fully relevant to the query",
        "if the answer is not relavant lower the score else if it is fully relevant provide it as 0.9"
    ],
    threshold = 0.8

)
