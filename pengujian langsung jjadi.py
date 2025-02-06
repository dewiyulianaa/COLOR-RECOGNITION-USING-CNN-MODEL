import cv2
import numpy as np
from keras.models import load_model
import serial  # Import the serial library

# Load the pre-trained model
model = load_model(r"D:\Kuliah Praktik\robot sosial\arm robot\arm_robot_model(1).h5")

# Define the labels for gestures
gesture_labels = ['m', 'b', 'k', 'h']

# Initialize the webcam or video capture
cap = cv2.VideoCapture(0)

# Initialize the serial connection
arduino = serial.Serial('COM8', 9600)  # Replace 'COM3' with the correct port and baud rate

while True:
    ret, frame = cap.read()

    # Resize the frame to match the model input size                                                                                                                                                                   
    resized_frame = cv2.resize(frame, (150, 150))

    # Preprocess the frame for model prediction
    normalized_frame = resized_frame / 255.0
    input_data = np.expand_dims(normalized_frame, axis=0)

    # Predict the gesture
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction)

    # Get the predicted gesture label
    gesture_label = gesture_labels[predicted_class]

    # Display the frame with predicted gesture
    cv2.putText(frame, gesture_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Hand Gesture Recognition', frame)

    # Send the gesture label to Arduino over serial
    arduino.write(gesture_label.encode())  # Send the label as bytes

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture, close windows, and close serial connection
cap.release()
cv2.destroyAllWindows()
arduino.close()  # Close the serial connection
