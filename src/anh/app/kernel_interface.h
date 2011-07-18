
#ifndef ANH_APP_KERNEL_INTERFACE_H_
#define ANH_APP_KERNEL_INTERFACE_H_

#include <cstdint>
#include <memory>
#include <string>

namespace anh {
namespace database {
class DatabaseManagerInterface;
}}  // namespace anh::database

namespace anh {
namespace event_dispatcher {
class EventDispatcherInterface; 
}}  // namespace anh::event_dispatcher

namespace anh {
namespace plugin {
class PluginManager;
}}  // namespace anh::plugin

namespace anh {
namespace service {
class ServiceManager;
}}  // namespace anh::service

namespace anh {
namespace app {

struct Version {
    int32_t major;
    int32_t minor;

    std::string ToString() {
        return major + "." + minor;
    }
};

class KernelInterface {
public:
    virtual ~KernelInterface() {}

    virtual const Version& GetVersion() = 0;

    virtual std::shared_ptr<anh::event_dispatcher::EventDispatcherInterface> GetEventDispatcher() = 0;

    virtual std::shared_ptr<anh::plugin::PluginManager> GetPluginManager() = 0;

    virtual std::shared_ptr<anh::service::ServiceManager> GetServiceManager() = 0;

    virtual std::shared_ptr<anh::database::DatabaseManagerInterface> GetDatabaseManager() = 0;

    // also add entity manager, blah blah.
};

}}  // namespace anh::app

#endif  // ANH_APP_KERNEL_INTERFACE_H_