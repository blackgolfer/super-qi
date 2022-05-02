cleanupdocker:
	@docker ps -a -f status=exited -q | xargs --no-run-if-empty docker rm
	@docker images --filter "dangling=true" -q | xargs --no-run-if-empty docker rmi

# documents
.PHONY: html
html:
	$(MAKE) -C docs html
