# Define variables
APP_NAME := flask_app  # You can replace 'flask_app' with your desired container name
DOCKER_IMAGE := flask_image  # You can replace 'flask_image' with your desired image name
DOCKERFILE_DIR := ./flask  # Path to the folder containing Dockerfile
PORT := 5000

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE) $(DOCKERFILE_DIR)

# Run the Docker container
run:
	docker run -d -p $(PORT):5000 --name $(APP_NAME) $(DOCKER_IMAGE)

# Stop the Docker container
stop:
	docker stop $(APP_NAME)

# Remove the Docker container
remove:
	docker rm $(APP_NAME)

# Restart the Docker container
restart: stop remove run

# Remove the Docker image
remove-image:
	docker rmi $(DOCKER_IMAGE)

# Clean up stopped containers and unused images
clean:
	docker system prune -f

# Run the Flask app in Docker using bash
shell:
	docker exec -it $(APP_NAME) /bin/bash
