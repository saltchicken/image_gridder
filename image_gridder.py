from PIL import Image
import os

def grid_splitter(image_path):
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size

    # Split the image into four quarters
    top_left = image.crop((0, 0, width // 2, height // 2))
    top_right = image.crop((width // 2, 0, width, height // 2))
    bottom_left = image.crop((0, height // 2, width // 2, height))
    bottom_right = image.crop((width // 2, height // 2, width, height))

    # Save the quarters as separate image files
    top_left.save('0001.png')
    top_right.save('0002.png')
    bottom_left.save('0003.png')
    bottom_right.save('0004.png')



def grid_joiner(image_directory):
    
    # List the image files in the directory
    image_files = [f for f in os.listdir(image_directory) if f.endswith('.png')]
    
    # Get the dimensions of the image
    image = Image.open(image_directory + image_files[0])
    image_width, image_height = image.size
    
    # Create a blank canvas for the combined image
    canvas_width, canvas_height = image_width * 2, image_height * 2
    combined_image = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255))

    # Iterate through the image files and paste them onto the canvas
    for idx, image_file in enumerate(image_files):
        row = idx // 2
        col = idx % 2
        image_path = os.path.join(image_directory, image_file)
        img = Image.open(image_path)
        combined_image.paste(img, (col * image_width, row * image_height))

    # Save the combined image
    combined_image.save('combined_grid.png')

# grid_joiner('tmp/')
# grid_splitter('test.png')
