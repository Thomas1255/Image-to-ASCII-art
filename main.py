import cv2 as cv
MAX_BRIGHTNESS = 255

def main ():
    # Define the path for the image file
    image_path = "images/"
    image_name = ""
    image_name = input("Enter file name exactly including the file type .png, .jpg, etc: ")
    image_path += image_name

    # Read the image from specified path and convert the image to grayscale 
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

    # Check if the image was successfully loaded
    if image is not None:
        # Display image
        print("Original size:", image.shape[1], "x", image.shape[0])
        cv.imshow('Image', image)
        cv.waitKey(0)
        cv.destroyAllWindows
    else:
        print("Error: No matching file name. Remember to check capilization or include .png, .jpg, etc.")
        return -1

    # Resize the image relative to its image size
    if (image.shape[0] + image.shape[1] > 10000):
        scale_factor = 0.05
    elif (image.shape[0] + image.shape[1] > 1000):
        scale_factor = 0.3
    elif (image.shape[0] + image.shape[1] > 500):
        scale_factor = 0.5
    else:
        scale_factor = 0.7
        
    resized_image = cv.resize(image, None, fx = scale_factor, fy = scale_factor) 

    # Get dimensions of the resized image
    height = resized_image.shape[0]
    width = resized_image.shape[1]
    print("Resized to", width, "x", height)

    # Write out the ASCII art
    ascii_art = ""
    ascii_characters = ".:l|nxQ#8!$"

    for y in range(height):
        for x in range(width):
            # Get the brightness value of the pixel
            brightness = resized_image[y, x] 

            # Write associated ascii char with its brightness
            ascii_index = int(brightness / MAX_BRIGHTNESS * (len(ascii_characters) - 1))   # a decimal between 0-1 * length of ASCII string
            ascii_art += ascii_characters[ascii_index]
        ascii_art += '\n'    

    # Save the ASCII art to a txt file
    image_name += "_ascii_art.txt"
    with open(image_name, 'w') as file:
        file.write(ascii_art)
    print("ASCII art text file generated.")

    return 0

main()

