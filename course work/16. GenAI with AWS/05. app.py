import boto3
import botocore.config
import json

def blog_generate_using_bedrock(blogtopic:str)-> str:
    prompt = f"""<s>[INST]Human: Write a 200 words blog on the topic {blogtopic}
    Assistant:[/INST]
    """

    body={
        "prompt":prompt,
        "max_gen_len":512,
        "temperature":0.5,
        "top_p":0.9
    }

    try:
        bedrock=boto3.client("bedrock-runtime", region_name="us-east-1",
                             config=boto3.config.Config(read_timeout=300, retries={"max_attempts":3}))
        response = bedrock.invoke_model(body=json.dumps(body), modelId="meta.llama2-13b-chat-v1")
        response_content = response.get("body").read()
        response_data = json.loads(response_content)
        print(response_data)
        blog_details = response_data["generation"]
        return blog_details
    except Exception as e:
        print(f"Error generating the blog:{e}")
        return ""