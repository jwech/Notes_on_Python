# pickle - Object Serialization

# Encode and Decode Data in Strings
import pickle

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('DATA:', end=' ')
print(data)

# pickle.dumps()
data_string = pickle.dumps(data)
print('PICKLE:: {!r}'.format(data_string))

# upickle the data
print('BEFORE: ', end=' ')
print(data)
data_string = pickle.dumps(data)
data_loads = pickle.loads(data_string)
print('AFTER:', end=' ')
print(data_loads)

print('SAME? :', (data is data_loads))
print('QUAL? :', (data == data_loads))
