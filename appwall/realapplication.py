"""
*************************************************
* ConfigApplication: Driven by configuration
*************************************************
Goal:
1. Config Application
2. One that is constructed from the configuration file
3. Gets Log, Config, and Factory from app config file

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
from typing import Any, cast
from baselib.configinterface import IConfig
from baselib.defaultfactory import AbsFactory
from appwall.appholder import ApplicationHolder

from baselib.objectinterfaces import (ISingleton, IInitializableWithArgs)

class ConfigApplication(IApplication,ISingleton, IInitializableWithArgs):

    config: IConfig
    log: ICoreLog
    factory: IFactory
    configRootContext: str

    """
    From IInitializableWithArgs
    """
    def initializeWithArgs(self, rootContext: str, args: Any) -> None:
        self.configRootContext = rootContext
        self._init(cast(str,args))

    """
    *************************************************
    * Init (local): called by initialzablewith args
    *************************************************
    """
    def _init(self, configfilename: str):

        self.log = self._createLog()
        self.config = self._createConfig(configfilename)
        self.factory = self._createFactory(self.config)

    def _getBootstrapFactory() -> IFactory:
        fact = ApplicationHolder.application.getFactory() #type:ignore
        return fact

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
        fact = self._getBootstrapFactory()
        app.

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


