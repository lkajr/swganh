#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/ship/components/weapon_capacitor/shared_cap_reward_sorosuub_elite.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/ship/components/weapon_capacitor/shared_cap_reward_sorosuub_elite.iff"
		result.attribute_template_id = 8
		result.stf_name_file = "cap_reward_sorosuub_elite"
		result.stf_name_string = "space/space_item"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())