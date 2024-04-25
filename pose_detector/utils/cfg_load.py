import yaml
import loguru as lgr

with open("settings.yaml", "r") as file_object:
    cfg = yaml.load(file_object, Loader=yaml.SafeLoader)


if __name__ == "__main__":
    # Change to logging
    print(cfg)
    
    
    