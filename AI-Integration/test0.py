import docarray
import elasticsearch
docarray.__version__
from docarray import DocumentArray, Document
from elasticsearch import Elasticsearch


da = DocumentArray(
    storage='elasticsearch',
    config={'hosts': 'http://os1:9200','index_name': 'new_stuff','n_dim': 128},
)
da.summary()

