#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/static/structure/general/shared_poi_nboo_corral_32x32_s03.iff"
	is_prototype = False
	
	def create(self, params):
		result = Static()
	
		result.template = "object/static/structure/general/shared_poi_nboo_corral_32x32_s03.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "unknown_object"
		result.stf_name_string = "obj_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())