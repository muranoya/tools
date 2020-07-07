# scrub-json

This is the tool that rewrites JSON file specific items at once.

# How to use

```bash
./main.py <json file> <key1> <data1> <key2> <data2> ... <key n> <data n>
```

`<json file>` is consisted from 1 line 1 json.

e.g.

```json
{"apple": 100, "grape": 200}
{"apple": 80, "grape": 230}
```

This is OK but the following is NG.

```json
{"apple": 100, "grape": 200},{"apple": 80, "grape": 230}
```

If `key1` is in json, it will be replaced with `data1`.