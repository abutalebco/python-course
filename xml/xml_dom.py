import xml.dom.minidom

domtree = xml.dom.minidom.parse('xml/data.xml')

group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print("======PERSON======")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))

    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Major: {}".format(person.getElementsByTagName('major')[0].childNodes[0].data))

newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Daleda Osman'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('22'))

major = domtree.createElement('major')
major.appendChild(domtree.createTextNode('Project Management'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(major)

group.appendChild(newperson)

pretty_xml = domtree.toprettyxml(indent=" ")

pretty_xml = "\n".join([line for line in pretty_xml.splitlines() if line.strip()])

with open('xml/data.xml', 'w') as f:
    f.write(pretty_xml)

# domtree.writexml(open('xml/data.xml', 'w'))