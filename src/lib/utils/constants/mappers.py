import pandas as pd
from src.lib.utils.data_loaders import load_data

event_codes = load_data(
    "src/lib/utils/constants/event_codes.tsv", kwargs={"dtype": {"CAMEOEVENTCODE": str}}
)
event_code_map = event_codes.set_index("CAMEOEVENTCODE")["EVENTDESCRIPTION"].to_dict()


geo_type_codes = load_data(
    "src/lib/utils/constants/geo_type_codes.tsv", kwargs={"dtype": {"GEOTYPECODE": str}}
)
geo_type_code_map = geo_type_codes.set_index("GEOTYPECODE")["DESCRIPTION"].to_dict()

# Source: http://data.gdeltproject.org/documentation/GDELT-Event_Codebook-V2.0.pdf, https://github.com/carrillo/Gdelt/blob/master/resources/staticTables/CAMEO.country.txt
# Note: Manually-added TWN and SSD
country_codes = load_data(
    "src/lib/utils/constants/cameo_country_codes.tsv", kwargs={"dtype": {"CODE": str, "LABEL": str}}
)
country_code_map = country_codes.set_index("CODE")["LABEL"].to_dict()

# Source: http://data.gdeltproject.org/documentation/CAMEO.Manual.1.1b3.pdf
role_codes = load_data(
    "src/lib/utils/constants/role_codes.tsv", kwargs={"dtype": {"ROLECODE": str}}
)
role_code_map = role_codes.set_index("ROLECODE")["ROLE"].to_dict()

gov_arm_code_map = (
    role_codes[role_codes["ROLECODE"] != "GOV"].set_index("ROLECODE")["ROLE"].to_dict()
)
gov_arm_code_map = {
    f"GOV{k}": f"GOVERNMENT {gov_arm_code_map[k]}" for k in gov_arm_code_map.keys()
}
