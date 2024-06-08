# Import necessary functions
from prepare_data import load_data
from model import create_model

# Define parameters for the model and data
IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224
NUM_CATEGORIES = 5 
DATA_DIRECTORY = 'C:\\Users\\cikku\\Documents\\ThesisPrototype\\dataset'  # Path to data

# Load the data
train_data, validation_data = load_data(DATA_DIRECTORY)

# Create the model
model = create_model(IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CATEGORIES)

# Train the model
model.fit(
    train_data,
    epochs=250,  # Number of full passes over the entire dataset
    validation_data=validation_data
)
