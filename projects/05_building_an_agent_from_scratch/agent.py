from termcolor import colored
import os
from dotenv import load_dotenv
load_dotenv()

# models
import requests
import json
import operator


# defining the model class

class OllamaModel:

    def __init__(self, model, system_prompt, temperature=0, stop=None):
        """
        Initializes the OllamaModel with the given parameters.

        Parameters:
        model (str): The name of the model to use.
        system_prompt (str): The system prompt to use.
        temperature (float): The temperature setting for the model.
        stop (str): The stop token for the model.
        """
        self.model_endpoint = "http://localhost:11434/api/generate"
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt
        self.headers = {"Content-Type": "application/json"}
        self.stop = stop

    # The generate_text method sends a request to the model API 
    # and returns the response.
    def generate_text(self, prompt):
        """
        Generates a response from the Ollama model based on the 
        provided prompt.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        dict: The response from the model as a dictionary.
        """
        payload = {
            "model": self.model,
            "format": "json",
            "prompt": prompt,
            "system": self.system_prompt,
            "stream": False,
            "temperature": self.temperature,
            "stop": self.stop
        }

        try:
            request_response = requests.post(
                self.model_endpoint,
                headers = self.headers,
                data = json.dumps(payload)
            )

            print("REQUEST RESPONSE", request_response)
            request_response_json = request_response.json()
            response = request_response_json["response"]
            response_dict = json.loads(response)

            print(f"\n\nResponse from Ollama model: {response_dict}")

            return response_dict
        except requests.RequestException as e:
            response = {"error": f"Error in invoking model! {str(e)}"}
            return response
        
# Creating tools for the agent
# The next step is to create tools that our agents can use. 
# These tools are simple Python functions that perform specific 
# tasks. Here’s an example of a basic calculator and a string 
# reverser.

def basic_calculator(input_str):
    """
    Perform a numeric operation on two numbers based on the input string or dictionary.

    Parameters:
    input_str (str or dict): Either a JSON string representing a dictionary with keys 'num1', 'num2', and 'operation',
                            or a dictionary directly. Example: '{"num1": 5, "num2": 3, "operation": "add"}'
                            or {"num1": 67869, "num2": 9030393, "operation": "divide"}

    Returns:
    str: The formatted result of the operation.

    Raises:
    Exception: If an error occurs during the operation (e.g., division by zero).
    ValueError: If an unsupported operation is requested or input is invalid.
    """
    
    try:
        # handle both dictionary and string inputs
        if isinstance(input_str, dict):
            input_dict = input_str
        else:
            # clean and parse the input string
            input_str_clean = input_str.replace("'", "\"")
            input_str_clean = input_str_clean.strip().strip("\"")
            input_dict = json.loads(input_str_clean)

        # validate required fields
        if not all(key in input_dict for key in ["num1", "num2", "operation"]):
            return "Error: Input must contain 'num1', 'num2' and 'operation'"
        num1 = float(input_dict['num1']) # convert to float to handle decimal numbers
        num2 = float(input_dict["num2"])
        operation = input_dict["operation"].lower() # make case-insensitive
    except (json.JSONDecodeError, KeyError) as e:
        return "Invalid input format. Please provide valid numbers and operation."
    except ValueError as e:
        return "Error: Please provide valid numerical values."
    
    # define the supported operations with error handling
    operations = {
        "add": operator.add,
        "plus": operator.plus, # alternative word for add
        "subtract": operator.sub,
        "minus": operator.sub, # alternative word for subtract
        "multiply": operator.mul,
        "times": operator.mul, # alternative word for multiply
        "divide": operator.truediv,
        "floor_divide": operator.floordiv,
        "modulus": operator.mod,
        "power": operator.pow,
        "lt": operator.lt,
        "le": operator.le,
        "eq": operator.eq,
        "ne": operator.ne,
        "ge": operator.ge,
        "gt": operator.gt
    }

    # check if the operation is supported
    if operation not in operations:
        return f"Unsupported operation: '{operation}'. Supported operations are: {', '.join(operations.keys())}"
    try:
        # special handling for division by zero
        if (operation in ["divide", "floor_divide", "modulus"]) and num2 == 0:
            return "Error: Division by zero is not allowed"
        
        # perform the operation
        result = operations[operation](num1, num2)

        # format result based on type
        if isinstance(result, bool):
            result_str = "True" if result else "False"
        elif isinstance(result, float):
            # handle floating point precision
            result_str = f"{result:.6f}".rstrip("0").rstrip(".")
        else:
            result_str = str(result)

        return f"The answer is: {result_str}"
    except Exception as e:
        return f"Error during calculation: {str(e)}"