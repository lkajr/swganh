#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/creature/npc/droid/shared_r2_base.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/creature/npc/droid/shared_r2_base.iff"
		result.attribute_template_id = 3
		result.stf_name_file = "r2_base"
		result.stf_name_string = "droid_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())