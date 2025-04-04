from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
The sky shimmered with hues of orange and violet as the 
last rays of sunlight danced over the quiet town. 
Birds chirped their final songs before nightfall, 
and a cool breeze carried the scent of jasmine through 
the air. In the distance, a train hummed along the tracks, 
its whistle fading into the horizon. Children laughed, 
chasing fireflies with glass jars, while an old man sat on 
a bench, smiling at memories only he could see. The world, 
for a moment, seemed perfectly at peace.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks)) # 9

print(chunks)
# ['The sky shimmered with hues of orange and violet as the',
#  'last rays of sunlight danced over the quiet town.',
#  'Birds chirped their final songs before nightfall,',
#  'and a cool breeze carried the scent of jasmine through',
#  'the air. In the distance, a train hummed along the tracks,',
#  'its whistle fading into the horizon. Children laughed,',
#  'chasing fireflies with glass jars, while an old man sat on',
#  'a bench, smiling at memories only he could see. The world,',
#  'for a moment, seemed perfectly at peace.']