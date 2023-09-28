# FastStream Application

Application in this repository is developed using the `FastStream` framework. Below, you'll find a guide on how to get started, develop new features or bug fixes, and ensure the quality of your code through testing and linting.

## Getting Started

To set up your development environment, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/faststream-app.git
   cd faststream-app
   ```

2. Install all development requirements using pip:

   ```bash
   pip install -e ".[dev]"
   ```

## Development

The application code is located in the `app/` directory. You can add new features or fix bugs in this directory. However, remember that code changes must be accompanied by corresponding updates to the tests located in the `tests/` directory.

## Running Tests

Before running tests, make sure you have a Kafka Docker container running. You can start it locally using the provided script:

```bash
./scripts/start_kafka_broker_locally.sh
```

Once the Kafka container is up and running, you can execute the tests using pytest:

```bash
pytest
```

## Code Linting

After making changes to the code, it's essential to ensure it adheres to coding standards. We provide a script to help you with code formatting and linting. Run the following script to automatically fix linting issues:

```bash
./scripts/lint.sh
```

## Static Analysis

Static analysis tools `mypy` and `bandit` can help identify potential issues in your code. To run static analysis, use the following script:

```bash
./scripts/static-analysis.sh
```

If there are any static analysis errors, resolve them in your code and rerun the script until it passes successfully.

## Contributing

Once you have successfully completed all the above steps, you are ready to contribute your changes:

1. Add and commit your changes:

   ```bash
   git add .
   git commit -m "Your commit message"
   ```

2. Push your changes to GitHub:

   ```bash
   git push origin your-branch
   ```

3. Create a merge request on GitHub.

## Continuous Integration (CI)

This repository is equipped with GitHub Actions that automate static analysis and pytest in the CI pipeline. Even if you forget to perform any of the required steps, CI will catch any issues before merging your changes.

---

Happy coding with FastStream Application! If you have any questions or encounter any problems, feel free to reach out to us. We appreciate your contributions and commitment to maintaining code quality.
