from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K


class Convnet:
    # A class to define the convolutional neural network architecture

    EPOCHS = 3
    IMG_WIDTH = 150
    IMG_HEIGHT = 150
    BATCH_SIZE = 32

    train_data_dir = 'data/train'
    validation_data_dir = 'data/validation'
    nb_train_samples = 3000
    nb_validation_samples = 600

    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        if K.image_data_format() == 'channels_first':
            input_shape = (3, self.IMG_WIDTH, self.IMG_HEIGHT)
        else:
            input_shape = (self.IMG_WIDTH, self.IMG_HEIGHT, 3)

        # The CNN layer architecture
        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(3))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

        return model

    def train_and_test(model):
        train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
        test_datagen = ImageDataGenerator(rescale=1. / 255)
        train_generator = train_datagen.flow_from_directory(convnet.train_data_dir,
                                                            target_size=(convnet.IMG_WIDTH, convnet.IMG_HEIGHT),
                                                            batch_size=convnet.BATCH_SIZE, class_mode='categorical')
        validation_generator = test_datagen.flow_from_directory(convnet.validation_data_dir,
                                                                target_size=(convnet.IMG_WIDTH, convnet.IMG_HEIGHT),
                                                                batch_size=convnet.BATCH_SIZE, class_mode='categorical')
        print(validation_generator.class_indices)

        model.fit_generator(train_generator, steps_per_epoch=convnet.nb_train_samples // convnet.BATCH_SIZE,
                            epochs=convnet.EPOCHS, validation_data=validation_generator,
                            validation_steps=convnet.nb_validation_samples // convnet.BATCH_SIZE)


if __name__ == 'main':
    convnet = Convnet()
    model = convnet.build_model()
    convnet.train_and_test(model)
    model.save('model.h5')
    model.save_weights('weights.h5')
