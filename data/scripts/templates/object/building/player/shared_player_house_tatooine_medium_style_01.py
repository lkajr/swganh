#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/player/shared_player_house_tatooine_medium_style_01.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/player/shared_player_house_tatooine_medium_style_01.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "housing_tatt_style01_med"
		result.stf_name_string = "building_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())