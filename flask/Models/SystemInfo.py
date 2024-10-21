class SystemInfo:
    def __init__(
        self,
        system,
        node,
        release,
        version,
        platform,
        architecture,
        device,
        brand,
        model,
        browser,
        browser_version,
        os,
        os_version,
        page,
    ):
        self.system = system
        self.node = node
        self.release = release
        self.version = version
        self.platform = platform
        self.architecture = architecture
        self.device = device
        self.brand = brand
        self.model = model
        self.browser = browser
        self.browser_version = browser_version
        self.os = os
        self.os_version = os_version
        self.page = page

    def to_dict(self):
        return {
            "system": self.system,
            "node": self.node,
            "release": self.release,
            "version": self.version,
            "platform": self.platform,
            "architecture": self.architecture,
            "device": self.device,
            "brand": self.brand,
            "model": self.model,
            "browser": self.browser,
            "browser_version": self.browser_version,
            "os": self.os,
            "os_version": self.os_version,
            "page": self.page,
        }
