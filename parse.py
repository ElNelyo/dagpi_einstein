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

# Charged XML File
xmldoc = minidom.parse('data.xml')

# Inventors list
inventorlist = xmldoc.getElementsByTagName('team')

# Inventions list
inventionslist = xmldoc.getElementsByTagName('inventions')

# Rewards list
rewardlist = xmldoc.getElementsByTagName('rewards')

myListInventor = []

# For each inventor in inventors list
for item in inventorlist:
    colorlist = item.getElementsByTagName('color')  # get his color
    myColor = colorlist[0].firstChild.nodeValue

    inventorlist = item.getElementsByTagName('inventor')

    for inventor in inventorlist:

        name = inventor.getElementsByTagName('name')  # get his name
        points = inventor.getElementsByTagName('points_target')

        # Inventor object
        myInventor = Inventor.Inventor(name, points)
        myListInventor.append(myInventor)

        physics = inventor.getElementsByTagName('physics')  # Get physics knowledge
        mathematics = inventor.getElementsByTagName('mathematics')  # Get maths knowledge
        chemistry = inventor.getElementsByTagName('chemistry')  # Get chemistry knowledge
        mechanics = inventor.getElementsByTagName('mechanics')  # Get mechanics knowledge

        # InventorKnowledge Object

        myInventorKnowledge = InventorKnowledge.InventorKnowledge(myInventor, Knowledge.Knowledge.physics, physics)
        myInventorKnowledge = InventorKnowledge.InventorKnowledge(myInventor, Knowledge.Knowledge.mathematics,mathematics)
        myInventorKnowledge = InventorKnowledge.InventorKnowledge(myInventor, Knowledge.Knowledge.chemistry, chemistry)
        myInventorKnowledge = InventorKnowledge.InventorKnowledge(myInventor, Knowledge.Knowledge.mechanics, mechanics)

        knowledgetargetlist = inventor.getElementsByTagName(
            'target_knowledge')  # Get target knowledge (list)

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

        # For each knowledge of Target knowledges
        for knowledgetarget in knowledgetargetlist:
            physicstarget = knowledgetarget.getElementsByTagName('physics')  # Get physics knowledge
            mathematicstarget = knowledgetarget.getElementsByTagName(
                'mathematics')  # Get maths knowledge
            mechanicstarget = knowledgetarget.getElementsByTagName(
                'mechanics')  # Get mechanics knowledge
            chemistrytarget = knowledgetarget.getElementsByTagName('chemistry')  # Get chemistry knowledge

            # InventorKnowledge Target Object

            myInventorKnowledgeTarget = InventorKnowledgeTarget.InventorKnowledgeTarget(myInventor,
                                                                                        Knowledge.Knowledge.physics,
                                                                                        physics)
            myInventorKnowledgeTarget = InventorKnowledgeTarget.InventorKnowledgeTarget(myInventor,
                                                                                        Knowledge.Knowledge.mathematics,
                                                                                        mathematics)
            myInventorKnowledgeTarget = InventorKnowledgeTarget.InventorKnowledgeTarget(myInventor,
                                                                                        Knowledge.Knowledge.chemistry,
                                                                                        chemistry)
            myInventorKnowledgeTarget = InventorKnowledgeTarget.InventorKnowledgeTarget(myInventor,
                                                                                        Knowledge.Knowledge.mechanics,
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


# For each invention in inventions list
for item in inventionslist:
    print("-------------------")
    print("INVENTION")
    print("-------------------")
    print(" ")

    inventionlist = item.getElementsByTagName('invention')  # Get invention

    for invention in inventionlist:
        name = invention.getElementsByTagName('name')  # Get name
        physics = invention.getElementsByTagName('physics')  # Get physics knowledge
        chemistry = invention.getElementsByTagName('chemistry')  # Get physics knowledge
        mechanics = invention.getElementsByTagName('mechanics')  # Get mechanics knowledge
        mathematics = invention.getElementsByTagName('mathematics')  # Get maths knowledge
        classification = invention.getElementsByTagName('classification')  # Get classification

        # Invention Object
        myInvention = Invention.Invention(name, classification)

        # InventionKnowledge Object

        myInventionKnowledgePhysics = InventionKnowledge.InventionKnowledge(Knowledge.Knowledge.physics, Invention)
        myInventionKnowledgeMathematics = InventionKnowledge.InventionKnowledge(Knowledge.Knowledge.mathematics, Invention)
        myInventionKnowledgeChemistry = InventionKnowledge.InventionKnowledge(Knowledge.Knowledge.chemistry, Invention)
        myInventionKnowledgeMechanics = InventionKnowledge.InventionKnowledge(Knowledge.Knowledge.mechanics, Invention)

        agetmp = int(chemistry[0].firstChild.nodeValue) + \
                 int(physics[0].firstChild.nodeValue) + \
                 int(mathematics[0].firstChild.nodeValue) + \
                 int(mechanics[0].firstChild.nodeValue)

        myInvention.age = int((agetmp-3)/2)

        print("WWWWWWWWWWWWWWWWWWWWWWWWWWW")
        print(myInvention.age)

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

# Token Object

# For each reward in rewards list
for item in rewardlist:
    progresspointlist = item.getElementsByTagName('progress_reward')  # Get progresspoints list
    pointrewardlist = item.getElementsByTagName('point_reward')  # Get pointrewards list
    availabilityrewardlist = item.getElementsByTagName(
        'availability_reward')  # Get availibilityreward list
    additionalknowledgerewardlist = item.getElementsByTagName(
        'additional_knowledge_reward')  # Get additionalknowledgereward list
    classificationrewardlist = item.getElementsByTagName(
        'classification_reward')  # Get classificationreward list

    print("[Progress Reward]")
    # For each progresspoint in progresspoint list
    for progresspoint in progresspointlist:
        reward = progresspoint.getElementsByTagName('number')  # Get number
        level = progresspoint.getElementsByTagName('level')  # Get level
        number = int(float(reward[0].firstChild.nodeValue))
        type = str(level[0].firstChild.nodeValue)
        for a in range(0, number):
            # Point reward object
            myProgressReward = Token.Token("progressreward" + type)
            print("Objet progressward cree")
        print("Type :" + "progressreward" + type)
        print("reward " + level[0].firstChild.nodeValue + " : " + reward[0].firstChild.nodeValue)
    print(" ")
    print("[Points Reward]")

    # For each pointreward in pointreward list
    for pointreward in pointrewardlist:
        reward = pointreward.getElementsByTagName('number')  # Get number
        level = pointreward.getElementsByTagName('point')  # Get points
        number = int(float(reward[0].firstChild.nodeValue))
        type = str(level[0].firstChild.nodeValue)
        for a in range(0, number):
            # Point reward object
            myPointReward = Token.Token("pointreward" + type)
            print("Objet pointreward cree")

        print("Type :" + "pointreward" + type)
        print("reward " + level[0].firstChild.nodeValue + " : " + reward[0].firstChild.nodeValue)

    print(" ")
    print("[Availability Reward]")

    # For each availabilityreward in availabilityreward list
    for availabilityreward in availabilityrewardlist:
        print(availabilityreward.firstChild.data)  # Get number
        number = int(float(availabilityreward.firstChild.data))
        for a in range(0, number):
            myToken = Token.Token("availabilityreward")
            print("Objet availability cree")

    print(" ")
    print("[Additionalknowledge Reward]")

    # For each availabilityreward in availabilityreward list
    for additionalknowledgereward in additionalknowledgerewardlist:
        print(additionalknowledgereward.firstChild.data)  # Get number
        number = int(float(additionalknowledgereward.firstChild.data))
        for a in range(0, number):
            myToken = Token.Token("additionalknowledger")
            print("Objet additionalknowledger cree")
    print(" ")
    print("[Classification Reward]")
    # For each availabilityreward in availabilityreward list
    for classificationreward in classificationrewardlist:
        print(classificationreward.firstChild.data)  # Get number
        number = int(float(classificationreward.firstChild.data))
        for a in range(0, number):
            myToken = Token.Token("classificationreward")
            print("Objet classification cree")




