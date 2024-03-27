import time
import json
import pandas as pd
import numpy as np
import google.generativeai as genai

# Get API KEY
config_path = 'C:/Users/Max/Desktop/api_keys.json'
with open(config_path) as f:
    GEMINI_API_KEY = json.load(f)['GEMINI_API_KEY']
genai.configure(api_key=GEMINI_API_KEY)

# Define model
model = 'models/embedding-001'

# Build a quick embeddings database
DOCUMENT1 = {
    "title": "Navigation Mode",
    "content": "Your robotic system has a navigation mode that allows you to navigate to a user-defined destination. To start the navigation mode, the user will use speech as the source of input. The speech will then be processed using audio processing to split the speech into chunks. The navigation mode will only start if the audio chunk is relevant to starting navigation mode. As an example, the user would say 'take me to the nearest mall', or 'I want to go to my friend Jesse's house'."}
DOCUMENT2 = {
    "title": "Search Mode",
    "content": "Your robotic system has a search mode that allows you to search the direct area around the user for a specific object. To start the search mode, the user will use speech as the source of input. The speech will then be processed using audio processing to split the speech into chunks. The search mode will only start if the audio chunk is relevant to starting search mode. As an example, the user would say 'I dropped my keys, can you help me find them', or 'where is the closest exit sign?'"}
DOCUMENT3 = {
    "title": "Sighted Guide Mode",
    "content": "Your robotic system has a sighted guide mode that performs similar duties to sighted guides for people with visual impairments. The goal of sighted guide mode is to be more conversational with the user and to actively describe the scenes around them. Your robotic system is equipped with cameras to be able to see the world around it. Sighted guide mode relies on these cameras to understand the scene around it. The system is also equipped with GPS and depth cameras to understand its position in the world. To start the sighted guide mode, the user will use speech as the source of input. The speech will then be processed using audio processing to split the speech into chunks. The sighted guide mode will only start if the audio chunk is relevant to starting sighted guide mode. As an example, the user would say 'I believe I'm in a park right now, can you describe what it's like?', or 'I hear a dog barking over there, can you tell me what it's doing and what color the dog is?'"}

# Organize documents
documents = [DOCUMENT1, DOCUMENT2, DOCUMENT3]
df = pd.DataFrame(documents)
df.columns = ['Title', 'Text']


# Get the embeddings of each text and add to an embeddings column in the dataframe
def embed_fn(title, text):
    return genai.embed_content(model=model,
                               content=text,
                               task_type="retrieval_document",
                               title=title)["embedding"]


df['Embeddings'] = df.apply(lambda row: embed_fn(row['Title'], row['Text']), axis=1)

# This is set up for document search not classification right now
start_time = time.time()
q = "What would I use if I want to know the color of a shirt?"
request = genai.embed_content(model=model,
                              content=q,
                              task_type="retrieval_query")


def find_best_passage(query, dataframe):
    """
  Compute the distances between the query and each document in the dataframe
  using the dot product.
  """
    query_embedding = genai.embed_content(model=model,
                                          content=query,
                                          task_type="retrieval_query")
    dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding["embedding"])
    idx = np.argmax(dot_products)
    return dataframe.iloc[idx]['Text']  # Return text from index with max value


passage = find_best_passage(q, df)
end_play_time = time.time()
play_time = end_play_time - start_time
print(play_time)
print(passage)