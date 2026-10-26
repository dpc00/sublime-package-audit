Status: not sent. hevp/sublime-sparql-runner has GitHub issues disabled (last pushed 2019-11-27, not archived). No contact address checked; kept as a finding.

Claude reports:

Sublime Text build 4215, Windows, SPARQL Runner 1.2.0 from Package Control's Install Package list.

## 1. The default endpoint always shows an error dialog (and also opens the results)

Steps: new `.rq` file with `SELECT ?s WHERE { ?s ?p ?o } LIMIT 3`, "SPARQL: Select endpoint" and pick the shipped `dbpedia` entry, then "SPARQL: Run query".

After about 35 seconds a "SPARQL Query Results" tab opens with the XML result (three rows), and at the same time a dialog says:

```
SPARQL Runner.SPARQLRunner: Error Response content type not supported: application/sparql-results+xml running query
```

Cause (`SPARQLRunner.py`, `QueryRunner.run`): the request has no `Accept` header, so dbpedia answers `application/sparql-results+xml` (checked with curl: HTTP 303 to https, then 200). The code stores `self.result = res.read().decode("utf-8")` first and only then compares the content type with `text/plain` and `application/json`; anything else raises "Response content type not supported". The result is shown anyway, so the user gets both the data and an error.

Fix: send `Accept: application/sparql-results+json` (what the JSON branch expects), and either accept XML too (show it as text) or raise before storing the body.

## 2. By reading (not run): the JSON branch reads the response body twice

```python
self.result = res.read().decode("utf-8")
...
elif ctype == "application/json":
    self.result = self.format_result(res.read())
```

The second `read()` returns `b""` because the body was consumed by the first. `format_result` then gets an empty value. I could not reach this branch with the default endpoint (it answers XML, see 1), so this is from reading only.

Fix: parse the text already read: `self.format_result(self.result)` (and check what `format_result` expects, since it is given bytes here).

## 3. Minor

- The query runs with no timeout on `urlopen`; the status bar shows "Running your query on ..." until the server answers (10 s with curl, about 35 s in Sublime including the 303 redirect). Nothing tells the user the endpoint redirected to https.
- `SelectSparqlEndpointCommand` is a window command; running "SPARQL: Run query" with no endpoint selected shows the expected dialog "You should add/select an endpoint using 'SPARQL: Select endpoint' command." (works as designed).

Not tested: endpoints with username/password, the `prefixes` setting, adding a new endpoint through the input panels.
