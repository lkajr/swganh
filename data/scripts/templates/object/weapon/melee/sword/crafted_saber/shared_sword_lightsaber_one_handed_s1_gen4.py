#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/weapon/melee/sword/crafted_saber/shared_sword_lightsaber_one_handed_s1_gen4.iff"
	is_prototype = False
	
	def create(self, params):
		result = Weapon()
	
		result.template = "object/weapon/melee/sword/crafted_saber/shared_sword_lightsaber_one_handed_s1_gen4.iff"
		result.attribute_template_id = 10
		result.stf_name_file = "sword_lightsaber_type1"
		result.stf_name_string = "weapon_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())