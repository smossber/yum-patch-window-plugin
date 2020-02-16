from yum import config
from yum.plugins import PluginYumExit,TYPE_CORE
import os

requires_api_version = '2.4'
plugin_type = (TYPE_CORE,)

def init_hook(conduit):
    conf = conduit.getConf()
    lockfile = conduit.confString('main', 'lockfile', default=None)

    if os.path.isfile(lockfile):
      raise PluginYumExit("This system is currently locked for patching. Try again in a couple of days")
