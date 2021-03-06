// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE
#pragma once

#include "swganh_core/object/tangible/tangible_factory.h"
#include <unordered_map>

namespace swganh {
namespace database {
class DatabaseManagerInterface;
}} // swganh::database

namespace sql {
    class Statement;
}  // namespace sql

namespace swganh {
namespace object {


    class Creature;
    class CreatureFactory : public swganh::object::TangibleFactory
    {
    public:
		typedef Creature ObjectType;

        CreatureFactory(swganh::app::SwganhKernel* kernel);

        virtual uint32_t PersistObject(const std::shared_ptr<swganh::object::Object>& object, bool persist_inherited = false);

        void DeleteObjectFromStorage(const std::shared_ptr<swganh::object::Object>& object);
		virtual void PersistChangedObjects();
		virtual void RegisterEventHandlers();
        std::shared_ptr<swganh::object::Object> CreateObjectFromStorage(uint64_t object_id);

        std::shared_ptr<swganh::object::Object> CreateObject();
        
    private:
		void LoadBuffs_(const std::shared_ptr<swganh::object::Creature>& creature,
			const std::shared_ptr<sql::Statement>& statement);

        void LoadSkills_(const std::shared_ptr<Creature>& creature, 
            const std::shared_ptr<sql::Statement>& statement);

        void LoadSkillMods_(const std::shared_ptr<Creature>& creature, 
            const std::shared_ptr<sql::Statement>& statement);

        void LoadSkillCommands_(const std::shared_ptr<Creature>& creature, 
            const std::shared_ptr<sql::Statement>& statement);
    };

}}  // namespace swganh::object
