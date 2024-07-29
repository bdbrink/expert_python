import sys

match sys.platform:
    case "windows":
        print("Running w box")
    case "darwin":
        print("Running mac os x86")
    case "linux":
        print("running linux king")
    case _:
        raise NotImplementedError(f"{sys.platform} not supported!")