
#ifndef SWGANH_OBJECT_TANGIBLE_BASE_TANGIBLE_H_
#define SWGANH_OBJECT_TANGIBLE_BASE_TANGIBLE_H_

#include <cstdint>
#include <set>
#include <string>
#include <vector>
#include <list>

#include "swganh/object/object.h"
#include "swganh/messages/containers/network_sorted_vector.h"

namespace swganh {
namespace object {
namespace tangible {

enum StaticType {
    MOVEABLE = 0,
    STATIC
};

struct Defender
{
    Defender()
        : object_id(0)
    {}

    Defender(uint64_t object_id_)
        : object_id(object_id_)
    {}

    void Serialize(swganh::messages::BaselinesMessage& message)
    {
        message.data.write<uint64_t>(object_id);
    }

    void Serialize(swganh::messages::DeltasMessage& message)
    {
        message.data.write<uint64_t>(object_id);
    }

    bool operator==(const Defender& other)
    {
        return other.object_id == object_id;
    }

    uint64_t object_id;
};

class TangibleMessageBuilder;
    
class BaseTangible : public swganh::object::Object
{
public:
    BaseTangible();
    BaseTangible(const std::string& customization, std::vector<uint32_t> component_customization, uint32_t bitmask_options,
        uint32_t incap_timer, uint32_t damage_amount, uint32_t max_condition, bool is_static, std::vector<uint64_t> defenders);
    void AddCustomization(const std::string& customization);
    void SetCustomization(const std::string& customization);
    const std::string& GetCustomization() { return customization_; }

    const std::vector<uint32_t>& GetComponentCustomization() { return component_customization_list_; }
    void AddComponentCustomization(uint32_t customization);
    void RemoveComponentCustomization(uint32_t customization);
    void ClearComponentCustomization();
    
    // no idea what options these are...
    uint32_t GetOptionsMask() { return options_bitmask_; }
    void ToggleOption(uint32_t option);
    void SetOptionsMask(uint32_t options);

    uint32_t GetIncapTimer() { return incap_timer_; }
    void SetIncapTimer(uint32_t incap_timer);

    uint32_t GetCondition() { return condition_damage_; }
    void SetConditionDamage(uint32_t damage_amount);

    uint32_t GetMaxCondition() { return max_condition_; }
    void SetMaxCondition(uint32_t max_condition);

    bool IsStatic() { return is_static_; }
    void SetStatic(bool is_static);

    void AddDefender(uint64_t defender);
    void RemoveDefender(uint64_t defender);
    void ResetDefenders(std::vector<uint64_t> defenders);
    bool IsDefending(uint64_t defender);
    swganh::messages::containers::NetworkSortedVector<Defender> GetDefenders() { return defender_list_; }
    void ClearDefenders();

    virtual boost::optional<swganh::messages::BaselinesMessage> GetBaseline3();
    virtual boost::optional<swganh::messages::BaselinesMessage> GetBaseline6();
    virtual boost::optional<swganh::messages::BaselinesMessage> GetBaseline7();
private:
    friend TangibleMessageBuilder;

    std::vector<uint64_t>::iterator FindDefender_(uint64_t defender);

    std::string customization_;                          // update 3
    std::vector<uint32_t> component_customization_list_; // update 3
    uint32_t component_customization_counter_;           // update 3
    uint32_t options_bitmask_;                           // update 3
    uint32_t incap_timer_;                               // update 3
    uint32_t condition_damage_;                          // update 3
    uint32_t max_condition_;                             // update 3
    bool is_static_;                                     // update 3
    swganh::messages::containers::NetworkSortedVector<Defender> defender_list_; // update 6
};
    
}}}  // namespace swganh::object::tangible

#endif  // SWGANH_OBJECT_TANGIBLE_BASE_TANGIBLE_H_
