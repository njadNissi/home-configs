import tensorflow as tf

print("\tTF CPU SETUP\n", "="*25)
print(tf.reduce_sum(tf.random.normal([1000, 1000])))

print("\tTF GPU SETUP\n", "="*25)
print(tf.config.list_physical_devices('GPU'))
