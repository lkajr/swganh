#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/creature/npc/theme_park/shared_event_transport.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/creature/npc/theme_park/shared_event_transport.iff"
		result.attribute_template_id = 9
		result.stf_name_file = "transport"
		result.stf_name_string = "theme_park_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())