import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('IntervisionInsurance-Customer')  # Replace with your DynamoDB table name
lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    try:
        # Logging the entire event for debugging
        print("Received event from Lex:", json.dumps(event, indent=2))

        # Extract session attributes
        session_attributes = event.get('sessionState', {}).get('sessionAttributes', {})

        # Determine the structure of the event and extract the intent
        if 'currentIntent' in event:
            current_intent = event['currentIntent']
        elif 'sessionState' in event and 'intent' in event['sessionState']:
            current_intent = event['sessionState']['intent']
        elif 'interpretations' in event and event['interpretations']:
            current_intent = event['interpretations'][0]['intent']
        else:
            raise KeyError("No intent found in event")

        # Ensure the 'slots' are present in the 'currentIntent'
        if 'slots' not in current_intent:
            raise ValueError("Missing 'slots' in 'currentIntent'")

        slots = current_intent['slots']

        # Handle name confirmation
        if 'NameConfirmation' in slots and slots['NameConfirmation']:
            print(f"NameConfirmation slot details: {slots['NameConfirmation']}")
            name_confirmation_value = slots['NameConfirmation']['value']['interpretedValue'].lower()
            print(f"Extrancted NameConfirmation value: {name_confirmation_value}")
            if name_confirmation_value in ['yes', 'yeah', 'yup', 'y' , 'Yes its name']:
                # Call the knowledge base lambda function
                knowledge_base_response = lambda_client.invoke(
                    FunctionName='QueryKnowledgeBaseFunction',  # Replace with your Lambda function name
                    InvocationType='RequestResponse',
                    Payload=json.dumps({})
                )
                knowledge_base_result = json.loads(knowledge_base_response['Payload'].read().decode('utf-8'))
                tips = json.loads(knowledge_base_result['body']).get('tips', 'No tips found.')
                response_message = f"okay here are some reasons why your insurance premium have gone up: {tips}"
                return {
                    "sessionState": {
                        "dialogAction": {
                            "type": "Close",
                            "fulfillmentState": "Fulfilled",
                        },
                        "intent": {
                            "name": current_intent['name'],
                            "slots": slots,
                            "state": "Fulfilled"
                        },
                        "sessionAttributes": session_attributes
                    },
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": response_message
                        }
                    ]
                }
            else:
                response_message = "Okay, please provide me with your policy number again."
                slots['PolicyNumber'] = None  # Reset PolicyNumber slot to re-ask for it
                return {
                    "sessionState": {
                        "dialogAction": {
                            "type": "ElicitSlot",
                            "slotToElicit": "PolicyNumber",
                        },
                        "intent": {
                            "name": current_intent['name'],
                            "slots": slots,
                            "state": "InProgress"
                        },
                        "sessionAttributes": session_attributes
                    },
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": response_message
                        }
                    ]
                }

        # Ensure the 'PolicyNumber' slot is retrieved correctly from the event object
        if 'PolicyNumber' not in slots:
            raise ValueError("Missing 'PolicyNumber' slot in 'slots'")

        policy_number_data = slots['PolicyNumber']

        # Extract the actual policy number value
        if isinstance(policy_number_data, dict) and 'value' in policy_number_data:
            policy_number = policy_number_data['value'].get('interpretedValue')
        else:
            policy_number = policy_number_data

        if not policy_number:
            raise ValueError("PolicyNumber is empty")

        # Fetch item from DynamoDB
        response = table.get_item(Key={'PolicyNumber': policy_number})
        item = response.get('Item')

        if item:
            first_name = item.get('FirstName', 'N/A')
            last_name = item.get('LastName', 'N/A')
            response_message = f"The policy is under the name {first_name} {last_name}. Can you please confirm if this is your name?"
            session_attributes['FirstName'] = first_name
            session_attributes['LastName'] = last_name
        else:
            response_message = "No details found for the provided policy number."

        # Return the correct response format expected by Lex
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "ElicitSlot",
                    "slotToElicit": "NameConfirmation",
                },
                "intent": {
                    "name": current_intent.get('name'),
                    "slots": {k: v for k, v in slots.items() if k in ['PolicyNumber', 'NameConfirmation']},
                    "state": "InProgress"
                },
                "sessionAttributes": session_attributes
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": response_message
                }
            ]
        }

    except KeyError as e:
        print(f"KeyError: {e}")
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                },
                "intent": {
                    "name": current_intent.get('name'),
                    "slots": {k: v for k, v in slots.items() if k in ['PolicyNumber', 'NameConfirmation']},
                    "state": "Failed"
                },
                "sessionAttributes": session_attributes
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"Error: {e}"
                }
            ]
        }

    except ValueError as e:
        print(f"ValueError: {e}")
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "ElicitSlot",
                    "slotToElicit": "PolicyNumber",
                },
                "intent": {
                    "name": current_intent.get('name'),
                    "slots": {k: v for k, v in slots.items() if k in ['PolicyNumber', 'NameConfirmation']},
                    "state": "InProgress"
                },
                "sessionAttributes": session_attributes
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": 'Please provide your policy number.'
                }
            ]
        }

    except Exception as e:
        print(f"Exception: {e}")
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                },
                "intent": {
                    "name": current_intent.get('name'),
                    "slots": {k: v for k, v in slots.items() if k in ['PolicyNumber', 'NameConfirmation']},
                    "state": "Failed"
                },
                "sessionAttributes": session_attributes
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": 'Sorry, I am unable to process your request at the moment.'
                }
            ]
        }
