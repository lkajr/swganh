#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/cell/shared_cell.iff"
	is_prototype = False
	
	def create(self, params):
		result = Cell()
	
		result.template = "object/cell/shared_cell.iff"
		result.attribute_template_id = -1
		result.stf_name_file = ""
		result.stf_name_string = ""
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())