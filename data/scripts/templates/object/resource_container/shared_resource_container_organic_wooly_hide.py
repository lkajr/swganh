#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/resource_container/shared_resource_container_organic_wooly_hide.iff"
	is_prototype = False
	
	def create(self, params):
		result = ResourceContainer()
	
		result.template = "object/resource_container/shared_resource_container_organic_wooly_hide.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "organic_hide_small"
		result.stf_name_string = "resource_container_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())