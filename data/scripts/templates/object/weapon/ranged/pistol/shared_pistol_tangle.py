#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/weapon/ranged/pistol/shared_pistol_tangle.iff"
	is_prototype = False
	
	def create(self, params):
		result = Weapon()
	
		result.template = "object/weapon/ranged/pistol/shared_pistol_tangle.iff"
		result.attribute_template_id = 10
		result.stf_name_file = "pistol_tangle"
		result.stf_name_string = "weapon_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())