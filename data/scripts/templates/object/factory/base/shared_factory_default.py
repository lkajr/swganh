#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/factory/base/shared_factory_default.iff"
	is_prototype = False
	
	def create(self, params):
		result = FactoryCrate()
	
		result.template = "object/factory/base/shared_factory_default.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "generic_items_crate"
		result.stf_name_string = "factory_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())