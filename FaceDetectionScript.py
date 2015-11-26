import sys,os, argparse # argsparse basically lets us input parameter values on our commandline 
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
DEFAULT_OUTPUT_PATH = 'FaceCaptureImages/'
DEFAULT_INPUT_PATH = 'haarcascade.xml'

class VideoCapture:

	def __init__(self):
		self.count = 0
		self.argsObj = parse() # This means I'm assigning all the return values of parse fn to argsObj. argsObj is basically all the objects we are creating that are parameters
		self.faceCascade = cv2.CascadeClassifier(self.argsObj.input_path) # Our cascadeCLASSIFIER IS BASICALLY THE Haarcascade whose path we are passing from our parse fn which inturn is passing to argsObj
		self.videoSource = cv2.VideoCapture(0) # 0 implies we are defaulting to the first webcam in case we have multiple webcams attached

	def CaptureFrames(self): #capture each frame captured in a folder and name each picture captured differently
		
		while True:

			#Create unique number for each frame
			frameNumber = '%08f' % (self.count) # '%08f'is a randomn number generated everytime and it assigned itself to self.count, thats what the modulo does
			
			#Capture frame by frame
			ret, frame = self.videoSource.read() #basically reading the webcam data. It has two outputs. "Frame" returns the next frame and "ret" says if its true or not(if something's wrong witht the webcam)

			if ret == True:
				#set screen color to grey so the haar cascading can do the edge and face detection more easily
				screenColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

				#CUSTOMIZE HOW THE CASCADE DETECTS YOUR FACE, faces is basically a array. So if we have two faces in the image, it stores two face objects in our faces array
				faces = self.faceCascade.detectMultiScale(screenColor,
														scaleFactor = 1.1,	# we need to apply a cascade to each frame. it basically passes a bunch of parameters to the frame so we could start detecting the face.
														minNeighbors = 5, #HOW MANY OTHER FACES IT CAN DETECT
														minSize = (30,30), # THE SIZE OF RECTANGLE FOR THE FACE
														flags = cv2.CASCADE_SCALE_IMAGE) 
				# DISPLAY THE RESULTING FRAME

				cv2.imshow('Thats me',screenColor)

			# IF LEN(FACES) IS ZERO, MEANS THERE ARE NO FACES DETECTED
			if len(faces) ==0:
				pass
			elif len(faces)>0:
				print('Face Detected')

				# Graph the rectangle when a face is detected
				for (x,y,w,h) in faces:	#For loop cos we can have multiple faces
					cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #frame is the picture;(0,255,0) is the color green; we're passing frame

				cv2.imwrite(DEFAULT_OUTPUT_PATH + frameNumber + '.png',frame)

			#Increment count so we get unique name for each frame
			self.count+=1 

			# If escape key is pressed, the video is closed, we are going to wait only for a fraction of a sec

			if cv2.waitKey(5000) == 27:
				break

			# When everything is done release the capture(webcam) and close windows
		self.videoSource.release()
		cv2.waitKey(500)
		cv2.destroyAllWindows()
		cv2.waitKey(500)


def parse():
	parser = argparse.ArgumentParser(description = 'Cascade path for facial detection') # argument object
	#adding argument objects like input and output path
	parser.add_argument('-i','--input_path',type = str, default = DEFAULT_INPUT_PATH,help = 'cascade input path')
	parser.add_argument('-o','--output_path',type = str, default = DEFAULT_OUTPUT_PATH,help = 'OUTPUT PATH FOR PICTURES TAKEN')
	args = parser.parse_args()
	return args # what we are gonna get back is args variable which has two componants "args.input_path" and "args.output_path"


def clearImageFolder():
	if not(os.path.exists(DEFAULT_OUTPUT_PATH)):
		os.makedirs(DEFAULT_OUTPUT_PATH)
	else:
		for files in os.listdir(DEFAULT_OUTPUT_PATH):
			filePath = os.path.join(DEFAULT_OUTPUT_PATH,files)
			if os.path.isfile(filePath):
				os.unlink(filePath)
			else:
				continue

def main():
	clearImageFolder()

	#Instantiate class object

	faceDetectImplementation = VideoCapture()

	#Capture frames from class

	faceDetectImplementation.CaptureFrames()

if __name__ == '__main__':
	main()






 
 
