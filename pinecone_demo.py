import pinecone
import os
import time

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY') or '0fd1dbc2-47e7-41e4-b84b-8bd38bb06a03'
PINECONE_ENV = os.environ.get('PINECONE_ENVIRONMENT') or '69f3e39c-5111-45e3-9146-5ed20377db44'

#verify pinecone API and establish connection
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

#ceate a pinecone index if not exist
index_name="firstindex"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        name=index_name,
        dimension=8,
        metric='euclidean'
    )
    # wait a moment for the index to be fully initialized
    time.sleep(1)

# now connect to the index
index = pinecone.GRPCIndex(index_name)
