import json
#1. Create your inner container 
person_dict = {'first': 'Christopher', 'last': 'Harrison'}

#Add a new field (labeling in MS Access)
person_dict['city'] = 'Seattle'

#let's add a list of languages to the inner container
# (created and added the list to the dictionary)
person_dict['languages'] = ['Python', 'JavaScript', 'SQL']

#it could be 
#languages = ['Python', 'JavaScript', 'SQL']
#person_dict['languages'] = languages


#Nest it (combine) inside an outer container
staff_dict = {}
staff_dict['Program Manager'] = person_dict

# "Seal the box for shipping" convert to JSON string
staff_json = json.dumps(staff_dict, indent=2)

#see fromatted output
print(staff_json)

