#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/loot/bestine/shared_bestine_painting_schematic_moncal_eye_01.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/loot/bestine/shared_bestine_painting_schematic_moncal_eye_01.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "painting_schematic_moncal_eye_01"
		result.stf_name_string = "craft_furniture_ingredients_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())