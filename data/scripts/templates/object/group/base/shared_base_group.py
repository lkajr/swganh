#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/group/base/shared_base_group.iff"
	is_prototype = False
	
	def create(self, params):
		result = Group()
	
		result.template = "object/group/base/shared_base_group.iff"
		result.attribute_template_id = -1
		result.stf_name_file = ""
		result.stf_name_string = "string_id_table"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())