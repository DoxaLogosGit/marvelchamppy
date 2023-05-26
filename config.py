# Module that handles reading in the yaml config data
import strictyaml
from path import Path
hero_config_data = strictyaml.load(Path("heroes.yaml").text()).data
villain_config_data = strictyaml.load(Path("villains.yaml").text()).data
Traits = strictyaml.load(Path("traits.yaml").text()).data
expansions = strictyaml.load(Path("expansions.yaml").text()).data