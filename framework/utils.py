from deepeval.test_case import LLMTestCase
from typing import Optional, Callable, List
import allure

def build_llm_test_case(chatbot_fun: Callable, prompt: str, context: Optional[List[str]] = None, 
                        expected_output: Optional[str] = None, retrieval_context : Optional[List[str]]=None):

    response = chatbot_fun(prompt) # chatbot(prompt)

    allure.attach(prompt, name= "User Query", attachment_type=allure.attachment_type.TEXT)
    allure.attach(response, name= "Assistant Response", attachment_type=allure.attachment_type.TEXT)

    if context != None:
        allure.attach(str(context), name= "Context", attachment_type=allure.attachment_type.TEXT)

    if expected_output != None:
            allure.attach(str(expected_output), name= "Expected Output", attachment_type=allure.attachment_type.TEXT)

    if retrieval_context != None:
            allure.attach(str(retrieval_context), name= "Retrieval Context", attachment_type=allure.attachment_type.TEXT)
    

    return LLMTestCase(
            input=prompt,
            actual_output=response,
            context=context,
            expected_output=expected_output,
            retrieval_context=retrieval_context
        )