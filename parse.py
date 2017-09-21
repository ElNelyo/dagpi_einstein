#IMPORT XML DOM
from xml.dom import minidom

#TestPushDepuisPyCharm

#Fichier xml chargé
xmldoc = minidom.parse('data.xml')

#Liste des inventeur
inventorlist = xmldoc.getElementsByTagName('team')

#Liste des inventions
inventionslist = xmldoc.getElementsByTagName('inventions')

#Liste des récompenses
rewardlist = xmldoc.getElementsByTagName('rewards')



#Pour chaque inventeur dans la liste des inventions
for item in inventorlist:
    colorlist = item.getElementsByTagName('color') #On récupère sa couleur
    for color in colorlist:
        print("-------------------")
        print("TEAM : "+ color.firstChild.data)
        print("-------------------")
        print(" ")


    inventorlist = item.getElementsByTagName('inventor')

    for inventor in inventorlist:
        name = inventor.getElementsByTagName('name') #On récupère son nom
        physics = inventor.getElementsByTagName('physics') #On récupère sa compétence en physique
        mathematics = inventor.getElementsByTagName('mathematics') #On récupère sa compétence en math
        chemistry = inventor.getElementsByTagName('chemistry') #On récupère sa compétence en chimie
        mechanics = inventor.getElementsByTagName('mechanics') #On récupère sa compétence en mecanique

        knowledgetargetlist = inventor.getElementsByTagName('target_knowledge') #On récupère ses target compétences (liste)

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


        #Pour chaque compétence target de sa liste de compétence target
        for knowledgetarget in knowledgetargetlist:

            physicstarget = knowledgetarget.getElementsByTagName('physics')   #On récupère sa compétence en physique
            mathematicstarget = knowledgetarget.getElementsByTagName('mathematics')  #On récupère sa compétence en mathématique
            mechanicstarget = knowledgetarget.getElementsByTagName('mechanics')  #On récupère sa compétence en mécanique
            chemistrytarget = knowledgetarget.getElementsByTagName('chemistry')  #On récupère sa compétence en chimie

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

    inventionlist = item.getElementsByTagName('invention') #On récupère une invention


    for invention in inventionlist:
        name = invention.getElementsByTagName('name') #On récupère son nom
        physics = invention.getElementsByTagName('physics') #On récupère sa compétence en physique
        chemistry = invention.getElementsByTagName('chemistry') #On récupère sa compétence en chimie
        mechanics = invention.getElementsByTagName('mechanics') #On récupère sa compétence en mecanique
        mathematics = invention.getElementsByTagName('mathematics') #On récupère sa compétence en mathématique
        classification = invention.getElementsByTagName('classification') #On récupère sa classification



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

#Pour chaque récompense dans la liste de récompenses
for item in rewardlist:
    progresspointlist = item.getElementsByTagName('progress_reward') #On récupère la liste des progresspoint
    pointrewardlist = item.getElementsByTagName('point_reward') #On récupère la liste des pointreward
    availabilityrewardlist = item.getElementsByTagName('availability_reward') #On récupère la liste des availibilityreward
    additionalknowledgerewardlist = item.getElementsByTagName('additional_knowledge_reward') #On récupère la liste des additionalknowledgereward
    classificationrewardlist = item.getElementsByTagName('classification_reward') #On récupère la liste des classificationreward

    print("[Progress Reward]")
    # Pour chaque progresspoint de la liste de progresspoint
    for progresspoint in progresspointlist:
        reward = progresspoint.getElementsByTagName('number') #On récupère son nombre
        level = progresspoint.getElementsByTagName('level') #On récupère son niveau
        print("reward "+level[0].firstChild.nodeValue+" : "+ reward[0].firstChild.nodeValue)
    print(" ")
    print("[Points Reward]")

# Pour chaque pointreward de la liste de pointreward
    for pointreward in pointrewardlist:
        reward = pointreward.getElementsByTagName('number')#On récupère son nombre
        level = pointreward.getElementsByTagName('point')#On récupère ses points
        print("reward "+level[0].firstChild.nodeValue+" : "+ reward[0].firstChild.nodeValue)

    print(" ")
    print("[Availability Reward]")

# Pour chaque availabilityreward de la liste de availabilityreward
    for availabilityreward in availabilityrewardlist:
        print(availabilityreward.firstChild.data)#On récupère son nombre

    print(" ")
    print("[Additionalknowledge Reward]")

# Pour chaque availabilityreward de la liste de availabilityreward
    for additionalknowledgereward in additionalknowledgerewardlist:
        print(additionalknowledgereward.firstChild.data) #On récupère son nombre

    print(" ")
    print("[Classification Reward]")
# Pour chaque availabilityreward de la liste de availabilityreward
    for classificationreward in classificationrewardlist:
        print(classificationreward.firstChild.data)#On récupère son nombre