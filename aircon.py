import json
from warwick.observatory.common import daemons
with daemons.superwasp_aircon.connect() as aircon:
    print(json.dumps(aircon.last_measurement(), indent=4))
