#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/ship/components/droid_interface/shared_ddi_novaldex_special_droid_interface_mk1.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/ship/components/droid_interface/shared_ddi_novaldex_special_droid_interface_mk1.iff"
		result.attribute_template_id = 8
		result.stf_name_file = "ddi_novaldex_special_droid_interface_mk1_n"
		result.stf_name_string = "space/space_item"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())