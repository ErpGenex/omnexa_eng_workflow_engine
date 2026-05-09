### Omnexa Eng Workflow Engine

Workflow engine extraction stub. **Production behaviour** still lives in `omnexa_engineering_consulting`; this app declares `required_apps = ["omnexa_engineering_consulting"]` and exposes `consulting_bridge.get_workflow_facade()` for gradual code moves.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app omnexa_eng_workflow_engine
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/omnexa_eng_workflow_engine
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
