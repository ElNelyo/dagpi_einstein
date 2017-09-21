#IMPORT XML DOM
from xml.dom import minidom

#TestPushDepuisPyCharm

#Fichier xml charge
xmldoc = minidom.parse('data.xml')

#Liste des inventeur
inventorlist = xmldoc.getElementsByTagName('team')

#Liste des inventions
inventionslist = xmldoc.getElementsByTagName('inventions')

#Liste des recompenses
rewardlist = xmldoc.getElementsByTagName('rewards')



#Pour chaque inventeur dans la liste des inventions
for item in inventorlist:
    colorlist = item.getElementsByTagName('color') #On recupere sa couleur
    for color in colorlist:
        print("-------------------")
        print("TEAM : "+ color.firstChild.data)
        print("-------------------")
        print(" ")


    inventorlist = item.getElementsByTagName('inventor')

    for inventor in inventorlist:
        name = inventor.getElementsByTagName('name') #On recupere son nom
        physics = inventor.getElementsByTagName('physics') #On recupere sa competence en physique
        mathematics = inventor.getElementsByTagName('mathematics') #On recupere sa competence en math
        chemistry = inventor.getElementsByTagName('chemistry') #On recupere sa competence en chimie
        mechanics = inventor.getElementsByTagName('mechanics') #On recupere sa competence en mecanique

        knowledgetargetlist = inventor.getElementsByTagName('target_knowledge') #On recupere ses target competences (liste)

        print("[Name]")
        print(name[0].firstChild.nodeValue)
        print(" ")
        print("[Knowledge]")
        print("physique : "+physics[0].firstChild.nodeValue)
        print("chemistry : " + chemistry[0].firstChild.nodeValue)
        print("mechanics : " + mechanics[0].firstChild.nodeValue)
        print("mathematics : " + mathematics[0].firstChild.nodeValue)
        print(" ")
        print("[Target Knowledge]")


        #Pour chaque competence target de sa liste de competence target
        for knowledgetarget in knowledgetargetlist:

            physicstarget = knowledgetarget.getElementsByTagName('physics')   #On recupere sa competence en physique
            mathematicstarget = knowledgetarget.getElementsByTagName('mathematics')  #On recupere sa competence en mathematique
            mechanicstarget = knowledgetarget.getElementsByTagName('mechanics')  #On recupere sa competence en mecanique
            chemistrytarget = knowledgetarget.getElementsByTagName('chemistry')  #On recupere sa competence en chimie

            print("physique : " + physicstarget[0].firstChild.nodeValue)
            print("chemistry : " + chemistrytarget[0].firstChild.nodeValue)
            print("mechanics : " + mechanicstarget[0].firstChild.nodeValue)
            print("mathematics : " + mathematicstarget[0].firstChild.nodeValue)



        print(" ")

#Pour chaque invention dans la liste des inventions
for item in inventionslist:
    print("-------------------")
    print("INVENTION")
    print("-------------------")
    print(" ")

    inventionlist = item.getElementsByTagName('invention') #On recupere une invention


    for invention in inventionlist:
        name = invention.getElementsByTagName('name') #On recupere son nom
        physics = invention.getElementsByTagName('physics') #On recupere sa competence en physique
        chemistry = invention.getElementsByTagName('chemistry') #On recupere sa competence en chimie
        mechanics = invention.getElementsByTagName('mechanics') #On recupere sa competence en mecanique
        mathematics = invention.getElementsByTagName('mathematics') #On recupere sa competence en mathematique
        classification = invention.getElementsByTagName('classification') #On recupere sa classification



        print("[Name] ")
        print(name[0].firstChild.nodeValue)
        print(" ")
        print("[Knowledge]")
        print("physics : "+physics[0].firstChild.nodeValue)
        print("chemistry : " + chemistry[0].firstChild.nodeValue)
        print("mechanics : " + mechanics[0].firstChild.nodeValue)
        print("mathematics : " + mathematics[0].firstChild.nodeValue)

        print(" ")
        print("[Classification]")
        print("classification : " + classification[0].firstChild.nodeValue)
        print(" ")

        print("~")

#Pour chaque recompense dans la liste de recompenses
for item in rewardlist:
    progresspointlist = item.getElementsByTagName('progress_reward') #On recupere la liste des progresspoint
    pointrewardlist = item.getElementsByTagName('point_reward') #On recupere la liste des pointreward
    availabilityrewardlist = item.getElementsByTagName('availability_reward') #On recupere la liste des availibilityreward
    additionalknowledgerewardlist = item.getElementsByTagName('additional_knowledge_reward') #On recupere la liste des additionalknowledgereward
    classificationrewardlist = item.getElementsByTagName('classification_reward') #On recupere la liste des classificationreward

    print("[Progress Reward]")
    # Pour chaque progresspoint de la liste de progresspoint
    for progresspoint in progresspointlist:
        reward = progresspoint.getElementsByTagName('number') #On recupere son nombre
        level = progresspoint.getElementsByTagName('level') #On recupere son niveau
        print("reward "+level[0].firstChild.nodeValue+" : "+ reward[0].firstChild.nodeValue)
    print(" ")
    print("[Points Reward]")

# Pour chaque pointreward de la liste de pointreward
    for pointreward in pointrewardlist:
        reward = pointreward.getElementsByTagName('number')#On recupere son nombre
        level = pointreward.getElementsByTagName('point')#On recupere ses points
        print("reward "+level[0].firstChild.nodeValue+" : "+ reward[0].firstChild.nodeValue)

    print(" ")
    print("[Availability Reward]")

# Pour chaque availabilityreward de la liste de availabilityreward
    for availabilityreward in availabilityrewardlist:
        print(availabilityreward.firstChild.data)#On recupere son nombre

    print(" ")
    print("[Additionalknowledge Reward]")

# Pour chaque availabilityreward de la liste de availabilityreward
    for additionalknowledgereward in additionalknowledgerewardlist:
        print(additionalknowledgereward.firstChild.data) #On recupere son nombre

    print(" ")
    print("[Classification Reward]")
# Pour chaque availabilityreward de la liste de availabilityreward
    for classificationreward in classificationrewardlist:
        print(classificationreward.firstChild.data)#On recupere son nombre