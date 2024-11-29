Prime Number Verification Automation
Overview

This app automates Python code generation and verification for tasks like checking if a number is prime. It uses two agents: CodeWriter (writes code) and CodeVerifier (tests code).
How It Works

    Prompt: Provide a task (e.g., "Write a function to check if a number is prime").
    Code Generation: CodeWriter creates clean, functional Python code.
    Verification: CodeVerifier tests the code:
        If successful, returns the working code with TERMINATE.
        If failed, returns Verification Failed TERMINATE.

Example Output

def verify_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
TERMINATE

