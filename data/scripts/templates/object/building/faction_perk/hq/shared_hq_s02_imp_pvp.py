#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/faction_perk/hq/shared_hq_s02_imp_pvp.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/faction_perk/hq/shared_hq_s02_imp_pvp.iff"
		result.attribute_template_id = -1
		result.stf_name_file = "hq_s02_imp_pvp"
		result.stf_name_string = "faction_perk_n"
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())