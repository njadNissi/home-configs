import tensorflow as tf

devname = None
if tf.test.gpu_device_name():
    devname = tf.test.gpu_device_name()
    print('Default GPU Device: {}'.format(devname))
    with tf.device(devname):
	    print(tf.reduce_sum(tf.random.normal([1000, 1000])))
else:
	print("Please install GPU version of TensorFlow")
