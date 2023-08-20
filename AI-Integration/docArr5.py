#embedding
#a multi-dimensional representation of a Document (often a [1, D] vector)

import numpy as np
import scipy.sparse as sp
from docarray import Document

d0 = Document(embedding=[1, 2, 3])
d1 = Document(embedding=np.array([1, 2, 3]))
d2 = Document(embedding=np.array([[1, 2, 3], [4, 5, 6]]))
d3 = Document(embedding=sp.coo_matrix([0, 0, 0, 1, 0]))

print(d0.embedding)
print(d0.non_empty_fields)
print(d0.embedding.count(2))
print(d2.summary())
print(d3.summary())

#instead of manually specifying embedding, use a DNN with .embed option
q = (Document(uri='/home/hdu/Downloads/apple1.jpg')
     .load_uri_to_image_tensor()
     .set_image_tensor_normalization()
     .set_image_tensor_channel_axis(-1, 0))

#embed it into a vector
import torchvision
model = torchvision.models.resnet50(pretrained=True)
d = q.embed(model)

print(d.embedding)
print(d.summary())
print(d.non_empty_fields)
print(type(d))

#Documents with an .embedding can be “matched” against each other.
q1 = (Document(uri='/home/hdu/Downloads/apple1.jpg')
     .load_uri_to_image_tensor()
     .set_image_tensor_normalization()
     .set_image_tensor_channel_axis(-1, 0))

q2 = (Document(uri='/home/hdu/Downloads/apple2.png')
     .load_uri_to_image_tensor()
     .set_image_tensor_normalization()
     .set_image_tensor_channel_axis(-1, 0))

q3 = (Document(uri='/home/hdu/Downloads/apple3.png')
     .load_uri_to_image_tensor()
     .set_image_tensor_normalization()
     .set_image_tensor_channel_axis(-1, 0))

print(q1.summary())
print(q2.summary())
print(q3.summary())
import torchvision
model = torchvision.models.resnet50(pretrained=True)
d1 = q1.embed(model)
d2 = q2.embed(model)
d3 = q3.embed(model)

from docarray import DocumentArray
da = DocumentArray([d1,d2,d3])
print(da.contents)
print(da.embeddings)
d1.match(da)
d3.match(da)

#we create ten Documents and put them into a DocumentArray, and then use another Document to search against them.
da = DocumentArray.empty(10)
da.embeddings = np.random.random([10, 256])
q = Document(embedding=np.random.random([256]))
q.match(da)
q.summary()




