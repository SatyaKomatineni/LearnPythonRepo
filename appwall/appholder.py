"""
*************************************************
* ApplicationHolder class
*************************************************
Goal:
1. Holds the application singleton object
2. Initializes the application through a config file
3. This must be done before this application is used
4. Starts with a bootstrap app and then loads the real app from config file

"""
from baselib.applicationinterface import IApplication
from baselib import baselog as log
from baselib.baseapplication import BaseApplication
from baselib.appconfignames import ApplicationObjectNames

class ApplicationHolder():
    appconfig_filename: str = ""
    application: IApplication | None = None

    @staticmethod
    def getApplication() -> IApplication:
        return ApplicationHolder.application #type:ignore
    
    @staticmethod
    def initializeApplication(config_filename: str):
        log.validate_not_null_or_empty(config_filename)
        ApplicationHolder.appconfig_filename = config_filename
        ApplicationHolder.application = BaseApplication(config_filename)

    @staticmethod
    def _createRealApplication():
        fact = ApplicationHolder.application.getFactory() #type:ignore
        try:
            fact.getObjectAbsolute(ApplicationObjectNames.APPLICATION_OBJ_NAME, ApplicationHolder.appconfig_filename)
        except Exception as e:
            return 
