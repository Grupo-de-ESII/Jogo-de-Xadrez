class MockTabuleiro:
	def __init__(self):
		self.estado=0
		self.resposta0=[
			[['peao', (0,1),(0,2)]],
			[['peao',(0,1),(0,3)]],
			[['peao', (1,1),(1,2)]],
			[['peao',(1,1),(1,3)]],
			[['peao', (2,1),(2,2)]],
			[['peao',(2,1),(2,3)]],
			[['peao', (3,1),(3,2)]],
			[['peao',(3,1),(3,3)]],
			[['peao', (4,1),(4,2)]],
			[['peao',(4,1),(4,3)]],
			[['peao', (5,1),(5,2)]],
			[['peao',(5,1),(5,3)]],
			[['peao', (6,1),(6,2)]],
			[['peao',(6,1),(6,3)]],
			[['peao', (7,1),(7,2)]],
			[['peao',(7,1),(7,3)]],
			#cavalos
			[['cavalo',(1,0),(0,2)]],
			[['cavalo',(1,0),(2,2)]],
			[['cavalo',(6,0),(5,2)]],
			[['cavalo',(6,0),(7,2)]]
			]
		self.resposta1=[
			[['peao', (0,1),(0,2)]],
			[['peao',(0,1),(0,3)]],
			[['peao', (1,1),(1,2)]],
			[['peao',(1,1),(1,3)]],
			[['peao', (2,1),(2,2)]],
			[['peao',(2,1),(2,3)]],
			[['peao', (3,1),(3,2)]],
			[['peao',(3,1),(3,3)]],
			[['peao', (4,3),(4,4)]],
			[['peao', (5,1),(5,2)]],
			[['peao',(5,1),(5,3)]],
			[['peao', (6,1),(6,2)]],
			[['peao',(6,1),(6,3)]],
			[['peao', (7,1),(7,2)]],
			[['peao',(7,1),(7,3)]],
			#cavalos
			[['cavalo',(1,0),(0,2)]],
			[['cavalo',(1,0),(2,2)]],
			[['cavalo',(6,0),(5,2)]],
			[['cavalo',(6,0),(7,2)]]
			]
	#mock dos possiveisMovimentos do estado inicial
	def possiveisMovimentos(self):
		#so as brancas
		if(self.estado==0)
			return self.resposta0
		if(self.estado==1)
			return self.resposta1
