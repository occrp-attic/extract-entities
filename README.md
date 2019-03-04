# extract-entities

This is a simple gRPC service to manage the extraction of named entities from text
using one of several open source tools. The main reason for having this run in a
service is to avoid inlining the required training data and Python dependencies in
the main aleph application.

## Usage

In order to use this container, you need to use the same protocol buffer specifications
active on the server. The simplest way to use them would be via the `servicelayer` Python
library, but the protocol can also be used independently.

Check out the following client code to see how `extract-entities` is used:

https://github.com/alephdata/servicelayer/blob/master/servicelayer/rpc/__init__.py

You can also inspect the protocol buffer files directly here:

https://github.com/alephdata/servicelayer/tree/master/protos/servicelayer/rpc

The container itself can be pulled from the DockerHub and will expose a service on port
`50000`:

```shell
docker pull alephdata/recognize-text
docker run -p 50000:50000 -ti alephdata/recognize-text
```

### NER backend options

* https://github.com/zalandoresearch/flair
* https://github.com/aboSamoor/polyglot
* https://spacy.io/
