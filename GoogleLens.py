import io, os, re
from google.cloud import vision
from google.cloud.vision import types
import cv2


auth_file_path = "YOUR_GOOGLE_API_KEY_FILE"
file_name = "temp.png"

def get_text(im):
	"""
	Cut the text part in image
	"""
	return im[3:24, 116:288]

def get_12306_text(image_path):
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=auth_file_path
	client = vision.ImageAnnotatorClient()
	
	
def get_target_text(image_path):
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=auth_file_path
	client = vision.ImageAnnotatorClient()
	file_name = os.path.join(os.path.dirname(__file__),image_path)

	cv2_image = cv2.imread(file_name)
#	cv2.imshow("image", cv2_image)
	text_img = get_text(cv2_image)
	cv2.imwrite(file_name, text_img)	

	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)
	
	response = client.text_detection(image=image)
	texts = response.full_text_annotation
	text = texts.text
	
	s = text 
	re_words = re.compile(u"[\u4e00-\u9fa5]+")  
	res = re.findall(re_words, s) 
#	print("".join(res))
	return "".join(res)