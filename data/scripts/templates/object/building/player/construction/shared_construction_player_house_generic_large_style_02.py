#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/player/construction/shared_construction_player_house_generic_large_style_02.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/player/construction/shared_construction_player_house_generic_large_style_02.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "temporary_structure"
		result.stf_name_string = "player_structure"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())