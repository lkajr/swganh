#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/resource_container/shared_simple.iff"
	is_prototype = False
	
	def create(self, params):
		result = ResourceContainer()
	
		result.template = "object/resource_container/shared_simple.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "unknown_container"
		result.stf_name_string = "obj_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())