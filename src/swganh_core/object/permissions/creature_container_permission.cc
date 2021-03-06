// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE

#include "creature_container_permission.h"

#include "swganh_core/object/object.h"
#include "swganh/object/container_interface.h"

using namespace swganh::object;

bool CreatureContainerPermission::canInsert(std::shared_ptr<ContainerInterface> container, std::shared_ptr<Object> requester, std::shared_ptr<Object> object)
{
	return (container->GetContainer() == requester);
}

bool CreatureContainerPermission::canRemove(std::shared_ptr<ContainerInterface> container, std::shared_ptr<Object> requester, std::shared_ptr<Object> object)
{
	return (container->GetContainer() == requester);
}

bool CreatureContainerPermission::canView(std::shared_ptr<ContainerInterface> container, std::shared_ptr<Object> requester)
{
	return (container->GetContainer() == requester);
}