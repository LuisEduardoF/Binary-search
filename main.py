N =	[4, 7, 8, 10, 11, 12, 14, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28, 32, 33, 35, 37, 38, 39, 40, 50, 51, 52, 53, 54, 55, 57, 58, 62, 64, 68, 72, 73, 76, 77, 78, 80, 81, 82, 84, 86, 88, 90, 95, 99]
# N.sort()
def binarySearch(N, nmb):
	pos = 0
	mid = int(len(N)/2)
	while True:

		if( mid == 0 ):
			return -1

		pivot = N[mid]

		if( pivot > nmb):
			N = N[:mid]		
		elif( pivot < nmb):
			pos += mid
			N = N[mid:]
		else:
			pos += mid
			return pos

		mid = int(len(N)/2)
print("Resposta:", binarySearch(N,90))
