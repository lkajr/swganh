#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/space/story_loot/shared_loot_all_freighter_2.iff"
	is_prototype = False
	
	def create(self, kernel, params):
		result = Tangible()
	
		result.template = "object/tangible/space/story_loot/shared_loot_all_freighter_2.iff"
		result.attribute_template_id = -1
		result.stfName("space/story_loot_n","loot_all_freighter_2")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())