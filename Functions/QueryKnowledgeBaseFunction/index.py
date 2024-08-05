import json
import boto3

bedrock_agent_runtime_client = boto3.client('bedrock-agent-runtime')

def lambda_handler(event, context):
    try:
        # Logging the event for debugging
        print("Received event:", json.dumps(event, indent=2))
        
        # Extract the query from the event
        query = event.get("query", "Reasons why insurance premium might go up")
        
        # Define the Knowledge Base ID and Model ARN
        knowledge_base_id = 'A2X0SPJ8LQ'  # Your Knowledge Base ID
        model_arn = 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-v2'  # Your Model ARN
        
        # Define the prompt
        prompt = f"""\n\nHuman:
        Please answer the following question appropriately.
        [question]
        {query}
        Assistant:
        """
        
        # Call the Bedrock API
        response = bedrock_agent_runtime_client.retrieve_and_generate(
            input={
                'text': prompt,
            },
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': knowledge_base_id,
                    'modelArn': model_arn,
                }
            }
        )
        
        print("Received response:", json.dumps(response, ensure_ascii=False))
        
        # Extract the response content
        response_output = response['output']['text']
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'tips': response_output
            })
        }
        
    except Exception as e:
        print(f"Exception: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
