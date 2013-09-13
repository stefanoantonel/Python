

class ArgsParser():
	def get_url(self, args):
		result = ""
		for i in args:
			if i.startswith("--url="):
				result = i[6:]
				if(not result.startswith("http")):
					result="http://"+result
		return result
	
	def get_ext(self, args):
		result = ""
		for i in args:
			if i.startswith("--ext="):
				result = i[6:]
				if(not result.startswith(".")):
					result="."+result
		return result

def main():
	
	return 0

if __name__ == '__main__':
	main()

