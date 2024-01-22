from face_authentication.utils.util import CommonUtils


SECRET_KEY = CommonUtils().get_environment_variable("SECRET_KEY")
ALGORITHM = CommonUtils().get_environment_variable("ALGORITHM")