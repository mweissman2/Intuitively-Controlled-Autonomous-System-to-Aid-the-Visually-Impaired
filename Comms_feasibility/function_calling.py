import time
import json
import google.generativeai as genai
import google.ai.generativelanguage as glm

# Get API KEY
config_path = 'C:/Users/Max/Desktop/api_keys.json'
with open(config_path) as f:
    GEMINI_API_KEY = json.load(f)['GEMINI_API_KEY']
genai.configure(api_key=GEMINI_API_KEY)

# Define functions
# noinspection PyTypeChecker
available_funcs = glm.Tool(
    function_declarations=[
        glm.FunctionDeclaration(
            name='global_nav',
            description="Begins global navigation from starting position to destination",
            parameters=glm.Schema(
                type=glm.Type.OBJECT,
                properties={
                    'destination': glm.Schema(type=glm.Type.STRING),
                },
                required=['destination']
            )
        ),
        glm.FunctionDeclaration(
            name='get_next_waypoint_on_route',
            description="Checks the current position using GPS and the current global navigator to identify where it "
                        "is on the path and output the next path waypoint",
            parameters=glm.Schema(
                type=glm.Type.OBJECT,
                properties={
                    'position': glm.Schema(type=glm.Type.ARRAY),
                    'navigation_map': glm.Schema(type=glm.Type.OBJECT),
                },
                required=['position', 'navigation_map']
            )
        ),
        glm.FunctionDeclaration(
            name='describe_env',
            description="Takes a picture of the environment and passes to a model to describe the scene",
        )
    ])

# Define model
model = genai.GenerativeModel(
    'gemini-pro',
    tools=[available_funcs])

# Start chat and send message
chat = model.start_chat()
nav_msg = 'Take me to the closest mall'
desc_env_msg = 'What does the world around me look like?'
waypoint_msg = 'Where is the next waypoint on my route? I am currently at [0,1] and will provide the map separately'

start_time = time.time()
response = chat.send_message(
    nav_msg
)
end_play_time = time.time()
play_time = end_play_time - start_time
# print(play_time)

# This sends the answer to the LLM, which we don't really care about (we just want the function call itself)
# response = chat.send_message(
#   glm.Content(
#     parts=[glm.Part(
#         function_response = glm.FunctionResponse(
#           name='now',
#           response={'datetime': 'Sun Dec 5 03:33:56 PM UTC 2023'}
#         )
#     )]
#   )
# )

print(response.candidates)
if response.candidates[0].content.parts[0].function_call.name == 'global_nav':
    dest = response.candidates[0].content.parts[0].function_call.args['destination']
    print(f'global_nav called! Destination: {dest}')
elif response.candidates[0].content.parts[0].function_call.name == 'get_next_waypoint_on_route':
    print('get_next_waypoint_on_route called!')
elif response.candidates[0].content.parts[0].function_call.name == 'describe_env':
    print('describe_env called!')
else:
    print(response.text)
