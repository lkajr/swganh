#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/military/shared_military_imperial_detachment_hq.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/military/shared_military_imperial_detachment_hq.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "military_imperial_detachment"
		result.stf_name_string = "building_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())