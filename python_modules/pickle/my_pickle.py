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
# pickle.loads()
print('BEFORE: ', end=' ')
print(data)
data_string = pickle.dumps(data)
data_loads = pickle.loads(data_string)
print('AFTER:', end=' ')
print(data_loads)

print('SAME? :', (data is data_loads))
print('QUAL? :', (data == data_loads))

'''Working with Streams'''
# pickle.dump(obj, file, protocol=0)  
# protocol: pickle.HIGHEST_PROTOCOL / pickle.DEFAULT_PROTOCOL / -1
# pickle.load(file)

data_list = [[1, 1, 'yes'],
             [1, 1, 'no']]
data_dict = [{0: [1, 2, 3, 4],
             1: ('a', 'b')}]
with open('./python_modules/pickle/data.pkl', 'wb') as f:
    pickle.dump(data_list, f) # use the highest protocol available
    pickle.dump(data_dict, f)

with open('./python_modules/pickle/data.pkl', 'rb') as f:
    data1 = pickle.load(f)
    print(data1)
    data2 = pickle.load(f)
    print(data2)

p = pickle.dumps(data_list)
print(pickle.loads(p))
p = pickle.dumps(data_dict)
print(pickle.loads(p))