## 44.Regex in python to put spaces between words starting with capital letters.
import re

def putSpace(input):
	
	words = re.findall('[A-Z][a-z]*', input)
	for i in range(0,len(words)):
	  words[i]=words[i][0].lower()+words[i][1:]
	print(' '.join(words))
	


if __name__ == "__main__":
	input = 'BruceWayneIsBatman'
	putSpace(input)
