
import  uuid


print(uuid.UUID)
print(uuid.uuid1())
print(uuid.uuid4())

# 6fa459ea-ee8a-3ca4-894e-db77e160355e
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org'))


# make a UUID using a SHA-1 hash of a namespace UUID and a name
# UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org'))
