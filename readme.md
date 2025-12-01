# Guest Concierge Platform

Welcome to the Guest Concierge Platform! This is a .NET Core application configured for containerized development with Docker.

The setup is optimized for a productive development experience with hot-reloading.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following software installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Running the Application

1.  **Clone the repository:**

    ```sh
    git clone <your-repository-url>
    cd Guest-Concierge-Platform
    ```

2.  **Build and run the application using Docker Compose:**

    ```sh
    docker-compose up --build
    ```

3.  **Access the application:**

    Once the container is running, the application will be available at [http://localhost:8080](http://localhost:8080).

## Development Workflow

This project is configured for hot-reloading during development:

- **Code Changes (`.cs` files):** When you modify and save a C# file, `dotnet watch` will automatically recompile and restart the application inside the container.
- **Project Dependency Changes (`.csproj` file):** When you change a `.csproj` file (e.g., adding a NuGet package), `docker-compose watch` will automatically trigger a rebuild of the Docker image to restore the new dependencies.

This ensures a fast and efficient development loop without needing to manually restart or rebuild the container for most changes.