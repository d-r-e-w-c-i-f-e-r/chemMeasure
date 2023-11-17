import cv2
import numpy as np

# og value was 227

def measure_pixels(image_path, reference_length):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours to find the reference scale
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the contour has four vertices (assuming it's a rectangular shape)
        # if len(approx) == 4:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # Check if the area is within a reasonable range
        if area > 500 and area < 10000:
            # Draw the contour on the original image
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

            # Calculate the pixel length of the reference scale
            pixels_per_unit = area / reference_length
            print(f"Pixels per unit: {pixels_per_unit}")

    # Display the image with the reference scale contour
    cv2.imshow("Image with Reference Scale", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = "../resources/example.PNG"  # Replace with the path to your image
reference_length = 50.0  # Replace with the known length of your reference scale (in the same unit as your measurements)

measure_pixels(image_path, reference_length)
