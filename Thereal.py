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

def warp(image, points):
  result = img = Image.new("RGB",image.size,"black")

  image_pixels = image.load()
  result_pixels = result.load()

  for y in range(image.size[1]):
    for x in range(image.size[0]):

      offset = [0,0]

      for point in points:
        point_position = (point[0] + point[2],point[1] + point[3])
        shift_vector = (point[2],point[3])

        helper = 1.0 / (3 * (points_distance((x,y),point_position) / vector_length(shift_vector)) ** 4 + 1)

        offset[0] -= helper * shift_vector[0]
        offset[1] -= helper * shift_vector[1]

      coords = (clamp(x + int(offset[0]),0,image.size[0] - 1),clamp(y + int(offset[1]),0,image.size[1] - 1))

      result_pixels[x,y] = image_pixels[coords[0],coords[1]]

  return result

image = Image.open("tester.png")
image = warp(image,[(210,296,100,0), (101,97,-30,-10), (77,473,50,-100)])
image.save("testwarp.png","PNG")