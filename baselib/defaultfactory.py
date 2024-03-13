"""
*************************************************
* DefaultFactory
*************************************************
Goal:
    1. A factory that knows how to instantiate
    2. Singletons
    3. Multi instance
    4. Call executors for dynamic output/pipelines
    5. Takes threading into consideration

Logic:
1. Create a factory class called DefaultFactory
2. Maintains a cache (dictionary) of singleton objects
3. Create a method called getObject(fqcn: str) -> Any
4. This mehtod takes a fully qualified classname as a string
5. The logic of this method is as follows
6. works with 3 interface tags
    1. IInitializable
    2. IExecutor
    3. ISingleton
7. case: if the fqcn is in the cache return its corresponding singleton object
8. case: if not
    1. create a class object (not the instance) by calling a method called load_class(fqcn)
    2. You can call a static method ISingleton.isSingleton() to see if the class is a singleton or a multi instance
    3. case: multi instance
        call an instance method called processSingleOrMultiInstance(obj: Any)
        return the output from that method 
    4. case: singleton
        1. lock the cache
        2. see if it is in the cache and if so return it and unlock
        3. log a message that we are creating a singleton of that type
        4. create the instance from the class object
        5. call an instance method called processSingleton(obj: Any)
        6. register the singleton in the cache
        7. unlock the cache
        8. return the singleton
    5. processSingleOrMultiInstance(obj: Any) -> Any
        1. if the obj is an instance of IInitializable call initialize() with args if needed
        2. if it implements IExecutor call its execute() method and get an object back
        3. Return the object to the caller
9. In the end this class should have the following
    1. A dictionary dict[str: Any] of named objects as a cache
    2. A method: getObject(fqcn) -> Any
    3. processSingleOrMultiInstance(obj: Any) -> Any

"""

import threading
import importlib
from typing import Any, Dict
from baselib.factoryinterface import IFactory

from baselib.objectinterfaces import (
    IInitializable,
    IInitializableWithArgs,
    ISingleton,
    IExecutor
)

"""
*************************************************
* AbstractFactory
*************************************************
"""
class AbsFactory(IFactory):

    def getObjectWithDefault(self, identifier: str, args: Any, defaultObject: Any) -> Any:
        """
        Attempts to call getObject and returns defaultObject if an exception occurs.
        """
        try:
            return self.getObject(identifier, args)
        except Exception as e:
            print(f"Exception caught: {e}")  # Simple logging of the exception
            return defaultObject
        
    def getObjectAbsoluteWithDefault(self, identifier: str, args: Any, defaultObject: Any) -> Any:
        """
        Attempts to call getObject and returns defaultObject if an exception occurs.
        """
        try:
            return self.getObjectAbsolute(identifier, args)
        except Exception as e:
            print(f"Exception caught: {e}")  # Simple logging of the exception
            return defaultObject


# Assuming the preliminary interface definitions from the previous explanation

class DefaultFactory(AbsFactory):
    _cache: Dict[str, Any] = {}
    _lock = threading.Lock()

    """
    *************************************************
    * Initialization
    *************************************************
    1. It doesn't need initialization for dependencies
    2. Assumes the BaseApplication object is in place while this is being constructed
    """    
    def __init__(self):
        pass

    """
    *************************************************
    * abstract methods for IFactory
    *************************************************
    """
    def getObjectAbsolute(self, identifier: str, args: Any) -> Any:
        pass

    """
    *************************************************
    * Rest of the implementation
    *************************************************
    """
    @staticmethod
    def load_class(fqcn: str) -> Any:
        module_name, class_name = fqcn.rsplit('.', 1)
        module = importlib.import_module(module_name)
        return getattr(module, class_name)
    
    @staticmethod
    def processSingleOrMultiInstance(config_root_context: str, obj: Any, objargs: Any) -> Any:
        if isinstance(obj, IInitializableWithArgs):
            # Assuming no args for simplicity; adjust as necessary
            obj.initializeWithArgs(config_root_context,objargs)
        elif isinstance(obj, IInitializable):
            obj.initialize(config_root_context)

        if isinstance(obj, IExecutor):
            return obj.execute(config_root_context, objargs)
        return obj
    
    """
    fqcn: fully qualified classname
    config_root_context: where this object is anchored in the config file
    objectargs: the client passed arguments meant for the instantiated object
    """
    def _getObjectGivenClassname(self, fqcn: str, config_root_context: str, objectargs: Any) -> Any:
        if fqcn in self._cache:
            return self._cache[fqcn]
        
        class_obj = self.load_class(fqcn)
        # Assuming ISingleton provides a means to check for singleton status; adjust as necessary
        if ISingleton.isSingleton(class_obj):
            with self._lock:
                if fqcn in self._cache:
                    return self._cache[fqcn]
                print(f"Creating a singleton of type: {fqcn}")
                instance = class_obj()
                instance = self.processSingleOrMultiInstance(instance, config_root_context, objectargs)
                self._cache[fqcn] = instance
                return instance
        else:
            instance = class_obj()
            return self.processSingleOrMultiInstance(instance, config_root_context, objectargs)
