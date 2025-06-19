import os
import sys

from queries.orm import create_tables, insert_data, insert_data_source, insert_data_vk, update_data_vk
#sys.path.insert(1, os.path.join(sys.path[0], '..'))

filtered_content = {
    "link": "https://vk.com/sergeyiss?w=wall-101948711_41719",
    "platform_source_enum": "vk",
    "source": "https://vk.com/sergeyiss",
}

source = ["https://vk.com/sergeyiss"]

##insert_data_source(source)
#insert_data_vk(filtered_content)
update_data_vk()