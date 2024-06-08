from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224

def load_data(img_directory):
    # Create an instance of ImageDataGenerator with the required transformations
    datagen = ImageDataGenerator(
        rescale=1./255, # Scales the pixel values to a range of [0,1]
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2  # for splitting train and validation data
    )

    # Load training data from directories
    train_generator = datagen.flow_from_directory(
        img_directory,
        target_size=(IMAGE_HEIGHT, IMAGE_WIDTH),
        batch_size=32,
        class_mode='categorical',
        subset='training',  # Set as training data
        shuffle=True  # Ensure the data is well shuffled
    )

    # Load validation data
    validation_generator = datagen.flow_from_directory(
        img_directory,
        target_size=(IMAGE_HEIGHT, IMAGE_WIDTH),
        batch_size=32,
        class_mode='categorical',
        subset='validation',  # Set as validation data
        shuffle=True  # Ensure the data is well shuffled
    )

    return train_generator, validation_generator
