midterm.build:
	@docker build -t ros:midterm -f docker/Dockerfile .

midterm.create: 
	@./run_scripts/run.bash

	
midterm.shell:
	@docker exec -it ros-midterm bash

midterm.up:
	@xhost +
	@docker start ros-midterm

midterm.down:	
	@docker stop ros-midterm


midterm.remove: 
	@docker container rm ros-midterm

#: Show a list of containers.
list:
	@docker container ls -a

#: Show a list of containers.
listUp:
	@docker ps
