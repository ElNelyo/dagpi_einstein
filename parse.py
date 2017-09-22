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
teamlist = xmldoc.getElementsByTagName('team')

# Inventions list
inventionslist = xmldoc.getElementsByTagName('inventions')

# Rewards list
rewardlist = xmldoc.getElementsByTagName('rewards')

myListInventor = []
myListInvention = []

# For each inventor in inventors list
for item in teamlist:
    colorlist = item.getElementsByTagName('color')  # get his color
    myColor = colorlist[0].firstChild.nodeValue

    teamlist = item.getElementsByTagName('inventor')

    for inventor in teamlist:

        name = inventor.getElementsByTagName('name')  # get his name
        points = inventor.getElementsByTagName('points_target')

        startphysics = inventor.getElementsByTagName('physics')  # Get physics knowledge
        startmathematics = inventor.getElementsByTagName('mathematics')  # Get maths knowledge
        startchemistry = inventor.getElementsByTagName('chemistry')  # Get chemistry knowledge
        startmechanics = inventor.getElementsByTagName('mechanics')  # Get mechanics knowledge

        # startknowledge var in inventor class

        startknowledge = [int(startphysics[0].firstChild.nodeValue),
                          int(startchemistry[0].firstChild.nodeValue),
                          int(startmechanics[0].firstChild.nodeValue),
                          int(startmathematics[0].firstChild.nodeValue)]

        knowledgetargetlist = inventor.getElementsByTagName('target_knowledge')  # Get target knowledge (list)

        # For each knowledge of Target knowledges
        for knowledgetarget in knowledgetargetlist:
            targetphysics = knowledgetarget.getElementsByTagName('physics')  # Get physics knowledge
            targetmathematics = knowledgetarget.getElementsByTagName('mathematics')  # Get maths knowledge
            targetmechanics = knowledgetarget.getElementsByTagName('mechanics')  # Get mechanics knowledge
            targetchemistry = knowledgetarget.getElementsByTagName('chemistry')  # Get chemistry knowledge

        targetknowledge = [int(targetphysics[0].firstChild.nodeValue),
                           int(targetchemistry[0].firstChild.nodeValue),
                           int(targetmechanics[0].firstChild.nodeValue),
                           int(targetmathematics[0].firstChild.nodeValue)]

        strName = name[0].firstChild.nodeValue
        strPoints = points[0].firstChild.nodeValue

        # Inventor object
        myInventor = Inventor.Inventor(strName, strPoints, startknowledge, targetknowledge)
        myListInventor.append(myInventor)

        print("[Inventor]")
        print(myInventor.name)
        print("\n   [Start Knowledge]")
        print("   " + str(startknowledge))
        print("\n   [Target Knowledge]")
        print("   " + str(targetknowledge))
        print("\n   [Target Points]")
        print("   " + myInventor.points)
        print(" ")
        myTeam = Team.Team(myListInventor, myColor)
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
        startphysics = invention.getElementsByTagName('physics')  # Get physics knowledge
        startchemistry = invention.getElementsByTagName('chemistry')  # Get physics knowledge
        startmechanics = invention.getElementsByTagName('mechanics')  # Get mechanics knowledge
        startmathematics = invention.getElementsByTagName('mathematics')  # Get maths knowledge
        classification = invention.getElementsByTagName('classification')  # Get classification

        knowledge = [int(startphysics[0].firstChild.nodeValue),
                     int(startchemistry[0].firstChild.nodeValue),
                     int(startmechanics[0].firstChild.nodeValue),
                     int(startmathematics[0].firstChild.nodeValue)
                     ]
        agetmp = 0
        for k in knowledge:
            agetmp = agetmp + k

        # Invention Object

        nametmp = name[0].firstChild.nodeValue
        myInvention = Invention.Invention(nametmp, classification, knowledge)
        myListInvention.append(myInvention)

        myInvention.age = int((agetmp-3)/2)

        print("Age : " + str(myInvention.age))

        print("[Name] ")
        print(name[0].firstChild.nodeValue)
        print(" ")
        print("[Knowledge]")

        print("physics : " + str(knowledge[0]))
        print("chemistry : " + str(knowledge[1]))
        print("mechanics : " + str(knowledge[2]))
        print("mathematics : " + str(knowledge[3]))

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
            print("Availability object created")

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
            print("Classification object created")

print("\n\n\n")
test = myListInvention[0]
print(test.name)
print(test.knowledge)
