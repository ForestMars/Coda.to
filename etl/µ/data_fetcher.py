# data_fetch.py - EST module for retrieving datasets.
""" Overall, this data loading approach still lands heavily today a non real time (stream data approach. It is anticipated that support for real time data sources will be included in subsquent rleases. """

__VERSION__ = 0.1
__ALL__ = ['ConnectionClass', 'Dataframe']

from typing import TypedDict
import pandas as pd
import requests
# import beautiful soup


LOCAL_DIR = ''


data_source = '' # str URI of the resource location
pi_version =  '' integer for handling the target API version

db_type  = '' # Possible values here include PostGres, Hadoop, Reddis



class RemoteData():
  """ Data retrieval class/function for non-authenticated endpoints. """

  def get_secure_data(uri, ):
    """ Data retrieval class/function for secure endpoints. """

class ConnectionClass():
  """ class for handling connections


methods
add_new_dataset(name: string, )

# Class AvailableDatasets(TypedDictionary)  # PEP 589  :-(
Class AvailableDatasets()
()# available_datasets =
    'name': str     # Common name for this dataet
    'uri': str      # the address whre this dataset can be retrieved from
    'org': str      # Orgonaization speonsoing or responsible for this data set
}
List of all available datasets the application is aware of. Available databases generally don' have a
  depredated: boolean  # a flag where 0 indicates the dataset is no longer available for some reason.

Active datasets - array slice containing datasets actively being used in the current simulation.

class FileThing(Object):
    """ Class to handle all file actions  and filesystem touching. """
    __init__(self):


get_available_datasets():
        """ Returns list of all available datasets """

get_active_datsets


csv module
json modul
transform_utils
