# FastStream Application

Application in this repository is developed using the `FastStream` framework. Below, you'll find a guide on how to get started, develop new features or bug fixes, and ensure the quality of your code through testing and linting, run the `FastStream` application locally, and view `AsyncAPI` documentation.

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

Once you have updated tests, you can execute the tests using `pytest`:

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

## Running FastStream Application Locally

To run the `FastStream` application locally, follow these steps:

1. Start the Kafka Docker container locally using the provided script:

   ```bash
   ./scripts/start_kafka_broker_locally.sh
   ```

2. Start the `FastStream` application with the following command:

   ```bash
   faststream run app.application:app --workers 1
   ```

3. You can now send messages to the Kafka topic and can test the application. Optionally, if you want to view messages in a topic, you can subscribe to it using the provided script:

   ```bash
   ./scripts/subscribe_to_kafka_broker_locally.sh <topic_name>
   ```

4. To stop the `FastStream` application, press `Ctrl+C`.

5. Finally, stop the Kafka Docker container by running the script:

   ```bash
   ./scripts/stop_kafka_broker_locally.sh
   ```

## Viewing AsyncAPI Documentation

`FastStream` framework supports `AsyncAPI` documentation. To ensure that your changes are reflected in the `AsyncAPI` documentation, follow these steps:

1. Ensure you have Node.js installed locally. If not, you can download and install it from [here](https://nodejs.org/en/download/package-manager).

2. Run the following script to view the `AsyncAPI` documentation:

   ```bash
   ./scripts/serve_asyncapi_docs.sh
   ```

   This command builds the `AsyncAPI` specification file, generates `AsyncAPI` documentation based on the specification, and serves it at `localhost:8888`.

3. Open your web browser and navigate to <http://localhost:8888> to view the `AsyncAPI` documentation reflecting your changes.

4. To stop the `AsyncAPI` documentation server, press `Ctrl+C`.

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

Happy coding with `FastStream` Application! If you have any questions or encounter any problems, feel free to reach out to us. We appreciate your contributions and commitment to maintaining code quality.
