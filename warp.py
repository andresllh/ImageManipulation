# Imported PIL Library from PIL import Image
from PIL import Image
import math
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


#x,y differences
def pointsdistance(point1, point2):
  return (point1[0] - point2[0],point1[1] - point2[1])

#warp a image given an image and two points
#p1 and p2 are x, y values
def warp(image, point):
    newpix = Image.new("RGB", image.size, "white")

    orgpix = image.load()
    newpix = newpix.load()


    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if (x > point[0] and x< point[2]) and (y > point[1] and y< point[3]):
                newpix[x,y] = orgpix[point[0], point[1]]
            newpix[x,y] = orgpix[x,y]


    return newpix



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
  #background = open_image('eiffel_tower.png')
  warped = warp(original, (101, 97, -30, -10))
  print('Now converting...')
  #new = change_background(original, background)
  #print('Done')
  save_image(warped, 'warped.png')
