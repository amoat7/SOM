# The repo address for the docker image in artifact registry
# replace with your own repo
IMAGE=us-central1-docker.pkg.dev/proven-script-347020/kohonen/kohonen:latest

# run self organising map
build:
	docker build -t "$(IMAGE)" . 

push:
	docker push "$(IMAGE)"

pull:
	docker pull "$(IMAGE)"


use_som_local:
	docker run \
		-it --rm \
		--entrypoint python \
		--volume "$(shell pwd)/som_plots:/som_plots:rw" \
		--volume "$(shell pwd)/use_som:/use_som:rw" \
		"$(IMAGE)"\
		/use_som/use_som_local.py > logs/local.log

use_som_gcp:
	docker run \
		-it --rm \
		--entrypoint python \
		--volume "$(shell pwd)/som_plots:/som_plots:rw" \
		--volume "$(shell pwd)/use_som:/use_som:rw" \
		"$(IMAGE)"\
		/use_som/use_som_gcp.py > logs/gcp.log

