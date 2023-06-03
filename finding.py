class Finding:
    def __init__(self, date, username, email, species, tree, height, direction, location, info, photos):
        self.date = date
        self.username = username
        self.email = email
        self.species = species
        self.tree = tree
        self.height = height
        self.direction = direction
        self.location = location
        self.info = info
        self.photos = photos

    def cells(self):
    	cells = [self.date, self.username, self.email, self.location, self.species, self.tree, self.height, self.direction, self.info]
    	for photo in self.photos:
    		cells.append(photo)
    	return cells