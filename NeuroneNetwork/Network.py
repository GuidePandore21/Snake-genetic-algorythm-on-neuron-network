class Network:
    def __init__(self, layers) -> None:
        """Constructeur de la classe Network

        Args:
            layers (Layer): liste des Layer du Network
        """
        self.layers = layers
        self.fitness = 0
    
    def deplacement(self, x, y, distance_sf):
        """Mise à jour des valeurs des InputNeurones pour le déplacement du Snake

        Args:
            x (int): position en x du Snake
            y (int): position en y du Snake
            distance_sf (int): distance manhattan du Snake par rapport à la pomme
        """
        self.layers[0].neurones[0].inputData = x
        self.layers[0].neurones[1].inputData = y
        self.layers[0].neurones[4].inputData = distance_sf
    
    def mangerPomme(self, foodx, foody, fitness):
        """ajoute une valeurs fitness au score du Network et modifie les valeurs d'InputNeurones pour qu'elles correspondent à la nouvelle position de la pomme

        Args:
            foodx (_type_): position en x de la pomme
            foody (_type_): position en y de la pomme
            fitness (_type_): valeur à ajouter au score
        """
        self.fitness += fitness
        self.layers[0].neurones[2].inputData = foodx
        self.layers[0].neurones[3].inputData = foody