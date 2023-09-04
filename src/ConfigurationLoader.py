import os
from dotenv import load_dotenv
from dotenv import dotenv_values
from configparser import ConfigParser

class ConfigurationLoader:
    
    def __init__(self):
        # Load the stored environment variables
        load_dotenv() 
    
    @staticmethod
    def get_value_environment(key):
        env_configurations = dotenv_values(".env") 
        return env_configurations.get(key)
    
    @staticmethod
    def get_all_environment():
        env_configurations = dotenv_values(".env")        
        return print(env_configurations)
    
    @staticmethod
    def get_value(section, key):
        configurations = ConfigParser()
        configurations.read("app.conf")
        if configurations.has_section(section=section):
            if configurations.has_option(section=section, option=key):
                return configurations.get(section, key)
            else: 
                return None
        else: 
            return None
        
    @staticmethod
    def get_all():
        configurations = ConfigParser()
        configurations.read("app.config")
        configurations_dict = {s:dict(configurations.items(s)) for s in configurations.sections()}
        return configurations_dict
