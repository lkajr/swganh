/*
 This file is part of SWGANH. For more information, visit http://swganh.com
 
 Copyright (c) 2006 - 2011 The SWG:ANH Team

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 as published by the Free Software Foundation; either version 2
 of the License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
*/

#ifndef CHARACTER_CHARACTER_SERVICE_H_
#define CHARACTER_CHARACTER_SERVICE_H_

#include "anh/event_dispatcher/event_dispatcher_interface.h"

#include "swganh/base/base_service.h"
#include "swganh/character/base_character_service.h"

namespace character {
    
class CharacterService : public swganh::character::BaseCharacterService {
public:
    CharacterService(std::shared_ptr<anh::event_dispatcher::EventDispatcherInterface> event_dispatcher);
    ~CharacterService();
    
    /*
    *  @brief used to subscribe to events on a serivce
    */
    virtual void subscribe();

    /*
    *  @brief used to perform any startup specific tasks for the service
    */
    virtual void onStart();

    /*
    *  @brief used to perform any shutdown specific tasks for the service
    */
    virtual void onStop();

    /*
    *  @brief used to perform any update specific tasks for the service
    */
    virtual void Update();

    // CharacterService API Methods

    std::vector<swganh::character::CharacterData> GetCharactersForAccount(uint64_t account_id);
};

}  // namespace character

#endif  // CHARACTER_CHARACTER_SERVICE_INTERFACE_H_
