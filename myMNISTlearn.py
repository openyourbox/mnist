from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import readdraw
import readMNIST
mnist = input_data.read_data_sets("MNIST-data", one_hot=True)
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
#y = tf.matmul(x, W) + b
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])
#cross_entropy = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
mmp = readdraw.image
#sess = tf.InteractiveSession()
#tf.global_variables_initializer().run()
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
  # Train
for _ in range(500):
    if (_ % 100 == 0):
        print(sess.run(b))
    #batch_xs = readMNIST.readtrainimage(_ * 100)
    #batch_ys = readMNIST.readtrainlabel(_ * 100)
    batch_xs, batch_ys = mnist.train.next_batch(100)
    """
    xs = np.zeros(shape=(100, 784))
    for i in range(100):
        for j in range(784):
            if batch_xs[i, j] > 0:
                xs[i, j] = batch_xs[i, j]
    """
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
print(sess.run(tf.argmax(y, 1), feed_dict={x: mmp.reshape((1, 784))}))

sess.close()