#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/item/quest/hero_of_tatooine/shared_explosives_crate.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/item/quest/hero_of_tatooine/shared_explosives_crate.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "hero_of_tatooine_explosives_crate"
		result.stf_name_string = "quest_item_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())