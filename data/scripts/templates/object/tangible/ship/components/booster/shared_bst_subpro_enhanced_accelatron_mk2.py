#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/ship/components/booster/shared_bst_subpro_enhanced_accelatron_mk2.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/ship/components/booster/shared_bst_subpro_enhanced_accelatron_mk2.iff"
		result.attribute_template_id = 8
		result.stf_name_file = "bst_subpro_enhanced_accelatron_mk2_n"
		result.stf_name_string = "space/space_item"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())