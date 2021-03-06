// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE

#include "cell_message_builder.h"

#include <algorithm>

#include "cell.h"
#include "swganh_core/object/object_events.h"
#include "swganh_core/messages/scene_end_baselines.h"
#include "swganh_core/messages/deltas_message.h"
#include "swganh_core/messages/baselines_message.h"

using namespace std;
using namespace swganh::object;
using namespace swganh::messages;

void CellMessageBuilder::RegisterEventHandlers()
{
    // TODO: Register Handlers for Cells
}

void CellMessageBuilder::SendBaselines(const std::shared_ptr<Cell>& cell, const std::shared_ptr<swganh::observer::ObserverInterface>& observer)
{
	cell->AddBaselineToCache(&BuildBaseline3(cell));
    cell->AddBaselineToCache(&BuildBaseline6(cell));

    for (auto& baseline : cell->GetBaselines())
    {
        observer->Notify(&baseline);
    }
        
    SendEndBaselines(cell, observer);
}

BaselinesMessage CellMessageBuilder::BuildBaseline3(const shared_ptr<Cell>& cell)
{
    auto message = CreateBaselinesMessage(cell, Object::VIEW_3, 5);
    message.data.append(IntangibleMessageBuilder::BuildBaseline3(cell).data);
    return BaselinesMessage(std::move(message));
}

BaselinesMessage CellMessageBuilder::BuildBaseline6(const shared_ptr<Cell>& cell)
{
    auto message = CreateBaselinesMessage(cell, Object::VIEW_6, 5);
    message.data.append(IntangibleMessageBuilder::BuildBaseline6(cell).data);
    return BaselinesMessage(std::move(message));
}