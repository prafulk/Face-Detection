import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2,numpy

def main():
	img = cv2.imread('praful.jpg',0) #Read an image and greyscale it
									#thats what the 0 does
	#print(type(img)) gives you a numpy array

	cv2.imshow('Demo Image',img)

	exitOnKeyStroke = cv2.waitKey(0) #Wait infinite time for a key to be pressed

	if exitOnKeyStroke == 27: #Apparently 27 represents the ESC key
		cv2.destroyAllWindows()

if __name__=='__main__':
	main()
