from PIL import Image
import math

def vector_length(vector):
  return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def points_distance(point1, point2):
  return vector_length((point1[0] - point2[0],point1[1] - point2[1]))

def clamp(value, minimum, maximum):
  return max(min(value,maximum),minimum)

## Warps an image accoording to given points and shift vectors.
#
#  @param image input image
#  @param points list of (x, y, dx, dy) tuples
#  @return warped image

def warp(image, point):
  result = img = Image.new("RGB",image.size,"black")
  if point[0] > image.size[0] or point[2] > image.size[0] or point[1] > image.size[1] or point[3] > image.size[1]:
    print("Point given is out of range")
    return
  image_pixels = image.load()
  result_pixels = result.load()

  for y in range(image.size[1]):
    for x in range(image.size[0]):

      offset = [0,0]

      point_position = (point[0] + point[2],point[1] + point[3])
      shift_vector = (point[2],point[3])

      # warping formula
      helper = 1.0 / (3 * (points_distance((x,y),point_position) / vector_length(shift_vector)) ** 4 + 1)


      offset[0] -= helper * shift_vector[0]
      offset[1] -= helper * shift_vector[1]

      # coordinates for new pixels
      coords = (clamp(x + int(offset[0]),0,image.size[0] - 1),clamp(y + int(offset[1]),0,image.size[1] - 1))

      result_pixels[x,y] = image_pixels[coords[0],coords[1]]

  return result

image = Image.open("movie.png")
print("Now warping image...")
image = warp(image, (890, 590, 200, 300))
image.save("testwarp_two.png","PNG")