from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter



ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch('LPZh9BOjkQs')

def format_transcript(fetched_transcript):
    return "".join(snippet.text for snippet in fetched_transcript)

text = format_transcript(fetched_transcript=fetched_transcript)


text_splitter= RecursiveCharacterTextSplitter(chunk_size= 100 , chunk_overlap = 20 )

documents = text_splitter.create_documents(text)

print(documents[2])