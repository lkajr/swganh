#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/weapon/ranged/carbine/base/shared_carbine_base.iff"
	is_prototype = False
	
	def create(self, params):
		result = Weapon()
	
		result.template = "object/weapon/ranged/carbine/base/shared_carbine_base.iff"
		result.attribute_template_id = 10
		result.stf_name_file = "unknown_weapon"
		result.stf_name_string = "obj_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())