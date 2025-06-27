import json
import yaml


class LoadDataFiles:
    def load_yaml_file(self,
                       yaml_file_path :str,) -> dict[object:object]:
        try:
            with open(yaml_file_path,"r") as yaml_file_obj:
                yaml_file_contents = yaml.safe_load(yaml_file_obj)
        except Exception as e:
            raise f"cannot open/find file got error : {e}: {e.__traceback__}"
        return yaml_file_contents

    def load_json_file(self,
                       json_file_path :str,) -> dict[object:object]:
        try:
            with open(json_file_path,"r") as json_file_obj:
                json_file_contents = json.dumps(json_file_obj)
        except Exception as e:
            raise f"cannot open/find file got error : {e}: {e.__traceback__}"
        return json_file_contents




