#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/endor/shared_endor_catwalk_cap.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/endor/shared_endor_catwalk_cap.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "base_filler_building"
		result.stf_name_string = "building_name"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())