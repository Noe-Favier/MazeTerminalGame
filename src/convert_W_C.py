#WALL (int) to CHAR converter
def traduct(e):
	"""
	s = int entre 0 & 4
	"""
	
	w = '░' # 1 = mur
	n = ' ' # 0 = passage
	j = '☺' # 2 = joueur
	s = '▼' # 3 = sortie
	x = '?' # ? = case inconnue
	rt = None

	
	if  (e == 0):
		rt = n
	elif(e == 1):
		rt = w
	elif(e == 2):
		rt = j
	elif(e == 3):
		rt = s
	else:
		rt = x


	return rt
