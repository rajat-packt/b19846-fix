class ConvNet():
    @staticmethod
    def create(width, height, depth, classes):
        # initialize the network
        network = Sequential()
        inputShape = (height, width, depth)

        # first set of CONV => RELU => POOL layers
        network.add(Conv2D(50, (10, 10), padding="same", input_shape=inputShape))
        network.add(Activation("relu"))
        network.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # second set of CONV => RELU => POOL layers
        network.add(Conv2D(50, (5, 5), padding="same"))
        network.add(Activation("relu"))
        network.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # third set of CONV => RELU => POOL layers
        network.add(Conv2D(50, (5, 5), padding="same"))
        network.add(Activation("relu"))
        network.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # Fully connected ReLU layers
        network.add(Flatten())
        network.add(Dense(500))
        network.add(Activation("relu"))
        network.add(Dense(500))
        network.add(Activation("relu"))

        # softmax classifier
        network.add(Dense(classes))
        network.add(Activation("softmax"))

        # return the constructed network architecture
        return network
