#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/deed/city_deed/shared_garden_naboo_sml_05_deed.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/deed/city_deed/shared_garden_naboo_sml_05_deed.iff"
		result.attribute_template_id = 2
		result.stf_name_file = "garden_naboo_sml_05_deed"
		result.stf_name_string = "deed"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())