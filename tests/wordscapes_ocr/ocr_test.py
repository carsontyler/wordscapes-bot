import cv2
from wordscapes_bot.wordscapes_ocr.get_image import screenshot
from wordscapes_bot.wordscapes_ocr import get_formatted_screenshot
from wordscapes_bot.wordscapes_ocr import ocr_characters
from wordscapes_bot.wordscapes_ocr import ocr_bounding_boxes

screenshot_image = screenshot((1621, 347, 1824, 547))
formatted_image = get_formatted_screenshot((1621, 347, 1824, 547))
bounding_boxes = ocr_bounding_boxes(formatted_image)

characters = ocr_characters(formatted_image)
print([character for character, pos in characters])
print(characters)

cv2.imshow('screenshot', cv2.cvtColor(screenshot_image, cv2.COLOR_BGR2RGB))
cv2.imshow('formatted image', formatted_image)
cv2.imshow('bounding boxes', bounding_boxes)

while True:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()