#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/weapon/trap/shared_eqp_weapon_auto_laser_trap.iff"
	is_prototype = False
	
	def create(self, kernel, params):
		result = Weapon()
	
		result.template = "object/weapon/trap/shared_eqp_weapon_auto_laser_trap.iff"
		result.attribute_template_id = 10
		result.stfName("wpn_d","laser trap")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())