// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE

#include "resource_container.h"

using namespace std;
using namespace swganh::object;
using namespace swganh::object;
using namespace swganh::messages;

ResourceContainer::ResourceContainer() : Tangible()
    , current_quantity_(0)
    , global_resource_id_(0)
    , max_quantity_(0)
    , resource_type_("")
    , variation_name_(L"")
{
}
ResourceContainer::ResourceContainer(const std::string& customization, std::vector<uint32_t> component_customization, uint32_t bitmask_options,
        uint32_t incap_timer, uint32_t condition_damage, uint32_t max_condition, bool is_static, std::vector<uint64_t> defenders,
        uint32_t current_quantity, uint64_t global_resource_id, uint32_t max_quantity, std::string resource_type, std::wstring name)
    : Tangible(customization, component_customization, bitmask_options, incap_timer, condition_damage, max_condition, is_static, defenders)
    , current_quantity_(current_quantity)
    , global_resource_id_(global_resource_id)
    , max_quantity_(max_quantity)
    , resource_type_(resource_type)
    , variation_name_(name)
{
}

uint32_t ResourceContainer::GetCurrentQuantity()
{
	boost::lock_guard<boost::mutex> lock(object_mutex_);
	return current_quantity_;
}

uint64_t ResourceContainer::GetGlobalResource()
{
	boost::lock_guard<boost::mutex> lock(object_mutex_);
	return global_resource_id_;
}

uint32_t ResourceContainer::GetMaxQuantity()
{
	boost::lock_guard<boost::mutex> lock(object_mutex_);
	return max_quantity_;
}

std::string ResourceContainer::GetResourceType()
{
	boost::lock_guard<boost::mutex> lock(object_mutex_);
	return resource_type_;
}

std::wstring ResourceContainer::GetResourceName()
{
	boost::lock_guard<boost::mutex> lock(object_mutex_);
	return variation_name_;
}

void ResourceContainer::SetCurrentQuantity(uint32_t current_quantity)
{
	{
		boost::lock_guard<boost::mutex> lock(object_mutex_);
		current_quantity_ = current_quantity;
	}
	DISPATCH(ResourceContainer, CurrentQuantity);
}

void ResourceContainer::SetGlobalResource(uint64_t global_resource)
{
	{
		boost::lock_guard<boost::mutex> lock(object_mutex_);
		global_resource_id_ = global_resource;
	}
	DISPATCH(ResourceContainer, GlobalResourceId);
}

void ResourceContainer::SetMaxQuantity(uint32_t max_quantity)
{
	{
		boost::lock_guard<boost::mutex> lock(object_mutex_);
		max_quantity_ = max_quantity;
	}
	DISPATCH(ResourceContainer, MaxQuantity);
}
void ResourceContainer::SetResourceType(const string& resource_type)
{
	{
		boost::lock_guard<boost::mutex> lock(object_mutex_);
		resource_type_ = resource_type;
	}
	DISPATCH(ResourceContainer, ResourceType);
}
void ResourceContainer::SetResourceName(const wstring& name)
{
	{
		boost::lock_guard<boost::mutex> lock(object_mutex_);
		variation_name_ = name;
	}
	DISPATCH(ResourceContainer, ResourceName);
}


std::shared_ptr<Object> ResourceContainer::Clone()
{
	boost::lock_guard<boost::mutex> lock(object_mutex_);
	auto other = make_shared<ResourceContainer>();
	Clone(other);
	return other;
}

void ResourceContainer::Clone(std::shared_ptr<ResourceContainer> other)
{
	other->current_quantity_ = current_quantity_;
	other->global_resource_id_ = global_resource_id_;
	other->max_quantity_ = max_quantity_;
	other->resource_type_ = resource_type_;
	other->variation_name_ = variation_name_;

	Tangible::Clone(other);
}