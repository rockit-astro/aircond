#!/usr/bin/env python3
#
# This file is part of aircond.
#
# aircond is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# aircond is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with aircond.  If not, see <http://www.gnu.org/licenses/>.

import json
from warwick.observatory.common import daemons
with daemons.halfmetre_aircon.connect() as aircon:
    print(json.dumps(aircon.last_measurement(), indent=4))
