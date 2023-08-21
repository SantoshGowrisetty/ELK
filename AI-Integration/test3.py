import docarray
from docarray import BaseDoc, DocList
import numpy as np
from docarray.index import ElasticDocIndex  # or ElasticV7DocIndex
import numpy

# Define the document schema.
class MyDoc(BaseDoc):
    title: str

    # Create dummy documents.
docs = DocList[MyDoc](MyDoc(title=f'title #{i}', embedding=np.random.rand(128)) for i in range(10))
#
# # Initialize a new ElasticDocIndex instance and add the documents to the index.
doc_index = ElasticDocIndex[MyDoc](index_name='my_index',hosts='http://os1:9200')
print(type(doc_index))
doc_index.index(docs)


#check index from elasticsearch
