from wand.image import Image as WImage

class EPS(WImage):
	def __init__(self, filename):
		super(EPS, self).__init__(filename=filename)