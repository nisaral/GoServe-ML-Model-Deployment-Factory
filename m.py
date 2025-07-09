import os

project_structure = {
    "goserve": {
        "README.md": "",
        ".gitignore": "",
        "docker": {
            "Dockerfile.api": "",
            "Dockerfile.ui": "",
            "docker-compose.yml": "",
        },
        "cmd": {
            "api": {
                "main.go": "",
            },
        },
        "internal": {
            "config": {
                "config.go": "",
            },
            "db": {
                "db.go": "",
            },
            "handlers": {
                "api.go": "",
            },
            "models": {
                "experiment.go": "",
                "model.go": "",
            },
        },
        "pkg": {
            "utils": {
                "logger.go": "",
            },
        },
        "webui": {
            "package.json": "",
            "vite.config.js": "",
            "public": {},
            "src": {
                "App.jsx": "",
                "components": {},
                "pages": {},
            },
        },
        "scripts": {
            "run_db_migrations.sh": "",
            "run_tests.sh": "",
            "deploy.sh": "",
        },
        "ci-cd": {
            ".github": {
                "workflows": {
                    "ci-cd.yml": "",
                },
            },
            "Jenkinsfile": "",
        },
        "configs": {
            "config.yml": "",
            "logging.yml": "",
        },
        "tests": {
            "unit": {},
            "integration": {},
            "e2e": {},
        },
        "monitoring": {
            "prometheus.yml": "",
            "grafana": {
                "dashboards": {},
            },
            "alerts": {},
        },
        "docs": {
            "design.md": "",
            "api.md": "",
            "usage.md": "",
            "architecture.png": "",
        },
        "migrations": {
            "001_init.sql": "",
        },
        "go.mod": "",
        "go.sum": "",
        "Makefile": "",
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

base_dir = "goserve"
os.makedirs(base_dir, exist_ok=True)
create_structure(base_dir, project_structure["goserve"])
print(f"Project structure created at {os.path.abspath(base_dir)}")
