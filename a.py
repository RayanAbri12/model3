
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

data_path = '/home/rahem/Downloads/dataP.txt'
df = pd.read_csv(data_path, skiprows=1,names=['yyyy.MM.dd','(DDD)','HH:mm:ss','C-score','foF2','hmF2','TEC','B0'],
                 sep=',', index_col=False)


df = df[df.foF2 != 0]

for index,row in df.iterrows():
    a = row['yyyy.MM.dd'] +','+ row['HH:mm:ss']
    df.set_value(index, 'new', a)


df['new'] = pd.to_datetime(df['new'])

print(df)
print(df.dtypes)
df1 = df[df.new <= '2012-01-02 00:00:00']


#df = df[df.TEC != 0]
plt.plot(df1['foF2'], df1['new'].index)

y_input = df1['foF2']
x_input = df1['new'].index
# model parameters
# order of polynomial
n = 2
W = tf.Variable(tf.random_normal([n, 1]), name='weight')
# bias
b = tf.Variable(tf.random_normal([1]), name='bias')

# X=tf.placeholder(tf.float32,shape=(None,2))
X = tf.placeholder(tf.float32, shape=[None, n])
Y = tf.placeholder(tf.float32, shape=[None, 1])


# preparing the data
def modify_input(x, x_size, n_value):
    x_new = np.zeros([x_size, n_value])
    for i in range(n):
        x_new[:, i] = np.power(x, (i + 1))
        x_new[:, i] = x_new[:, i] / np.max(x_new[:, i])
    return x_new


# model
x_modified = modify_input(x_input, x_input.size, n)
Y_pred = tf.add(tf.matmul(X, W), b)

# algortihm
loss = tf.reduce_mean(tf.square(Y_pred - Y))
# training algorithm
optimizer = tf.train.GradientDescentOptimizer(0.05).minimize(loss)
# initializing the variables
init = tf.global_variables_initializer()

# starting the session session
sess = tf.Session()
sess.run(init)

epoch = 12000

for step in range(epoch):
    _, c = sess.run([optimizer, loss], feed_dict={X: x_modified, Y: y_input})
    if step % 1000 == 0:
        print
        c

print
"Model paramters:"
print
sess.run(W)
print
"bias:%f" % sess.run(b)
# comparing our model
y_test = sess.run(Y_pred, feed_dict={X: x_modified})
plt.plot(x_input, y_input, x_input, y_test)


#plt.title('TEC Over 2012')
#plt.legend(loc='lower right')
#plt.xlabel('TEC')
#plt.ylabel('TIME')
#plt.ticklabel_format(style='plain')
plt.show()
