import autogen
 
config_list = [
    {
        'model': 'gpt-4o',
        'api_key': 'NOSTEALING'
    }
]
 
llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}
 
code_writer = autogen.AssistantAgent(
    name="CodeWriter",
    llm_config=llm_config,
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower(),
    system_message="""
        You are a Python coding expert. Your sole responsibility is to write Python code as requested. 
        Do not verify or test the code yourself. Focus exclusively on writing functional, clean, and well-documented code.
 
        Ensure that the code includes inputs or mechanisms that allow it to be tested effectively by the verifier, and there should only be one code block.
 
        After submitting the code to the verifier, wait for its response do not handle termination.
        """
)
 
code_verifier = autogen.UserProxyAgent(
    name="CodeVerifier",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=2,
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower(),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""
        Your task is to verify and test the code provided by the CodeWriter.
 
        - If the code works correctly:
            1. Respond with the complete, functional code.
            2. Append "TERMINATE" to signal the task's completion as the absolute last thing
 
        - If the code does not work:
            1. Respond with "Verification Failed TERMINATE"
 
        Always ensure termination of the task. If your initial attempt does not close the loop, retry termination by repeating the process.
        """
 
    ,
)
 
task = """
Write a Python function that takes a number and verifies that the number is a prime number.
"""
 
code_verifier.initiate_chat(
    code_writer,
    message=task
)
 
