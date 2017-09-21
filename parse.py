# IMPORT XML DOM
from xml.dom import minidom
import Inventor
import Knowledge
import InventorKnowledge
import InventorKnowledgeTarget
import Invention
import Token
import InventionKnowledge
import Team

# Fichier xml charge
xmldoc = minidom.parse('data.xml')

# Liste des inventeur
inventorlist = xmldoc.getElementsByTagName('team')

# Liste des inventions
inventionslist = xmldoc.getElementsByTagName('inventions')

# Liste des recompenses
rewardlist = xmldoc.getElementsByTagName('rewards')

myListInventor = []

# Pour chaque inventeur dans la liste des inventions
for item in inventorlist:
    colorlist = item.getElementsByTagName('color')  # On recupere sa couleur
    myColor = (colorlist[0].firstChild.nodeValue)



    inventorlist = item.getElementsByTagName('inventor')



    for inventor in inventorlist:

        name = inventor.getElementsByTagName('name')  # On recupere son nom
        points = inventor.getElementsByTagName('points_target')


        # Objet Inventeur
        myInventor = Inventor.Inventor(name, points)
        myListInventor.append(myInventor)

        physics = inventor.getElementsByTagName('physics')  # On recupere sa competence en physique
        mathematics = inventor.getElementsByTagName('mathematics')  # On recupere sa competence en math
        chemistry = inventor.getElementsByTagName('chemistry')  # On recupere sa competence en chimie
        mechanics = inventor.getElementsByTagName('mechanics')  # On recupere sa competence en mecanique

        # Objet InventorKnowledge

        myInventorKnowledge = InventorKnowledge.InventorKnowledge(myInventor, Knowledge.Knowledge.Physics, physics)
        myInventorKnowledge = InventorKnowledge.InventorKnowledge(myInventor, Knowledge.Knowledge.Mathematics,mathematics)
        myInventorKnowledge = InventorKnowledge.InventorKnowledge(myInventor, Knowledge.Knowledge.Chemistry, chemistry)
        myInventorKnowledge = InventorKnowledge.InventorKnowledge(myInventor, Knowledge.Knowledge.Mecanics, mechanics)

        knowledgetargetlist = inventor.getElementsByTagName(
            'target_knowledge')  # On recupere ses target competences (liste)

        print("[Name]")
        print(name[0].firstChild.nodeValue)
        print(" ")
        print("[Knowledge]")
        print("physique : " + physics[0].firstChild.nodeValue)
        print("chemistry : " + chemistry[0].firstChild.nodeValue)
        print("mechanics : " + mechanics[0].firstChild.nodeValue)
        print("mathematics : " + mathematics[0].firstChild.nodeValue)
        print(" ")
        print("[Point target]")
        print(points[0].firstChild.nodeValue)
        print(" ")
        print("[Target Knowledge]")

        # Pour chaque competence target de sa liste de competence target
        for knowledgetarget in knowledgetargetlist:
            physicstarget = knowledgetarget.getElementsByTagName('physics')  # On recupere sa competence en physique
            mathematicstarget = knowledgetarget.getElementsByTagName(
                'mathematics')  # On recupere sa competence en mathematique
            mechanicstarget = knowledgetarget.getElementsByTagName(
                'mechanics')  # On recupere sa competence en mecanique
            chemistrytarget = knowledgetarget.getElementsByTagName('chemistry')  # On recupere sa competence en chimie

            # Objet InventorKnowledge Target

            myInventorKnowledgeTarget = InventorKnowledgeTarget.InventorKnowledgeTarget(myInventor,
                                                                                        Knowledge.Knowledge.Physics,
                                                                                        physics)
            myInventorKnowledgeTarget = InventorKnowledgeTarget.InventorKnowledgeTarget(myInventor,
                                                                                        Knowledge.Knowledge.Mathematics,
                                                                                        mathematics)
            myInventorKnowledgeTarget = InventorKnowledgeTarget.InventorKnowledgeTarget(myInventor,
                                                                                        Knowledge.Knowledge.Chemistry,
                                                                                        chemistry)
            myInventorKnowledgeTarget = InventorKnowledgeTarget.InventorKnowledgeTarget(myInventor,
                                                                                        Knowledge.Knowledge.Mecanics,
                                                                                        mechanics)

            print("physique : " + physicstarget[0].firstChild.nodeValue)
            print("chemistry : " + chemistrytarget[0].firstChild.nodeValue)
            print("mechanics : " + mechanicstarget[0].firstChild.nodeValue)
            print("mathematics : " + mathematicstarget[0].firstChild.nodeValue)

        print(" ")
        myTeam = Team.Team(myListInventor,myColor)
        """"for team in myTeam.inventors:
        print("LDOKDODSOKDKS33"+team.name[0].firstChild.nodeValue)
        print("LDOKDODSOKDKS33"+myTeam.color)"""


