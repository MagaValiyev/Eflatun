import cv2
import numpy as np

def detect_triangles(image_path):
    # Read the image
    color = cv2.imread(image_path)
    cv2.namedWindow("input")
    cv2.imshow("input", color)

    # Convert it to gray
    gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    canny = cv2.Canny(gray, 50, 150)
    canny_display = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)  # Convert to BGR for display
    cv2.namedWindow("canny")
    cv2.imshow("canny", canny_display)

    # Find contours in the Canny image
    contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours to find triangles
    triangles = []
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # If the contour has three vertices, it is a triangle
        if len(approx) == 3:
            triangles.append(approx)

    # Draw the detected triangles
    cv2.drawContours(color, triangles, -1, (0, 255, 0), 2)

    cv2.namedWindow("output")
    cv2.imshow("output", color)
    cv2.imwrite("detected_triangles.png", color)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "triangleimage.png"  # Replace with the path to your image
    detect_triangles(image_path)
