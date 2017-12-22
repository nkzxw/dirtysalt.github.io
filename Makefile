deploy:
	./scripts/publish
	ssh hkvps "cd dirtysalt.github.io; git pull"

@PHONY: deploy
