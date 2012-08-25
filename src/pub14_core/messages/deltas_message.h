// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE
#pragma once

#include <cstdint>
#include "anh/byte_buffer.h"
#include "base_deltas_message.h"

namespace swganh {
namespace messages {
    
    class DeltasMessage : public BaseDeltasMessage<DeltasMessage>
    {
    public:
        static uint16_t Opcount() { return 5; }
        static uint32_t Opcode() { return 0x12862153; }
    };
    
}}  // namespace swganh::messages
