from webapp import webApp
import random

class aleat(webApp):

	def parse(self, parsedRequest):
	        return parsedRequest.split(' ')[1]

	def process(self, parsedRequest):
	    print(parsedRequest)
	    number = random.randint(1, 1000000)
	    link = "http://localhost:1234/" + str(number)
	    return ("200 OK", '<html><body><h1><a href=' + link + '>Dame otra</a></h1></body></html>')

if __name__ == '__main__':
	testwebapp = aleat('localhost', 1234)