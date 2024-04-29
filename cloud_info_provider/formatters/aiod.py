from cloud_info_provider.formatters import base


class AIOD(base.BaseFormatter):
    def __init__(self):
        self.template_extension = "aiod.json.tmpl"
        self.templates = ["compute", "storage"]
