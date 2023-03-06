import os.path


def base_dir(*files):
    return os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", *files))


class Assets:
    @staticmethod
    def assets_dir(*files):
        return base_dir("assets", *files)

    @staticmethod
    def icons(*files):
        return Assets.assets_dir("icons", *files)

    @staticmethod
    def fonts(*files):
        return Assets.assets_dir("fonts", *files)

    @staticmethod
    def themes(*files):
        return Assets.assets_dir("themes", *files)

    @staticmethod
    def data(*files):
        return Assets.assets_dir("data", *files)
