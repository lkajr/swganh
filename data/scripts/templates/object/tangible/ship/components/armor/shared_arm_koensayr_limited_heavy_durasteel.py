#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/ship/components/armor/shared_arm_koensayr_limited_heavy_durasteel.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/ship/components/armor/shared_arm_koensayr_limited_heavy_durasteel.iff"
		result.attribute_template_id = 8
		result.stf_name_file = "arm_koensayr_limited_heavy_durasteel_n"
		result.stf_name_string = "space/space_item"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())