# Pour chaque invention dans la liste des inventions
for item in inventionslist:
    print("-------------------")
    print("INVENTION")
    print("-------------------")
    print(" ")

    inventionlist = item.getElementsByTagName('invention')  # On recupere une invention

    for invention in inventionlist:
        name = invention.getElementsByTagName('name')  # On recupere son nom
        physics = invention.getElementsByTagName('physics')  # On recupere sa competence en physique
        chemistry = invention.getElementsByTagName('chemistry')  # On recupere sa competence en chimie
        mechanics = invention.getElementsByTagName('mechanics')  # On recupere sa competence en mecanique
        mathematics = invention.getElementsByTagName('mathematics')  # On recupere sa competence en mathematique
        classification = invention.getElementsByTagName('classification')  # On recupere sa classification

        # Objet Invention
        myInvention = Invention.Invention(name, classification)

        # ObjetInventionKnowledge

        myInventionKnowledge = InventionKnowledge.InventionKnowledge(Knowledge.Knowledge.Physics, Invention)
        myInventionKnowledge = InventionKnowledge.InventionKnowledge(Knowledge.Knowledge.Mathematics, Invention)
        myInventionKnowledge = InventionKnowledge.InventionKnowledge(Knowledge.Knowledge.Chemistry, Invention)
        myInventionKnowledge = InventionKnowledge.InventionKnowledge(Knowledge.Knowledge.Mecanics, Invention)

        print("[Name] ")
        print(name[0].firstChild.nodeValue)
        print(" ")
        print("[Knowledge]")
        print("physics : " + physics[0].firstChild.nodeValue)
        print("chemistry : " + chemistry[0].firstChild.nodeValue)
        print("mechanics : " + mechanics[0].firstChild.nodeValue)
        print("mathematics : " + mathematics[0].firstChild.nodeValue)

        print(" ")
        print("[Classification]")
        print("classification : " + classification[0].firstChild.nodeValue)
        print(" ")

        print("~")

# Objet Token



# Pour chaque recompense dans la liste de recompenses
for item in rewardlist:
    progresspointlist = item.getElementsByTagName('progress_reward')  # On recupere la liste des progresspoint
    pointrewardlist = item.getElementsByTagName('point_reward')  # On recupere la liste des pointreward
    availabilityrewardlist = item.getElementsByTagName(
        'availability_reward')  # On recupere la liste des availibilityreward
    additionalknowledgerewardlist = item.getElementsByTagName(
        'additional_knowledge_reward')  # On recupere la liste des additionalknowledgereward
    classificationrewardlist = item.getElementsByTagName(
        'classification_reward')  # On recupere la liste des classificationreward

    print("[Progress Reward]")
    # Pour chaque progresspoint de la liste de progresspoint
    for progresspoint in progresspointlist:
        reward = progresspoint.getElementsByTagName('number')  # On recupere son nombre
        level = progresspoint.getElementsByTagName('level')  # On recupere son niveau
        number = int(float(reward[0].firstChild.nodeValue))
        type = str(level[0].firstChild.nodeValue)
        for a in range(0, number):
            # Objet point reward
            myProgressReward = Token.Token("progressreward" + type)
            print("Objet progressward cree")
        print("Type :" + "progressreward" + type)
        print("reward " + level[0].firstChild.nodeValue + " : " + reward[0].firstChild.nodeValue)
    print(" ")
    print("[Points Reward]")

    # Pour chaque pointreward de la liste de pointreward
    for pointreward in pointrewardlist:
        reward = pointreward.getElementsByTagName('number')  # On recupere son nombre
        level = pointreward.getElementsByTagName('point')  # On recupere ses points
        number = int(float(reward[0].firstChild.nodeValue))
        type = str(level[0].firstChild.nodeValue)
        for a in range(0, number):
            # Objet point reward
            myPointReward = Token.Token("pointreward" + type)
            print("Objet pointreward cree")

        print("Type :" + "pointreward" + type)
        print("reward " + level[0].firstChild.nodeValue + " : " + reward[0].firstChild.nodeValue)

    print(" ")
    print("[Availability Reward]")

    # Pour chaque availabilityreward de la liste de availabilityreward
    for availabilityreward in availabilityrewardlist:
        print(availabilityreward.firstChild.data)  # On recupere son nombre
        number = int(float(availabilityreward.firstChild.data))
        for a in range(0, number):
            myToken = Token.Token("availabilityreward")
            print("Objet availability cree")

    print(" ")
    print("[Additionalknowledge Reward]")

    # Pour chaque availabilityreward de la liste de availabilityreward
    for additionalknowledgereward in additionalknowledgerewardlist:
        print(additionalknowledgereward.firstChild.data)  # On recupere son nombre
        number = int(float(additionalknowledgereward.firstChild.data))
        for a in range(0, number):
            myToken = Token.Token("additionalknowledger")
            print("Objet additionalknowledger cree")
    print(" ")
    print("[Classification Reward]")
    # Pour chaque availabilityreward de la liste de availabilityreward
    for classificationreward in classificationrewardlist:
        print(classificationreward.firstChild.data)  # On recupere son nombre
        number = int(float(classificationreward.firstChild.data))
        for a in range(0, number):
            myToken = Token.Token("classificationreward")
            print("Objet classification cree")




