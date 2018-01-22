class Point():
	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

class Rect():
	# bl: bottom left point
	# tr: top right point
	def __init__(self, bl, tr):
		self.bl = bl
		self.tr = tr


def overlapping(R1, R2):
	if R2.bl.getX() >= R1.tr.getX() or R1.bl.getX() >= R2.tr.getX():
		return False
	elif R2.bl.getY() >= R1.tr.getY() or R1.bl.getY() >= R2.tr.getY():
		return False
	else:
		xl = max(R1.bl.getX(), R2.bl.getX())
		xr = min(R1.tr.getX(), R2.tr.getX())
		yt = min(R1.tr.getY(), R2.tr.getY())
		yb = max(R1.bl.getY(), R2.bl.getY())

		return (xr - xl) * (yt-yb)


def main():
	print(overlapping(Rect(Point(2,1), Point(5,5)), Rect(Point(3,2), Point(5,7))) )


if __name__ == '__main__':
	
	main()
