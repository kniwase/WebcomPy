from dataclasses import dataclass, field

@dataclass
class WebComPyConfig:
    app_package: str
    base: str = "/"
    server_port: int = 8080
    static_files_dir: str = "static"
    dist: str = "dist"
    dependencies: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.base = f"/{base}/" if (base := self.base.strip("/")) else "/"
