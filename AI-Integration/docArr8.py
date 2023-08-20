#A DocumentArray itself has no attributes. Accessing attributes in this context
# means accessing attributes of the contained Documents in bulk.

#da[element_selector, attribute_selector]
from docarray import DocumentArray

da = DocumentArray().empty(3)
for d in da:
    d.chunks = DocumentArray.empty(2)
    d.matches = DocumentArray.empty(2)

da.summary()
print(da[:, 'id'])
print(da['@c', 'id'])
print(da[..., 'id'])

#set mime_type for all top-level documents
da[:, 'mime_type'] = ['image/jpg', 'image/png', 'image/jpg']
da.summary()

#deleting
del da[:, 'mime_type']
da.summary()

