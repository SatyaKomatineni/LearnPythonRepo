"""
*************************************************
* BaseApplication: BootStrap Application
*************************************************
Goal:
1. Act as a bootstrapping application
2. This is available and used to instantiate the dynamic DefaultApplication
3. That one will load the config, log, and factory implementations dynamically
4. Once the real application so gotten, that will replace this app
5. This class has no dependencies on others
6. Resolves the interdependency between log, config, and factory
7. Consider this the ground floor

Related classes:
ApplicationHolder
AppObjects

"""
from baselib.applicationinterface import IApplication
from baselib.loginterface import TrivialLog, ICoreLog
from baselib.configinterface import IConfig
from baselib.factoryinterface import IFactory
from baselib.dictionaryconfig import BaseTOMLConfig
from baselib.defaultfactory import DefaultFactory
from typing import Any
from baselib.configinterface import IConfig
from baselib.defaultfactory import AbsFactory

class BaseApplication(IApplication):

    config: IConfig
    log: ICoreLog
    factory: IFactory

    """
    *************************************************
    * Init
    *************************************************
    """
    def __init__(self, configfilename: str):

        self.log = self._createLog()
        self.config = self._createConfig(configfilename)
        self.factory = self._createFactory(self.config)


    """
    *************************************************
    * Interface
    *************************************************
    """
    def getConfig(self) -> IConfig:
        return self.config

    def getFactory(self) -> IFactory:
        return self.factory

    def getLog(self) -> ICoreLog:
        return self.log

    """
    *************************************************
    * Creation
    *************************************************
    """
    def _createLog(self) -> ICoreLog:
        return TrivialLog()

    def _createConfig(self, configfilename: str) -> IConfig:
        return BaseTOMLConfig(configfilename)

    def _createFactory(self, config: IConfig):
        return BaseFactory(config)

class BaseFactory(AbsFactory):
    _config: IConfig

    def __init__(self, config: IConfig):
        self._config = config

    def getObjectAbsolute(self, identifier: str, args: Any) -> Any:
        """
        Abstract method to be implemented by subclasses.
        """
        fqcn = self._config.getValue(identifier)
        class_obj = DefaultFactory.load_class(fqcn)
        obj = class_obj()
        new_obj = DefaultFactory.processSingleOrMultiInstance(identifier,obj,args)
        return new_obj


