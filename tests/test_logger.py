import pyzzy as pz
import commons


CWD = pz.set_working_directory(__file__)

conf = CWD + "/configurations/logging.yaml"

conf = pz.load_yaml(conf)
pz.logs.load_config(conf)

user_logger = pz.logs.getLogger("development")
user_logger = pz.logs.getLogger(__name__)
root_logger = pz.logs.getLogger()


def test_logger():

    print(" main - development logger ".center(55, "-"))
    commons.use_logger(user_logger)
    commons.logger_infos(user_logger)

    print(" main - __main__ logger ".center(55, "-"))
    commons.use_logger(root_logger)
    commons.logger_infos(root_logger)

    print(" main - root logger ".center(55, "-"))
    commons.use_logger(root_logger)
    commons.logger_infos(root_logger)


def use_warnings():
    import warnings
    print(" main - warnings.warn ".center(55, "-"))
    warnings.warn("Message from 'warnings' module")


if __name__ == "__main__":
    test_logger()
    use_warnings()
