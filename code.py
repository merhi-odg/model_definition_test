# modelop.schema.0: input_schema.avsc
# modelop.slot.1: in-use


import json
  

# modelop.init
def begin(model_def):
    
    global model_definition
    global input_schema_definition
    global output_schema_definition
    
    print("\nModel Definition keys: \n", flush=True)
    print(model_def.keys(), flush=True)
    
    # if 'job' in model_def.keys():
    #     print(model_def['job'], flush=True)
    
    # elif 'deployedModel' in model_def.keys():
    #     print(model_def['deployedModel'], flush=True)
    
    model_definition = model_def
    
    # Extract rawJson from model_def
    raw_json = json.loads(model_def['rawJson'])
    
    # The JSON tree is different for models running as batch models and models deployed at REST:
    
    # Models running as batch models have a 'model' key, whereas ...
    if 'model' in raw_json.keys():
        model_reference_key = 'model'
        
    # ... models running as REST have a 'deployableModel' key
    elif 'deployableModel' in raw_json.keys():
        model_reference_key = 'deployableModel'
    
    print("\nModel Reference Key: ", model_reference_key, flush=True)
    
    try:
        # Extract input schema from rawJson
        input_schemas = raw_json[model_reference_key]['storedModel']['modelMetaData']['inputSchema']

        # Checking to see if any input schemas exist
        if len(input_schemas) > 0:
            print("\nInput Schema(s) found!\n", flush=True)

            input_schema_definition = input_schemas[0]['schemaDefinition']

            print("\nInput Schema Definition: \n", flush=True)
            print(input_schema_definition, flush=True)

        else:
            print("\nInput Schema(s) NOT found!\n", flush=True)
            input_schema_definition = None
        
        
        # Extract output schema from rawJson
        output_schemas = raw_json[model_reference_key]['storedModel']['modelMetaData']['outputSchema']

        # Checking to see if any output schemas exist
        if len(output_schemas) > 0:
            print("\nOutput Schema(s) found!\n", flush=True)

            output_schema_definition = output_schemas[0]['schemaDefinition']

            print("\nOutput Schema Definition: \n", flush=True)
            print(output_schema_definition, flush=True)

        else:
            print("\nOutput Schema(s) NOT found!\n", flush=True)
            output_schema_definition = None
    
    except:
        
        print("\nSchema extraction failed!\n", flush=True)
        
        input_schema_definition = None
        output_schema_definition = None
    
    pass
      


# modelop.score
def action(data):
    """
    param: data: dict of he form {"input": x} for some number x
    """
    
    print("action input: ", data, flush=True)
    
    num = data["input"]
    
    print("num: ", num, flush=True)
    
    out = {"reciprocal": 1/num}
    
    print("output: ", out, flush=True)
        
    yield out
