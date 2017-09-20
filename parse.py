from xml.dom import minidom
xmldoc = minidom.parse('data.xml')
inventorlist = xmldoc.getElementsByTagName('team')
inventionslist = xmldoc.getElementsByTagName('inventions')
rewardlist = xmldoc.getElementsByTagName('rewards')
#print(itemlist[0].attributes['color'].value)


for item in inventorlist:
    colorlist = item.getElementsByTagName('color')
    for color in colorlist:
        print("-------------------")
        print("TEAM : "+ color.firstChild.data)
        print("-------------------")
        print(" ")


    inventorlist = item.getElementsByTagName('inventor')
    for inventor in inventorlist:
        name = inventor.getElementsByTagName('name')
        physics = inventor.getElementsByTagName('physics')
        mathematics = inventor.getElementsByTagName('mathematics')
        chemistry = inventor.getElementsByTagName('chemistry')
        mechanics = inventor.getElementsByTagName('mechanics')
        knowledgetargetlist = inventor.getElementsByTagName('target_knowledge')

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

        for knowledgetarget in knowledgetargetlist:

            physicstarget = knowledgetarget.getElementsByTagName('physics')
            mathematicstarget = knowledgetarget.getElementsByTagName('mathematics')
            mechanicstarget = knowledgetarget.getElementsByTagName('mechanics')
            chemistrytarget = knowledgetarget.getElementsByTagName('chemistry')

            print("physique : " + physicstarget[0].firstChild.nodeValue)
            print("chemistry : " + chemistrytarget[0].firstChild.nodeValue)
            print("mechanics : " + mechanicstarget[0].firstChild.nodeValue)
            print("mathematics : " + mathematicstarget[0].firstChild.nodeValue)



        print(" ")

for item in inventionslist:
    print("-------------------")
    print("INVENTION")
    print("-------------------")
    print(" ")

    inventionlist = item.getElementsByTagName('invention')

    for invention in inventionlist:
        name = invention.getElementsByTagName('name')
        physics = invention.getElementsByTagName('physics')
        chemistry = invention.getElementsByTagName('chemistry')
        mechanics = invention.getElementsByTagName('mechanics')
        mathematics = invention.getElementsByTagName('mathematics')
        classification = invention.getElementsByTagName('classification')



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

for item in rewardlist:
    progresspointlist = item.getElementsByTagName('progress_reward')
    pointrewardlist = item.getElementsByTagName('point_reward')
    availabilityrewardlist = item.getElementsByTagName('availability_reward')
    additionalknowledgerewardlist = item.getElementsByTagName('additional_knowledge_reward')
    classificationrewardlist = item.getElementsByTagName('classification_reward')

    print("[Progress Reward]")
    for progresspoint in progresspointlist:
        reward = progresspoint.getElementsByTagName('number')
        level = progresspoint.getElementsByTagName('level')
        print("reward "+level[0].firstChild.nodeValue+" : "+ reward[0].firstChild.nodeValue)
    print(" ")
    print("[Points Reward]")

    for pointreward in pointrewardlist:
        reward = pointreward.getElementsByTagName('number')
        level = pointreward.getElementsByTagName('point')
        print("reward "+level[0].firstChild.nodeValue+" : "+ reward[0].firstChild.nodeValue)

    print(" ")
    print("[Availability Reward]")

    for availabilityreward in availabilityrewardlist:
        print(availabilityreward.firstChild.data)

    print(" ")
    print("[Additionalknowledge Reward]")

    for additionalknowledgereward in additionalknowledgerewardlist:
        print(additionalknowledgereward.firstChild.data)

    print(" ")
    print("[Classification Reward]")

    for classificationreward in classificationrewardlist:
        print(classificationreward.firstChild.data)