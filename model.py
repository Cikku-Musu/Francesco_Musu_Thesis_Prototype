from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam


def create_model(IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CATEGORIES):
    # Start defining the model as a Sequential model to stack layers.
    model = Sequential([
        # Input layer specifying the expected input shape, which is crucial for the network to know the shape of the data it will be processing.
        Input(shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3)),
        
        # First convolutional layer with 32 filters of size 3x3 and ReLU activation function.
        # ReLU is chosen to add non-linearity to the model, helping it learn more complex patterns in the data.
        Conv2D(32, (3, 3), activation='relu'),
        # Conv2D(64, (3, 3), activation='relu'),  # Increased filters
        
        
        # First pooling layer that reduces the spatial dimensions (height and width) of the output from the previous layer.
        # MaxPooling is used here to reduce the dimensions by taking the maximum value in each window of size 2x2.
        MaxPooling2D(2, 2),
         
        # Dropout(0.25),  # Added dropout
        
        # Second convolutional layer with 64 filters, increasing the capacity of the model to capture more complex features.
        Conv2D(64, (3, 3), activation='relu'),
        # Conv2D(128, (3, 3), activation='relu'),  # Increased filters
        
        
        # Second pooling layer to further reduce spatial dimensions and control overfitting.
        MaxPooling2D(2, 2),

        # Dropout(0.25),  # Added dropout
        
        # Third convolutional layer with 128 filters to capture even more complex features.
        Conv2D(128, (3, 3), activation='relu'),
        # Conv2D(256, (3, 3), activation='relu'),  # Added extra convolution layer
        
        # Third pooling layer for further dimensionality reduction.
        MaxPooling2D(2, 2),
        
        # Dropout(0.25),  # Added dropout
        
        # Flatten layer to convert the 2D feature maps into a 1D feature vector.
        # This step is necessary to transition from convolutional layers to dense (fully connected) layers.
        Flatten(),
        
        # A fully connected (dense) layer with 512 neurons and ReLU activation.
        # This layer integrates features learned by previous layers to help in making final predictions.
        Dense(512, activation='relu'),
        # Dense(1024, activation='relu'),  # Increased dense layer size
        
        # Dropout layer to reduce overfitting by randomly setting a fraction (50% here) of input units to 0 at each update during training.
        Dropout(0.5),
        
        # Output layer with as many neurons as there are categories, using softmax activation.
        # Softmax makes the output sum up to 1 so the output can be interpreted as probabilities.
        Dense(NUM_CATEGORIES, activation='softmax')
    ])

    # Compile the model by specifying the optimizer, loss function, and metrics to evaluate during training.
    # model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy']) # specified learning rate
    
    # Return the fully constructed model ready for training.
    return model
