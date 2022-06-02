# The repo address for the docker image in artifact registry
# replace with your own repo
IMAGE=us-central1-docker.pkg.dev/proven-script-347020/som-repo/som:latest

# run self organising map
build:
	docker build -t "$(IMAGE)" . 

push:
	docker push "$(IMAGE)"

pull:
	docker pull "$(IMAGE)"

run_som:
	docker run \
		-it --rm \
		-p 80:80 \
		--volume "$(shell pwd)/som_plots:/som_plots:rw" \
		"$(IMAGE)" > logs/local_pipeline.log
