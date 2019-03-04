
all: build

build:
	docker build -t alephdata/extract-entities .

shell: build
	docker run -v $(PWD):/service -ti alephdata/extract-entities sh

run: build
	docker run -ti -p 50000:50000 alephdata/extract-entities