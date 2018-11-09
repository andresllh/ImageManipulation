# Imported PIL Library from PIL import Image
from PIL import Image
# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')


# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image


# Get the pixel from the given image
def get_pixel(image, i, j):
  # Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None

  # Get Pixel
  pixel = image.getpixel((i, j))
  return pixel


def change_background(image, background):
    width, height = image.size
    new = create_image(width, height)
    pixels = new.load()
    print(image.size, background.size)
    for i in range(width):
        for j in range(height):
            pixel = get_pixel(image, i, j)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            try:
                pixel_background = get_pixel(background, i, j)
                red_b = pixel_background[0]
                green_b = pixel_background[1]
                blue_b = pixel_background[2]
            except:
                pass
            
            if green > 70 and red > 10 and blue > 30 and blue < 60 and red < 60: # greenscreen
                pixels[i,j] = (int(red_b), int(green_b), int(blue_b))
            
            else:
                pixels[i,j] = (int(red), int(green), int(blue))
                
    return new
            

# Main
if __name__ == "__main__":
  # Load Image (JPEG/JPG needs libjpeg to load)
  original = open_image('test.png')
  background = open_image('eiffel_tower.png')
  print('Now converting...')
  new = change_background(original, background)
  print('Done')
  save_image(new, 'converted_test_eiffel_tower.png')
