#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/creature/npc/droid/crafted/shared_dz_70_fugitive_tracker_droid_advanced.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/creature/npc/droid/crafted/shared_dz_70_fugitive_tracker_droid_advanced.iff"
		result.attribute_template_id = 3
		result.stf_name_file = "dz_70_fugitive_tracker_crafted_advanced"
		result.stf_name_string = "droid_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())