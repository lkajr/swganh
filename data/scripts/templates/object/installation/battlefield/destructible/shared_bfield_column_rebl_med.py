#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/installation/battlefield/destructible/shared_bfield_column_rebl_med.iff"
	is_prototype = False
	
	def create(self, params):
		result = Installation()
	
		result.template = "object/installation/battlefield/destructible/shared_bfield_column_rebl_med.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "column"
		result.stf_name_string = "battlefield"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())