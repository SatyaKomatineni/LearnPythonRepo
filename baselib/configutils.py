"""
*************************************************
* File specific imports
*************************************************
"""
import tomlkit
from typing import Any
import json
from flatten_dict import flatten #type:ignore

"""
*************************************************
* other libs
*************************************************
"""
from baselib import baselog as log
from baselib import fileutils as fileutils


def _getFlattenedDictionary(tomlConfigFilename: str) -> dict[str, Any]:
    # Read and parse the toml file
    toml_str = fileutils.read_text_file(tomlConfigFilename)
    parsed_toml: tomlkit.TOMLDocument = tomlkit.parse(toml_str)
    # convert it to json
    json_str: str = json.dumps(parsed_toml,indent=4)
    dict = json.loads(json_str)
    new_dict = _process_dict_for_aliases(dict)
    flat_dict = flatten(new_dict, reducer="dot") #type:ignore
    return flat_dict #type:ignore


    #return flatten(new_dict, reducer="dot")

def _process_dict_for_aliases(input_dict: dict[str,Any]) -> dict[str,Any]:
    # Create a copy of the dictionary to modify and return
    modified_dict = input_dict.copy()
    
    for key, value in input_dict.items():
        # Check if the value is a string and starts with "a@"
        if isinstance(value, str) and value.startswith("a@"):
            # Extract the rest of the value after "a@"
            new_key = value[2:]
            # Check if the extracted value is a key in the original dictionary
            if new_key in input_dict:
                # Replace the current value with the looked up value
                modified_dict[key] = input_dict[new_key]
            else:
                # If the new_key is not found, raise an exception
                raise ValueError(f"Aliased key '{new_key}' not found.")
    
    return modified_dict
"""
*************************************************
* Get sample configuration filename
*************************************************
"""
def _getSampleConfigFile() -> str:
    root = fileutils.getDataRoot()
    return fileutils.pathjoin(root, "appconfig.toml")

def _printConfigFilename():
    r = _getSampleConfigFile()
    log.ph("Config file", r)

def test():
    _printConfigFilename()
    d = _getFlattenedDictionary(_getSampleConfigFile())
    log.ph("Flattened dict", d)

def localTest():
    log.ph1("Starting local test")
    test()
    log.ph1("End local test")

if __name__ == '__main__':
    localTest()