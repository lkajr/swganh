#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/intangible/ship/shared_tiebomber_pcd.iff"
	is_prototype = False
	
	def create(self, params):
		result = Intangible()
	
		result.template = "object/intangible/ship/shared_tiebomber_pcd.iff"
		result.attribute_template_id = 8
		result.stf_name_file = "tiebomber_pcd"
		result.stf_name_string = "space_item_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())