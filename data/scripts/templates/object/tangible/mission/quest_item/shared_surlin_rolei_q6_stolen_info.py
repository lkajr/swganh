#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/mission/quest_item/shared_surlin_rolei_q6_stolen_info.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/mission/quest_item/shared_surlin_rolei_q6_stolen_info.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "surlin_rolei_q2_camera"
		result.stf_name_string = "quest_naboo_plc_quest_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())