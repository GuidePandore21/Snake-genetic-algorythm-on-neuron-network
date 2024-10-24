from NeuroneNetwork.Network import Network
from NeuroneNetwork.Layer import Layer
from NeuroneNetwork.Neurone import Neurone
from NeuroneNetwork.InputNeurone import InputNeurone
from NeuroneNetwork.OutputNeurone import OutputNeurone
from AlgorithmeGenetique import inputLayerGenerator

def saveNetwork(Network, cheminFichier):
    """Sauvegarde dans un fichier txt un Network

    Args:
        Network (Network): Network à sauvegarder
        cheminFichier (String): chemin du fichier (chemin relatif) ne pas oublier d'ajouter l'extension .txt
    """
    with open(cheminFichier, "w") as fichier:
        fichier.write(str(0) + "\n")
        fichier.write(str(len(Network.layers)) + "\n")
        
        for i in range(1, len(Network.layers)):
            fichier.write(Network.layers[i].label + "\n")
            fichier.write(str(len(Network.layers[i].neurones)) + "\n")
            
            for j in range(len(Network.layers[i].neurones)):
                fichier.write(Network.layers[i].neurones[j].label + "\n")
                if i != 0:
                    fichier.write(str(Network.layers[i].neurones[j].bias) + "\n")
                    fichier.write(str(len(Network.layers[i].neurones[j].inputs)) + "\n")
                    for k in range(len(Network.layers[i].neurones[j].inputs)):
                        fichier.write(Network.layers[i].neurones[j].inputs[k][0].label + " " + str(Network.layers[i].neurones[j].inputs[k][1]) + "\n")

def loadNetwork(cheminFichier, INPUTS, OUTPUTS):
    """Créer / Charge un Network à partir d'un txt

    Args:
        cheminFichier (string): chemin du fichier txt
        INPUTS ([int]): liste des inputs du Network
        OUTPUTS ([float]): liste des outputs du Network

    Returns:
        Network: retourne le Network créer / charger
    """
    curseur = 0
    with open(cheminFichier, "r") as fichier:
        tempLignes = fichier.readlines()
        lignes = []
        for ligne in tempLignes:
            lignes.append(ligne.replace("\n", ""))
            
        listeLayer = []
        listeLayer.append(inputLayerGenerator(INPUTS))
        
        fitness = lignes[curseur]
        print(fitness)
        curseur += 1
        print(lignes[curseur])
        for _ in range(int(lignes[curseur]) - 1): # Layers
            curseur += 1
            labelLayer = lignes[curseur]
            print(labelLayer)
            curseur += 1
            listeNeurones = []
            nbNeurone = int(lignes[curseur])
            print(nbNeurone)
            for _ in range(nbNeurone): # Neurones
                curseur += 1
                labelNeurone = lignes[curseur]
                print(labelNeurone)
                curseur += 1
                biasNeurone = lignes[curseur]
                print(biasNeurone)
                curseur += 1
                inputs = []
                print(lignes[curseur])
                for i in range(int(lignes[curseur])): # Inputs
                    curseur += 1
                    input = lignes[curseur].split(" ")
                    print(input)
                    for neurone in listeLayer[len(listeLayer) - 1].neurones:
                        if neurone.label == input[0]:
                            inputs.append([neurone, float(input[1])])
                            break
                if i == nbNeurone - 1:
                    neurone = OutputNeurone(labelNeurone, biasNeurone, inputs, OUTPUTS)
                else:
                    neurone = Neurone(labelNeurone, biasNeurone, inputs)
                listeNeurones.append(neurone)
            layer = Layer(labelLayer, listeNeurones)
            listeLayer.append(layer)
            network = Network(listeLayer)
            network.fitness = fitness
        return network