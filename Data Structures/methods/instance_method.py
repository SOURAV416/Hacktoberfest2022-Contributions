class shape:		
	def __init__(self, edge, color):        # Calling Constructor
		self.edge = edge
		self.color = color		
	def finEdges(self):                     # Instance Method
		return self.edge
	def modifyEdges(self, newedge):         # Instance Method
		self.edge = newedge
		
circle = shape(0, 'red')
square = shape(4, 'blue')
print("No. of edges for circle: "+ str(circle.finEdges()))  # Calling Instance Method
square.modifyEdges(6)                                       # Calling Instance Method
print("No. of edges for square: "+ str(square.finEdges()))
