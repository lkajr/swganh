#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/mission/quest_item/shared_jaleela_bindoo_q4_needed.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/mission/quest_item/shared_jaleela_bindoo_q4_needed.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "jaleela_bindoo_q4_needed"
		result.stf_name_string = "loot_rori_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())