#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/wearables/armor/ithorian_defender/shared_ith_armor_s01_bracer_r.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/wearables/armor/ithorian_defender/shared_ith_armor_s01_bracer_r.iff"
		result.attribute_template_id = 0
		result.stf_name_file = "ith_armor_s01_bracer_r"
		result.stf_name_string = "wearables_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())