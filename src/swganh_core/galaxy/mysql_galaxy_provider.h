// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE
#pragma once

#include "swganh/galaxy/providers/galaxy_provider_interface.h"
#include <memory>

namespace swganh { namespace database { class DatabaseManagerInterface; 
}}  // swganh::database

namespace swganh {
namespace galaxy {

/**
* Provides basic galaxy functionality via mysql
*/
class MysqlGalaxyProvider : public swganh::galaxy::providers::GalaxyProviderInterface {
public:
	/**
	* Creates a new instance
	*/
    explicit MysqlGalaxyProvider(swganh::database::DatabaseManagerInterface* db_manager);

	/**
	* @return the population of the galaxy
	*/
	virtual uint32_t GetPopulation();
	
private:
    swganh::database::DatabaseManagerInterface* db_manager_;
};

}}  // namespace swganh::galaxy::providers
