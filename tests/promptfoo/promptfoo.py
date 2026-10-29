'''

Promptfoo Metrics:

Types of testing using promptfoo

Deterministics Testing: 

In this case we will create a test case with specific input and expected output


assert:
    - type: 
      value: 


1. contains - To check if the output contains a specific word or phrase.
2. equals - To check if the output is exactly equal to the expected output
3. regex - To heck if the output matches a specific regular expression
4. not-contains - To check if the output not contains a specific word or phrase.
5. start-with - To check if the output starts with a specific word or phrases.
6. ends-with - To check if the output ends with a specific word or phrases.
7. is-json - To check if the output is a valid json string or not.
8. javascript - To execute custom javascript function evaluate the output:
ex: 2+2 = 4 - output.includes("4")
9. contains-any - To check if the output contains any of the specified word or phrases.
10. contains-all - To check if the output contains all of the specified word or phrases.
11. icontains - To check if the output contains a specific word or phrase, ignoring the case.

Non-deterministics Testing:  We can use promptfoo for non-deterministic evaluation for llms.
In this case also we will create the test cases with specific inputs without expected output.


1. LLM as a Judge

llm-rubric
Red Teaming
MITRE ATLAS
NIST AI

---------------------------------------------------------------------------------------------------------

Model Graded
1. llm-rubric
2. answer-relevance
3. factuality
4. context-relevance
5. context-recall
6. context-faithfulness
7. g-eval


1. By using model id - gpt-4o-mini
2. By using API
3. By using function call



Sample promptfoo configuration file:

description: This test validates the answer is relevant to the query or not using model graded evaluation

providers/targets:
    - id: openai:gpt-4o-mini

prompts:
    - "You are a professional banking customer AI assistant
       answer {{prompt}}"

tests:
    - vars:
        prompt: "How to reset the ATM PIN?"
      assert:
         - type: answer-relevance
           threshold: 0.8

    - vars:
        prompt: "How to apply for personal loan?"
      assert:
         - type: answer-relevance
           threshold: 0.8

           
How to execute the promptfoo file
# promptfoo eval -c pathofthefile


API Testing:

API request:

Base url - http://127.0.0.1:8000
end point - chat
URL - http://127.0.0.1:8000/chat
http method - POST
header - header details
request body - {key:value}



providers:
    - id: openai:gpt-4o-mini


Working with API:

providers:
    - id: http
      config:
        url: http://127.0.0.1:8000/chat
        method: POST
        body: 
          query: "{{prompt}}"
        transformResponse: json.response
         



Auto generation of the test case for Red team using Red team framework:

Below are the components that we need to have inside the yaml file

description:

prompts:

redteam:

  numTests: 5

  plugin: 
    - nist:ai:measure

  strategies:
    - jailbreak
    - 


Command to generate the RedTeam test cases:

# promptfoo redteam generate -c pathOfTheFile

Command to filter the test case depending on the suite file or any metadata key:

eval -c redteam.yaml --filter-metadata suite=smoke -j 5

# How to rerun only the failed test cases:

promptfoo eval --retry-errors

'''