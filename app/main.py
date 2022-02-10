# http://server/zm/api/host/getVersion.json
# TEST: http://server/zm/api/monitors.json

# Get -> Modify -> Save -> Configure -> Save Status -> Report

class DatabaseSingleton:
    """" 
    Connect to mongo server pool & wait for i/o.
    CRUD methods imported from custom dbs class.
    """
    pass


class Target:
    # TODO: `tiangelo/typer` for base cli entries
    def load_base_configs(self):
        """ 
        Use cli arguments to find config file?
        `zmconf --file clasico-configs.csv`
        """
        pass
    
    def modify(self):
        """ 
        `import csv`
        Load from excel doc with csv() and create dict
        """
        pass

    def map_cameras(self):
        """
        Map camera names to ip address.
        If assignment fails that gets a revision number.
        """
        pass

    def save(self):
        """
        Write configs and metadata to other collection or dbs
        Give incremental version num and tag host with UUID module
        """
        pass


class Cookies:

    def generate(self):
        """ Generate new cookie with for api auth """
        pass

    def cache(self):
        """ Cache for subsequent requests to same host """
        pass

    def delete(self):
        """ Delete cookie when session closes """
        pass


class Executor:
    
    def iterate_options(self):
        """ 
        Talk to REST API with requests module
        f-string's in four loop to iterate over endpoitns POST-ing
        # f"http://server/zm/api/{path}/{to}{endpoint}"
        """
        pass
