'''
What is a class and what is an object ?

Car / Bike /Scooty  are objects 
where as vehicle is the class 
the difference of all the objects lies in the attributes.
in this case all of them fall under vehicle as they have same function 
but have variation in attribute

Man / Dog /Cat  -> objects
Living beings -> class 

'''
# class vehicle:
#     def functionality_of_vehicle(self,vehicle_name):
#         print(vehicle_name)
#         if vehicle_name=='car':
#             print('Number of wheels: 4')
#             print('Steering wheel: 1')
#         elif vehicle_name=='bike':
#             print('Number of wheels: 2')
#             print('Steering wheel: 0')
#         else: 
#             print('Not a valid vehicle')
# car=vehicle()
# car.functionality_of_vehicle('car')

# bike=vehicle()
# bike.functionality_of_vehicle('bike')

'''
Task 1: So create a class named living things
living things vitra "functionality_of_living_things" vanney huna paryo 
create objects named human, dog , cat, crow

based on the attribute (species name)
display following information
"walks on {X} foot" human X=2, dog=4, cat =4 and crow=2
"Can Fly ? {X}" human,dog,cat X=Flase crow X=True
"Has Mathematical Brain ? {X}" human X=True, dog,cat,crow X=False
'''
# class living_things: 
#     def __init__(self,argument_name):
#         self.argument_name=argument_name
#         print(f'Species Name: {self.argument_name}')

#     def functionality_of_species(self):
#         if self.argument_name.lower()=='human':
#             mathematical_brain=True
#             fly=False
#             foot=2

#         elif self.argument_name.lower()=='dog':
#             mathematical_brain=False
#             fly=False
#             foot=4
            
                
#         print(f'{self.argument_name} Species has {foot} foot \nCan Fly ? {fly},\nHas Mathematical brain {mathematical_brain} ')
#         print('--'*25)


# human=living_things('human')
# human.functionality_of_species()

# dog=living_things('dog')
# dog.functionality_of_species()


'''
Replicating Account Based users app using oop
'''

class Account:
    def __init__(self,attribute_1_user_name,attribute_2_relation_ship_status,attribute_3_study_status):
        self.user_name=attribute_1_user_name
        self.relationship_status=attribute_2_relation_ship_status
        self.study_status=attribute_3_study_status
        print(f'Username: {self.user_name}\nRelationship_status: {self.relationship_status}\nStudy Status: {self.study_status}')
        print('--'*25)

siddhant_object=Account('Siddhant Sharma','IDK','Bachelors')
Prashant_Object=Account('Prashant Something','IDK','Masters')